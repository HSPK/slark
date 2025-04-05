from typing import Dict, List, Union

from slark.types._common import BaseModel
from slark.types.response import BaseResponse

from .common import FieldValueType, User


class RecordResponseData(BaseModel):
    record_id: str
    """一条记录的唯一标识 id"""
    created_by: Union[User, None] = None
    """该记录的创建人"""
    created_time: Union[int, None] = None
    """该记录的创建时间"""
    last_modified_by: Union[User, None] = None
    """该记录最新一次更新的修改人"""
    last_modified_time: Union[int, None] = None
    """该记录最近一次的更新时间"""
    fields: Dict[str, FieldValueType]
    """数据表的字段，即数据表的列"""


class CreateRecordResponseData(BaseModel):
    record: RecordResponseData


class CreateRecordResponse(BaseResponse):
    """创建记录相应体
        Example:
        ```
        {
        "code": 0,
        "data": {
            "record": {
                "fields": {
                    "条码": "+$$3170930509104X512356",
                    "人员": [
                        {
                            "id": "ou_2910013f1e6456f16a0ce75ede950a0a"
                        },
                        {
                            "id": "ou_e04138c9633dd0d2ea166d79f548ab5d"
                        }
                    ],
                    "单向关联": [
                        "recHTLvO7x",
                        "recbS8zb2m"
                    ],
                    "单选": "选项3",
                    "双向关联": [
                        "recHTLvO7x",
                        "recbS8zb2m"
                    ],
                    "地理位置": "116.397755,39.903179",
                    "复选框": true,
                    "多行文本": "多行文本内容",
                    "多选": [
                        "选项1",
                        "选项2"
                    ],
                    "数字": 100,
                    "日期": 1674206443000,
                    "电话号码": "13026162666",
                    "索引": "索引列多行文本类型",
                    "超链接": {
                        "link": "https://www.feishu.cn/product/base",
                        "text": "飞书多维表格官网"
                    },
                    "附件": [
                        {
                            "file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"
                        }
                    ],
                    "群组": [
                        {
                            "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"
                        }
                    ],
                    "评分": 3,
                    "货币": 3,
                    "进度": 0.25
                },
                "id": "reclAqylTN",
                "record_id": "reclAqylTN"
            }
        },
        "msg": "success"
    }
    ```
    """

    data: CreateRecordResponseData


class UpdateRecordResponse(CreateRecordResponse):
    pass


class SearchRecordResponseData(BaseModel):
    items: List[RecordResponseData]
    """数组类型。record 结果。了解 record 数据结构，
    [参考数据结构](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/bitable/development-guide/bitable-structure)"""

    has_more: bool
    """是否还有更多项"""

    page_token: Union[str, None] = None
    """分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token"""

    total: int
    """总数"""


