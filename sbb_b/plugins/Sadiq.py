import os
from datetime import datetime

from sbb_b import sbb_b

from . import hmention, reply_id

"""
try:
    from . import PING_PIC, PING_TEXT
except:
    pass
"""
plugin_category = "tools"

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/c8db372d36b015419396c.mp4"
)

HSO_TXT = os.environ.get("PING_TEXT") or "اختناق 💔🚬"


@sbb_b.ar_cmd(
    pattern="؟$",
    command=("؟", plugin_category),
    info={
        "header": "nothing",
        "option": "nothing",
        "usage": [
            "{tr}",
        ],
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(
        event, "<b><i>اختناق 💔🚬</b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{HSO_TXT}<i><b>\nهنا ︙ @HmmHH<code>"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "hi", "html"
        )
