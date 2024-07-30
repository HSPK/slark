from typing_extensions import Literal

from slark.types._common import BaseModel
from slark.types.response.base import BaseResponse


class GetNodeResponseDataNode(BaseModel):
    space_id: str
    """知识空间id 获取方式 https://open.feishu.cn/document/server-docs/docs/wiki-v2/wiki-overview"""
    node_token: str
    """节点token"""
    obj_token: str
    """对应文档类型的token，可根据 obj_type 判断属于哪种文档类型。"""
    obj_type: Literal[
        "doc",
        "docx",
        "sheet",
        "mindnote",
        "bitable",
        "file",
        "slides",
    ]
    """文档类型，对于快捷方式，该字段是对应的实体的obj_type。
        
       可选值有：
       doc：旧版文档
       sheet：表格
       mindnote：思维导图
       bitable：多维表格
       file：文件
       docx：新版文档
       slides：幻灯片"""
    parent_node_token: str
    """父节点 token。若当前节点为一级节点，父节点 token 为空。"""
    node_type: Literal["origin", "shortcut"]
    """节点类型
    
       可选值有：
       origin：实体
       shortcut：快捷方式"""
    origin_node_token: str
    """快捷方式对应的实体node_token，当节点为快捷方式时，该值不为空。"""
    origin_space_id: str
    """	快捷方式对应的实体所在的space id"""
    has_child: bool
    """是否有子节点"""
    title: str
    """文档标题"""
    obj_create_time: str
    """文档创建时间"""
    obj_edit_time: str
    """文档最近编辑时间"""
    node_create_time: str
    """节点创建时间"""
    creator: str
    """文档创建者"""
    owner: str
    """文档所有者"""
    node_creator: str
    """节点创建者"""


class GetNodeResponseData(BaseModel):
    node: GetNodeResponseDataNode


class GetNodeResponse(BaseResponse):
    """获取节点详情返回数据
    https://open.feishu.cn/document/server-docs/docs/wiki-v2/space-node/get_node"""

    data: GetNodeResponseData
