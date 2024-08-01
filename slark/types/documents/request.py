from typing import List, Union

from typing_extensions import Literal

from slark.types._common import BaseModel


class GetRawContentParams(BaseModel):
    lang: Union[Literal[0, 1, 2], None] = None
    """指定返回的 MentionUser 即 @用户 的语言。\
        示例值：0。\
        可选值有：\n
            0：该用户的默认名称。如：@张敏。\n
            1：该用户的英文名称。如：@Min Zhang。\n
            2：暂不支持该枚举，使用时返回该用户的默认名称。\n
        默认值：0"""

