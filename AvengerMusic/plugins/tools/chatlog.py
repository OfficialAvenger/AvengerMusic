import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_GROUP_ID
from AvengerMusic import app 
from pyrogram.errors import RPCError
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]
sangram = "https://t.me/Red_Wine_Op"

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(chat.id)
    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            msg = (
                f"<b><u>#𝖭𝖤𝖶_𝖦𝖱𝖮𝖴𝖯</u></b>\n\n"
                f"**𝖢𝗁𝖺𝗍 𝖭𝖺𝗆𝖾 :** {chat.title}\n"
                f"**𝖢𝗁𝖺𝗍 𝖨𝖽 :** {chat.id}\n"
                f"**𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :** @{chat.username}\n"
                f"**𝖫𝗂𝗇𝗄 :** [𝖢𝗅𝗂𝖼𝗄]({link})\n"
                f"**𝖬𝖾𝗆𝖻𝖾𝗋𝗌 :** {count}\n"
                f"**𝖠𝖽𝖽𝖾𝖽 𝖡𝗒** {message.from_user.mention}"
            )
            await app.send_message(LOG_GROUP_ID, text=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url=f"{link}")]
            ]))

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"<b><u>#𝖫𝖤𝖥𝖳_𝖦𝖱𝖮𝖴𝖯</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
        