class SearchRecordResponse(BaseResponse):
    """搜索记录响应体
        Example:
        ```
        {
        "code":0,
        "data":{
            "has_more":false,
            "items":[
                {
                    "created_by":{
                        "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                        "email":"",
                        "en_name":"测试1",
                        "id":"ou_92945f86a98bba075174776959c90eda",
                        "name":"测试1"
                    },
                    "created_time":1691049973000,
                    "fields":{
                        "人员":[
                            {
                                "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/b2-7619-4b8a-b27b-c72d90b06a2j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                                "email":"zhangsan.leben@bytedance.com",
                                "en_name":"ZhangSan",
                                "id":"ou_2910013f1e6456f16a0ce75ede950a0a",
                                "name":"张三"
                            },
                            {
                                "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/v2_q86-fcb6-4f18-85c7-87ca8881e50j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                                "email":"lisi.00@bytedance.com",
                                "en_name":"LiSi",
                                "id":"ou_e04138c9633dd0d2ea166d79f548ab5d",
                                "name":"李四"
                            }
                        ],
                        "修改人":[
                            {
                                "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                                "email":"",
                                "en_name":"测试1",
                                "id":"ou_92945f86a98bba075174776959c90eda",
                                "name":"测试1"
                            }
                        ],
                        "创建人":[
                            {
                                "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                                "email":"",
                                "en_name":"测试1",
                                "id":"ou_92945f86a98bba075174776959c90eda",
                                "name":"测试1"
                            }
                        ],
                        "创建时间":1691049973000,
                        "单向关联":{
                            "link_record_ids":[
                                "recnVYsuqV"
                            ]
                        },
                        "单选":"选项1",
                        "双向关联":{
                            "link_record_ids":[
                                "recqLvMaXT",
                                "recrdld32q"
                            ]
                        },
                        "地理位置":{
                            "address":"东长安街",
                            "adname":"东城区",
                            "cityname":"北京市",
                            "full_address":"天安门广场，北京市东城区东长安街",
                            "location":"116.397755,39.903179",
                            "name":"天安门广场",
                            "pname":"北京市"
                        },
                        "复选框":true,
                        "多行文本":[
                            {
                                "text":"多行文本内容1",
                                "type":"text"
                            },
                            {
                                "mentionNotify":false,
                                "mentionType":"User",
                                "name":"张三",
                                "text":"@张三",
                                "token":"ou_2910013f1e6456f16a0ce75ede950a0a",
                                "type":"mention"
                            }
                        ],
                        "多选":[
                            "选项1",
                            "选项2"
                        ],
                        "数字":2323.2323,
                        "日期":1690992000000,
                        "最后更新时间":1702455191000,
                        "条码":[
                            {
                                "text":"123",
                                "type":"text"
                            }
                        ],
                        "电话号码":"131xxxx6666",
                        "自动编号":"17",
                        "群组":[
                            {
                                "avatar_url":"https://internal-api-lark-file.feishu-boe.cn/static-resource/v1/v2_c8d2cd50-ba29-476f-b7f1-5b5917cb18ej~?image_size=72x72&amp;cut_type=&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                                "id":"oc_cd07f55f14d6f4a4f1b51504e7e97f48",
                                "name":"武侠聊天组"
                            }
                        ],
                        "评分":3,
                        "货币":1,
                        "超链接":{
                            "link":"https://bitable.feishu.cn",
                            "text":"飞书多维表格官网"
                        },
                        "进度":0.66,
                        "附件":[
                            {
                                "file_token":"Vl3FbVkvnowlgpxpqsAbBrtFcrd",
                                "name":"飞书.jpeg",
                                "size":32975,
                                "tmp_url":"https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens=Vl3FbVk11owlgpxpqsAbBrtFcrd&amp;extra={"bitablePerm":{"tableId":"tblBJyX6jZteblYv","rev":90}}",
                                "type":"image/jpeg",
                                "url":"https://open.feishu.cn/open-apis/drive/v1/medias/Vl3FbVk11owlgpxpqsAbBrtFcrd/download?extra={"bitablePerm":{"tableId":"tblBJyX6jZteblYv","rev":90}}"
                            }
                        ]
                    },
                    "last_modified_by":{
                        "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                        "email":"",
                        "en_name":"测试1",
                        "id":"ou_92945f86a98bba075174776959c90eda",
                        "name":"测试1"
                    },
                    "last_modified_time":1702455191000,
                    "record_id":"recyOaMB2F"
                }
            ],
            "total":1
        },
        "msg":"success"
    }```
    """

    data: SearchRecordResponseData


class DeleteRecordResponseData(BaseModel):
    deleted: bool
    """是否成功删除"""
    record_id: str
    """删除的记录 ID"""


class DeleteRecordResponse(BaseResponse):
    """删除记录响应体
    Example:
    ```
    {"code": 0, "msg": "success", "data": {"deleted": true, "record_id": "recpCsf4ME"}}
    ```"""

    data: DeleteRecordResponseData


class BatchDeleteRecordResponseData(BaseModel):
    records: List[DeleteRecordResponseData]


class BatchDeleteRecordResponse(BaseResponse):
    """批量删除记录响应体
    Example:
    ```
    {
        "code": 0,
        "msg": "success",
        "data": {"records": [{"deleted": true, "record_id": "recpCsf4ME"}]},
    }
    ```"""

    data: BatchDeleteRecordResponseData


class BatchCreateRecordResponseData(BaseModel):
    records: List[RecordResponseData]


class BatchCreateRecordResponse(BaseResponse):
    """批量创建记录响应体
    Example:
    ```
    {
        "code": 0,
        "data": {
            "records": [
                {
                    "fields": {
                        "人员": [
                            {"id": "ou_2910013f1e6456f16a0ce75ede950a0a"},
                            {"id": "ou_e04138c9633dd0d2ea166d79f548ab5d"},
                        ],
                        "群组": [{"id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"}],
                        "单向关联": ["recHTLvO7x", "recbS8zb2m"],
                        "单选": "选项3",
                        "双向关联": ["recHTLvO7x", "recbS8zb2m"],
                        "地理位置": "116.397755,39.903179",
                        "复选框": true,
                        "多行文本": "多行文本内容",
                        "多选": ["选项1", "选项2"],
                        "数字": 100,
                        "日期": 1674206443000,
                        "条码": "qawqe",
                        "电话号码": "13026162666",
                        "索引": "索引列多行文本类型",
                        "超链接": {
                            "link": "https://www.feishu.cn/product/base",
                            "text": "飞书多维表格官网",
                        },
                        "附件": [{"file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"}],
                        "评分": 3,
                        "货币": 3,
                        "进度": 0.25,
                    },
                    "id": "recB8s1jUB",
                    "record_id": "recB8s1jUB",
                }
            ]
        },
        "msg": "success",
    }
    ```"""

    data: BatchCreateRecordResponseData


