from typing_extensions import Literal

from slark.types._common import BaseModel

NodeTypes = Literal["doc", "docx", "sheet", "mindnote", "bitable", "file", "slides", "wiki"]


class GetNodeQuery(BaseModel):
    """节点详情GET请求参数
    https://open.feishu.cn/document/server-docs/docs/wiki-v2/space-node/get_node
    """

    token: str
    """"知识库或文档的 token。
        了解如何获取 token https://open.feishu.cn/document/server-docs/docs/faq#560bf735"""
    obj_type: NodeTypes = "wiki"
    """文档类型。不传时默认以wiki类型查询。
        可选值有：doc：旧版文档
        docx：新版文档
        sheet：表格
        mindnote：思维导图
        bitable：多维表格
        file：文件
        slides：幻灯片
        wiki：知识库节点"""
