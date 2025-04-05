from typing import TYPE_CHECKING, Dict, List, Union

from loguru import logger
from pydantic import BaseModel

from slark.types.documents.blocks import common as t_block

if TYPE_CHECKING:
    from slark.client.lark import AsyncLark


class Block(BaseModel):
    parent: Union["Block", None] = None
    children: List["Block"] = []
    data: t_block.BlockInfo


class BuildOptions(BaseModel):
    assets_path: str = "./assets/"
    level: int = 0


class PageHelper:
    _client: "AsyncLark"
    block_datas: Dict[str, t_block.BlockInfo]
    page: Block

    def __init__(self, blocks: List[t_block.BlockInfo], client: "AsyncLark") -> "PageHelper":
        """由 BlockInfo 列表构建页面，第一个 BlockInfo 必须为 Page 类型

        Args:
            blocks (List[t_block.BlockInfo]): 文档的 BlockInfo 列表
        """
        assert len(blocks) > 0, "blocks 不能为空"
        assert blocks[0].block_type == t_block.BlockType.PAGE, "第一个 BlockInfo 必须为 Page 类型"

        self.block_datas: Dict[str, t_block.BlockInfo] = {}
        """初始化 Block 数据"""
        for block in blocks:
            self.block_datas[block.block_id] = block

        """构建页面"""
        self.page = self._build_block(blocks[0])
        self._client = client

    def _build_block(self, block_info: t_block.BlockInfo, parent: Block = None) -> Block:
        """构建 Block 对象

        Args:
            block_info (t_block.BlockInfo): Block 的信息
            parent (Block, optional): 父 Block 对象. Defaults to None.

        Returns:
            Block: 构建好的 Block 对象
        """
        block = Block(parent=parent, data=block_info)
        if block_info.children is None:
            return block
        for child_id in block_info.children:
            if child_id not in self.block_datas:
                raise ValueError(f"Block {child_id} 不存在")
            child_block = self._build_block(self.block_datas[child_id], block)
            block.children.append(child_block)
        return block

    async def to_markdown(self, assets_path: str = "./assets/") -> str:
        """将页面转换为 Markdown

        Returns:
            str: Markdown 字符串
        """
        return await self._block_to_markdown(self.page, BuildOptions(assets_path=assets_path))

    async def _text_run_to_markdown(self, text_run: t_block.TextRun):
        md = text_run.content
        if not text_run.text_element_style:
            return md
        if text_run.text_element_style.bold:
            md = f" **{md}** "
        if text_run.text_element_style.italic:
            md = f" *{md}* "
        if text_run.text_element_style.strikethrough:
            md = f" ~~{md}~~ "
        if text_run.text_element_style.underline:
            md = f" _{md}_ "
        if text_run.text_element_style.inline_code:
            md = f" `{md}` "
        if text_run.text_element_style.link:
            from urllib.parse import unquote

            url = unquote(text_run.text_element_style.link.url)
            md = f" [{md}]({url}) "
        """忽略 background_color 和 foreground_color"""
        return md

    async def _equation_to_markdown(self, equation: t_block.Equation):
        return f"$$ {equation.content.strip()} $$"

    async def _mention_doc_to_markdown(self, mention_doc: t_block.MentionDoc):
        return f" [{mention_doc.title}]({mention_doc.url}) "

    async def _text_element_to_markdown(
        self, styles: Union[t_block.TextStyle, None], element: t_block.TextElement
    ):
        if element.text_run:
            return await self._text_run_to_markdown(element.text_run)
        if element.equation:
            return await self._equation_to_markdown(element.equation)
        if element.mention_doc:
            return await self._mention_doc_to_markdown(element.mention_doc)
        return ""

    async def _text_to_markdown(self, text: t_block.Text, type: t_block.BlockType):
        md = "".join(
            [await self._text_element_to_markdown(text.style, element) for element in text.elements]
        )
        """Ingore the children of text block, maybe will be a bug"""
        if not text.style:
            return md
        if text.style.indentation_level == t_block.TextIndentationLevel.ONE_LEVEL_INDENT:
            md = "    " + md
        if type == t_block.BlockType.CODE_BLOCK:
            md = f"```{text.style.language.name.lower()}\n{md}\n```"
        elif type == t_block.BlockType.QUOTE:
            md = f"> {md}"
        elif type == t_block.BlockType.TODO:
            done = "x" if text.style.done else " "
            md = f"- [{done}] {md}"
        elif type.name.startswith("TITLE"):
            md = f"{'#' * int(type.name[-1])} {md}"
        elif type == t_block.BlockType.PAGE:
            md = f"# {md}\n"
        return md

    async def _list_to_markdown(
        self, block: Block, options: BuildOptions, block_type: t_block.BlockType
    ):
        ordered = block_type == t_block.BlockType.ORDERED_LIST
        heading = "1. " if ordered else "- "
        data = block.data.ordered if ordered else block.data.bullet
        assert data is not None, "list 数据不能为空"
        md = await self._text_to_markdown(data, block_type)

        md = "    " * options.level + heading + md
        md = [md]
        for child in block.children:
            options.level += 1
            md.append(await self._block_to_markdown(child, options))
            options.level -= 1
        return "\n".join(md)

    async def _callout_to_markdown(self, callout: Block, options: BuildOptions):
        md = []
        for block in callout.children:
            md.append(f"> {await self._block_to_markdown(block, options=options)}")
        return "\n".join(md)

    async def _divider_to_markdown(self, divider: Block):
        return "---"

    async def _table_to_markdown(self, table: Block, options: BuildOptions):
        assert table.data.table is not None, "table 数据不能为空"
        assert len(table.data.table.cells) == len(table.children), "table 数据长度不匹配"

        def _list_to_row(items: List[str]):
            return "|" + "|".join(items) + "|"

        property = table.data.table.property
        md = []
        for cell in table.children:
            assert cell.data.table_cell is not None, "table_cell 数据不能为空"
            md.append(await self._table_cell_to_markdown(cell, options=options))
        rows = property.row_size
        cols = property.column_size
        header_row = property.header_row
        assert len(md) == rows * cols, "table 数据长度不匹配"
        table_md = []
        for row in range(rows):
            table_md.append(_list_to_row(md[row * cols : (row + 1) * cols]))
        if not header_row:
            table_md.insert(0, _list_to_row(["" for _ in range(cols)]))
        table_md.insert(1, _list_to_row([":---" for _ in range(cols)]))
        return "\n".join(table_md)

    async def _table_cell_to_markdown(self, table_cell: Block, options: BuildOptions):
        md = []
        for block in table_cell.children:
            md.append(await self._block_to_markdown(block, options=options))
        return "\n".join(md)

    async def _quote_container_to_markdown(self, quote_container: Block, options: BuildOptions):
        md = []
        for block in quote_container.children:
            md.append(f"> {await self._block_to_markdown(block, options=options)}")
        return "\n".join(md)

    async def _board_to_markdown(self, board: t_block.Board, options: BuildOptions):
        if options.assets_path is None:
            return ""
        logger.debug(f"Downloading board {board.token} as image to {options.assets_path}")
        path = await self._client.board.download_as_image(board.token, save_dir=options.assets_path)
        return f"![board]({path})"

    async def _image_to_markdown(self, image: t_block.Image, options: BuildOptions):
        if options.assets_path is None:
            return ""
        logger.debug(f"Downloading image {image.token} to {options.assets_path}")
        info = await self._client.assets.download(image.token, save_dir=options.assets_path)
        return f"![{info.filename}]({info.filepath})"

    async def _block_to_markdown(self, block: Block, options: BuildOptions):
        block_type = block.data.block_type
        if block.data.page:
            md = await self._text_to_markdown(block.data.page, block_type)
            md = [
                md,
                *[await self._block_to_markdown(child, options) for child in block.children],
            ]
            return "\n".join(md)
        elif block.data.text:
            return await self._text_to_markdown(block.data.text, block_type)
        elif block.data.heading1:
            return await self._text_to_markdown(block.data.heading1, block_type)
        elif block.data.heading2:
            return await self._text_to_markdown(block.data.heading2, block_type)
        elif block.data.heading3:
            return await self._text_to_markdown(block.data.heading3, block_type)
        elif block.data.heading4:
            return await self._text_to_markdown(block.data.heading4, block_type)
        elif block.data.heading5:
            return await self._text_to_markdown(block.data.heading5, block_type)
        elif block.data.heading6:
            return await self._text_to_markdown(block.data.heading6, block_type)
        elif block.data.heading7:
            return await self._text_to_markdown(block.data.heading7, block_type)
        elif block.data.heading8:
            return await self._text_to_markdown(block.data.heading8, block_type)
        elif block.data.heading9:
            return await self._text_to_markdown(block.data.heading9, block_type)
        elif block.data.bullet:
            return await self._list_to_markdown(block, options=options, block_type=block_type)
        elif block.data.ordered:
            return await self._list_to_markdown(block, options=options, block_type=block_type)
        elif block.data.code:
            return await self._text_to_markdown(block.data.code, block_type)
        elif block.data.equation:
            return await self._text_to_markdown(block.data.equation, block_type)
        elif block.data.quote:
            return await self._text_to_markdown(block.data.quote, block_type)
        elif block.data.todo:
            return await self._text_to_markdown(block.data.todo, block_type)
        elif block.data.callout:
            return await self._callout_to_markdown(block, options=options)
        elif block.data.divider:
            return await self._divider_to_markdown(block)
        elif block.data.table:
            return await self._table_to_markdown(block, options=options)
        elif block.data.quote_container:
            return await self._quote_container_to_markdown(block, options=options)
        elif block.data.board:
            return await self._board_to_markdown(block.data.board, options=options)
        elif block.data.image:
            return await self._image_to_markdown(block.data.image, options=options)
        return ""