class BatchGetRecordResponseData(BaseModel):
    records: List[RecordResponseData]
    forbidden_record_ids: List[str]
    absent_record_ids: List[str]


class BatchGetRecordResponse(BaseResponse):
    """批量获取记录响应体
    Example:
    ```
    {
      "code": 0,
      "msg": "success",
      "data": {
        "forbidden_record_ids": [
          "recyOaMB2F"
        ],
        "absent_record_ids": [
          "rec111111"
        ],
        "records": [
          {
            "created_by": {
              "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
              "email": "",
              "en_name": "Min Zhang",
              "id": "ou_92945f86a98bba075174776959c90eda",
              "name": "张敏"
            },
            "created_time": 1691049973000,
            "fields": {
              "人员": [
                {
                  "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/b2-7619-4b8a-b27b-c72d90b06a2j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                  "email": "minzhang.leben@bytedance.com",
                  "en_name": "Min Zhang",
                  "id": "ou_2910013f1e6456f16a0ce75ede950a0a",
                  "name": "张敏"
                },
                {
                  "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/v2_q86-fcb6-4f18-85c7-87ca8881e50j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                  "email": "minzhang.00@bytedance.com",
                  "en_name": "Min Zhang",
                  "id": "ou_e04138c9633dd0d2ea166d79f548ab5d",
                  "name": "张敏"
                }
              ],
              "修改人": [
                {
                  "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                  "email": "",
                  "en_name": "Min Zhang",
                  "id": "ou_92945f86a98bba075174776959c90eda",
                  "name": "张敏"
                }
              ],
              "创建人": [
                {
                  "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                  "email": "",
                  "en_name": "Min Zhang",
                  "id": "ou_92945f86a98bba075174776959c90eda",
                  "name": "张敏"
                }
              ],
              "创建时间": 1691049973000,
              "单向关联": {
                "link_record_ids": [
                  "recnVYsuqV"
                ]
              },
              "单选": "选项1",
              "双向关联": {
                "link_record_ids": [
                  "recqLvMaXT",
                  "recrdld32q"
                ]
              },
              "地理位置": {
                "address": "东长安街",
                "adname": "东城区",
                "cityname": "北京市",
                "full_address": "天安门广场，北京市东城区东长安街",
                "location": "116.397755,39.903179",
                "name": "天安门广场",
                "pname": "北京市"
              },
              "复选框": true,
              "多行文本": [
                {
                  "text": "多行文本内容1",
                  "type": "text"
                },
                {
                  "mentionNotify": false,
                  "mentionType": "User",
                  "name": "张敏",
                  "text": "@张敏",
                  "token": "ou_2910013f1e6456f16a0ce75ede950a0a",
                  "type": "mention"
                }
              ],
              "多选": [
                "选项1",
                "选项2"
              ],
              "数字": 2323.2323,
              "日期": 1690992000000,
              "最后更新时间": 1702455191000,
              "条码": [
                {
                  "text": "123",
                  "type": "text"
                }
              ],
              "电话号码": "131xxxx6666",
              "自动编号": "17",
              "群组": [
                {
                  "avatar_url": "https://internal-api-lark-file.feishu-boe.cn/static-resource/v1/v2_c8d2cd50-ba29-476f-b7f1-5b5917cb18ej~?image_size=72x72&amp;cut_type=&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                  "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48",
                  "name": "武侠聊天组"
                }
              ],
              "评分": 3,
              "货币": 1,
              "超链接": {
                "link": "https://bitable.feishu.cn",
                "text": "飞书多维表格官网"
              },
              "进度": 0.66,
              "附件": [
                {
                  "file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd",
                  "name": "飞书.jpeg",
                  "size": 32975,
                  "tmp_url": "https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens=Vl3FbVk11owlgpxpqsAbBrtFcrd&amp;extra={"bitablePerm":{"tableId":"tblBJyX6jZteblYv","rev":90}}",
                  "type": "image/jpeg",
                  "url": "https://open.feishu.cn/open-apis/drive/v1/medias/Vl3FbVk11owlgpxpqsAbBrtFcrd/download?extra={"bitablePerm":{"tableId":"tblBJyX6jZteblYv","rev":90}}"
                }
              ]
            },
            "last_modified_by": {
              "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
              "email": "",
              "en_name": "Min Zhang",
              "id": "ou_92945f86a98bba075174776959c90eda",
              "name": "张敏"
            },
            "last_modified_time": 1702455191000,
            "record_id": "recyOaMB2F",
            "shared_url": "https://example.feishu.cn/record/KBcNrNtpWePAlscCvdmb6ZcSc5b"
          }
        ]
      }
    }
    ```"""

    data: BatchGetRecordResponseData


class BatchUpdateRecordResponse(BatchCreateRecordResponse):
    pass
