from pyrogram import filters
from pyrogram.types import Message

from AvengerMusic import app
from AvengerMusic.misc import SUDOERS
from AvengerMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>Example :</b>\n\n/autoend [enable | disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» Auto end Stream Enabled.\n\nAssistant will Automatically Leave the VideoChat after few Mins When No one is Listening."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» Auto End Stream Disabled.")
    else:
        await message.reply_text(usage)
