from dotenv import find_dotenv, load_dotenv

from slark import AsyncLark, EventManager
from slark.types.event.common import EventType, LarkEvent

load_dotenv(find_dotenv())
lark = AsyncLark()
em = EventManager(lark)


@em.register(EventType.IM_MESSAGE_RECEIVE_V1)
async def test_event(lark: AsyncLark, ev: LarkEvent):
    message = ev.event.message
    if message.message_type == "image":
        await lark.messages.get_resource(
            message.message_id, message.content.image_key, "image", "uploads"
        )


em.listen(port=54467)
