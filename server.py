import anyio
from dotenv import find_dotenv, load_dotenv
from fastapi import BackgroundTasks
from fastapi.responses import JSONResponse

from card_docdb import build_docdb_save_card
from slark import AsyncLark, EventManager
from slark.types.event import CallbackResponse, CallbackToast, EventType, LarkEvent

load_dotenv(find_dotenv())
lark = AsyncLark()
em = EventManager(lark)


@em.register(EventType.IM_MESSAGE_RECEIVE_V1)
async def test_event(lark: AsyncLark, ev: LarkEvent):
    value = {"file_key": ev.event.message.content, "file_type": "message"}
    card = build_docdb_save_card(stage="ask", value=value)
    return await lark.messages.reply_card(ev.event.message.message_id, card=card)


@em.register(EventType.CARD_ACTION_TRIGGER, run_in_thread=False)
async def card_action_trigger(lark: AsyncLark, ev: LarkEvent):
    value = ev.event.action.value
    from pprint import pprint

    pprint(value)
    if value["event"] != "save_to_docdb":
        return JSONResponse(
            content=CallbackResponse(
                toast=CallbackToast(type="info", content="未知事件"),
            ).model_dump(),
        )

    async def reply():
        input_value = ev.event.action.form_value.get("input_save_to_docdb")
        card = build_docdb_save_card(stage="saving", input_value=input_value, value=value)
        await lark.messages.edit_card(ev.event.context.open_message_id, card)
        await anyio.sleep(1)
        card = build_docdb_save_card(stage="success", input_value=input_value, value=value)
        await lark.messages.edit_card(ev.event.context.open_message_id, card)
        await anyio.sleep(1)
        card = build_docdb_save_card(stage="fail", input_value=input_value, value=value)
        await lark.messages.edit_card(ev.event.context.open_message_id, card)

    tasks = BackgroundTasks()
    tasks.add_task(reply)
    return JSONResponse(
        content=CallbackResponse(
            toast=CallbackToast(type="info", content="保存中"),
        ).model_dump(),
        background=tasks,
    )


em.listen(port=54467)
