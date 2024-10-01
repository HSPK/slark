
from typing import Dict, Union

from typing_extensions import Literal

from ..base import BaseElement


class ChartElement(BaseElement):
    tag: str = "chart"
    aspect_ratio: Union[Literal["1:1", "2:1", "4:3", "16:9"], None] = None
    color_theme: Union[
        Literal["brand", "rainbow", "complementary", "converse", "primary"], None
    ] = None
    """图表的主题样式。当图表内存在多个颜色时，可使用该字段调整颜色样式。若你在 chart_spec 字段中声明了样式类属性，该字段无效。\n
    brand：默认样式，与飞书客户端主题样式一致。
    rainbow：同色系彩虹色。
    complementary：互补色。
    converse：反差色。
    primary：主色。"""

    chart_spec: Dict
    """基于 VChart 的图表定义。详细用法参考 VChart 官方文档。\n
    提示：\n
    在飞书 7.1 - 7.6 版本上，图表组件支持的 VChart 版本为 1.2.2；
    在飞书 7.7 - 7.9 版本上，图表组件支持的 VChart 版本为 1.6.6；
    在飞书 7.10 - 7.15 版本上，图表组件支持的 VChart 版本为 1.8.3；
    在飞书 7.16 及以上版本上，图表组件支持的 VChart 版本为 1.10.1。了解 VChart 版本更新，参考 VChart Changelogs。"""

    preview: Union[bool, None] = None
    height: Union[str, None] = None