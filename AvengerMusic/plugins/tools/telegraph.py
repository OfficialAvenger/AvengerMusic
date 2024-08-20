# sangram
import os
from pyrogram import filters
from telegraph import upload_file
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AvengerMusic import app


@app.on_message(filters.command("tgm"))
async def gentelegraph(_, message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("Reply To Some Media")
    if reply.media or reply.sticker:  # Check if replied message is media or sticker
        try:
            i = await message.reply("Generating Telegraph Link....")
            if reply.media:
                path = await reply.download()
            else:
                # For stickers, save as webp format
                path = await reply.download(file_name="sticker.webp")
                
            fk = upload_file(path)
            for x in fk:
                url = "https://graph.org/" + x

            await i.edit(f'[𝖸𝗈𝗎𝗋 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖫𝗂𝗇𝗄 𝗂𝗌 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾𝖽.]({url})', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Telegraph", url =f"{url}"), InlineKeyboardButton ("Share", url=f"https://telegram.me/share/url?url={url}")]]))
            os.remove(path)
        except Exception as e:
            await i.edit(f"ERROR: **{e}**")
            os.remove(path)
