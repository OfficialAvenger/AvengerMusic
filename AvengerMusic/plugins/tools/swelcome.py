import os
import time
from datetime import datetime
import pytz
from unidecode import unidecode
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger

from AvengerMusic import app
from AvengerMusic.dbfiles.wel_db import *

LOGGER = getLogger(__name__)

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(450, 450)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chat, id, uname):
    background = Image.open("AvengerMusic/resources/bg.jpg")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize(
        (450, 450)
    ) 
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('AvengerMusic/resources/SwanseaBold-D0ox.ttf', size=40)
    welcome_font = ImageFont.truetype('AvengerMusic/resources/SwanseaBold-D0ox.ttf', size=60)
    draw.text((30, 300), f'Name : {unidecode(user)}', fill=(255, 255, 255), font=font)
    draw.text((30, 370), f'ID : {id}', fill=(255, 255, 255), font=font)
    draw.text((30, 40), f"Welcome to {unidecode(chat)}", fill=(225, 225, 225), font=welcome_font)
    draw.text((30,430), f"Username : @{uname}", fill=(255,255,255),font=font)
    pfp_position = (770, 140)  
    background.paste(pfp, pfp_position, pfp)  
    background.save(
        f"downloads/welcome#{id}.png"
    )
    return f"downloads/welcome#{id}.png"


@app.on_message(filters.command("swelcome") & ~filters.private)
async def auto_state(_, message):
    usage = "**Usage:**\n/swelcome [ENABLE|DISABLE]"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
      A = await wlcm.find_one({"chat_id" : chat_id})
      state = message.text.split(None, 1)[1].strip()
      state = state.lower()
      if state == "enable":
        if A:
           return await message.reply_text("Special Welcome Already Enabled")
        elif not A:
           await add_wlcm(chat_id)
           await message.reply_text(f"Enabled Special Welcome in {message.chat.title}")
      elif state == "disable":
        if not A:
           return await message.reply_text("Special Welcome Already Disabled")
        elif A:
           await rm_wlcm(chat_id)
           await message.reply_text(f"Disabled Special Welcome in {message.chat.title}")
      else:
        await message.reply_text(usage)
    else:
        await message.reply("Only Admins Can Use This Command")

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one({"chat_id" : chat_id})
    if not A:
       return
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "AvengerMusic/resources/profilepic.jpg"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        joined_date = datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
        ist = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist)
        Joined_time = current_time.strftime("%H:%M:%S %p")
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption= f"""
<b>WELCOME TO {member.chat.title}</b>

<b>Name :</b> {user.mention}
<b>ID :</b> {user.id}
<b>Username :</b> @{user.username}

<b>Join Date :</b> {joined_date}
<b>Join Time :</b> {Joined_time}
➖➖➖➖➖➖➖➖➖➖➖➖➖
""",
            reply_markup=InlineKeyboardMarkup([
    [InlineKeyboardButton("Add me to your Group", url="https://t.me/AvengerXrobot?startgroup=s&admin=delete_messages+pin_messages+invite_users+ban_users+change_info+manage_video_chats+add_admins")],
    [InlineKeyboardButton("Join for Updates", url="https://t.me/AvengerNews")]
])

            )
    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass



from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton

# Assuming 'app' is your Pyrogram Client instance

@app.on_chat_member_updated(filters.group)
async def member_has_left(client: Client, member: ChatMemberUpdated):

    if (
        not member.new_chat_member
        and member.old_chat_member.status not in {"banned", "left", "restricted"}
        and member.old_chat_member
    ):
        user = member.old_chat_member.user
        caption = (
            f"<b>Sad to see you leaving {user.mention}</b>"
        )
        deep_link = f"https://t.me/AvengerNews"
        button_text = "UPDATES"

        # Send the message with only text and a button
        await client.send_message(
            chat_id=member.chat.id,
            text=caption,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(button_text, url=deep_link)]
            ])
        )
