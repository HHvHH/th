import random
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)

from sbb_b import StartTime, sbb_b, sbb_bversion

from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention


@sbb_b.ar_cmd(pattern="فحص$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    sbb_bevent = await edit_or_reply(
        event,
        "**⌔∮ عزيزي المستخدم اذا هذه الرسالة بقت ولم تظهر لك كليشه الفحص يرجى اضاف الكليشه بشكل صحيح مره اخرى**",
    )
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ☬"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "| **سورس ريثون** |"
    sbb_b_IMG = gvarstatus("ALIVE_PIC")
    sbb_b_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = sbb_b_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jmver=sbb_bversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if sbb_b_IMG:
        sbb_b = [x for x in sbb_b_IMG.split()]
        PIC = random.choice(sbb_b)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await sbb_bevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                sbb_bevent,
                f"**عليك استخدام رابط تليجراف لا يمكن استخدام اي رابط ثاني واعد استخدام الامر  ⪼  `.اضف صورة الحماية` <بالرد على الرابط> ",
            )
    else:
        await edit_or_reply(
            sbb_bevent,
            caption,
        )


temp = """{ALIVE_TEXT}
**{EMOJI} مطــور الســـورس :** @HvvHH
**{EMOJI} قاعدۿ البيانات :** `{dbhealth}`
**{EMOJI} أصـدار التـيليثون :** `{telever}`
**{EMOJI} أصـدار السورس :** `{jmver}`
**{EMOJI} الوقت :** `{uptime}` 
**{EMOJI} أصدار البـايثون :** `{pyver}` """



from sbb_b import sbb_b
from telethon import events
from telethon import version
from platform import python_version

@sbb_b.ar_cmd(pattern="بنىمخثخلي$")
async def _(event):
    await event.delete()
    jmthonget = await event.get_sender()
    hnarsl = event.to_id
    jmthon_pic = "https://telegra.ph/file/c8670dda3dfd70d763e14.jpg"
    await sbb_b.send_file(hnarsl, jmthon_pic, caption=f"اهلا بك {jmthonget.first_name}\n\n اصدار ريثون: 5.0.0\n اصدار البايثون: {python_version()}\n اصدار التيليثون: {version.__version__}\n\nشكرا لك\nريثون™")
