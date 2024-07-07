import os
from pyrogram import filters, enums, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from AvengerMusic import app
from config import BANNED_USERS

@app.on_message(filters.command("id"), group=10)
async def uid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    mention_user = message.from_user.mention
    message_id = message.id
    reply = message.reply_to_message

    text = f"Your ID is <code>{your_id}</code>\n\n"

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            user_mention = (await client.get_users(split)).mention 
            text += f"User {user_mention}'s ID is <code>{user_id}</code>\n"

        except Exception:
            return await message.reply_text("No User Found")


    if not getattr(reply, "empty", True) and not message.forward_from_chat and not reply.sender_chat:
        text += f"Replied User ID » <code>{reply.from_user.id}</code>\n\n"

    if reply and reply.forward_from_chat:
        text += f"The Forwarded Channel, {reply.forward_from_chat.title}, Has an ID of: <code>{reply.forward_from_chat.id}</code>\n\n"        
    
    if reply and reply.sender_chat:
        text += f"The ID of Replied Chat/Channel: <code>{reply.sender_chat.id}</code>"
        
    await message.reply(text)



@app.on_message(
    filters.command("gifid") & (filters.group | filters.private),
)
async def get_gifid(_, m: Message):
    if m.reply_to_message and m.reply_to_message.animation:
        await m.reply_text(
            f"<b>Gif ID :</b>\n<code>{m.reply_to_message.animation.file_id}</code>",
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await m.reply_text(text="Please reply to a gif to get it's ID.")
    return



# Define the command handler
@app.on_message(filters.command("stickerid"))
async def stickerid(client, message):
    # Check if the message is a reply and contains a sticker
    if message.reply_to_message and message.reply_to_message.sticker:
        sticker_id = message.reply_to_message.sticker.file_id
        await message.reply_text(
            f"<b>The sticker ID is:</b>\n <code>{sticker_id}</code>",
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await message.reply_text("Please reply to a sticker to get its ID.")






n = "\n"
w = " "

bold = lambda x: f"**{x}:** "
bold_ul = lambda x: f"**--{x}:**-- "
mono = lambda x: f"`{x}`{n}"


def section(title: str, body: dict, indent: int = 2, underline: bool = False) -> str:
    text = (bold_ul(title) + n) if underline else bold(title) + n
    for key, value in body.items():
        text += (indent * w + bold(key) + ((value[0] + n) if isinstance(value, list) else mono(value)))
    return text


async def get_user_info(user, already=False):
    if not already:
        user = await app.get_users(user)
    if not user.first_name:
        return ["𝖣𝖾𝗅𝖾𝗍𝖾𝖽 𝖠𝖼𝖼𝗈𝗎𝗇𝗍", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("ʟɪɴᴋ")
    mlink = user.mention()
    uname = ("@" + username) if username else mlink
    dc_id = user.dc_id
    photo_id = user.photo.big_file_id if user.photo else None
    is_scam = user.is_scam
    is_restricted = user.is_restricted
    caption = f"""<b><u>𝖴𝖲𝖤𝖱 𝖨𝖭𝖥𝖮</u></b>

<b>𝖭𝖺𝗆𝖾:</b> {first_name}
<b>𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾:</b> {uname}
<b>𝖬𝖾𝗇𝗍𝗂𝗈𝗇:</b> {mention}
<b>𝖴𝗌𝖾𝗋 𝖨𝖣:</b> <code>{user_id}</code>
<b>𝖣𝖢 𝖨𝖣:</b> <code>{dc_id}</code>
<b>𝖲𝖼𝖺𝗆:</b> {is_scam}
<b>𝖱𝖾𝗌𝗍𝗋𝗂𝖼𝗍𝖾𝖽:</b> {is_restricted}"""
    return [caption, photo_id]


async def get_chat_info(chat, already=False):
    if not already:
        chat = await app.get_chat(chat)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    is_scam = chat.is_scam
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    if username:
        link = f"@{username}"
    else:
        try:
            clink = await app.export_chat_invite_link(chat_id)
            link = f"<a href={clink}>private</a>"
        except:
            link = "ᴘʀɪᴠᴀᴛᴇ"
            pass
    photo_id = chat.photo.big_file_id if chat.photo else None
    caption = f"""<b><u>𝖢𝖧𝖠𝖳 𝖨𝖭𝖥𝖮</u></b>

<b>𝖭𝖺𝗆𝖾:</b> {title}
<b>𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾:</b> {link}
<b>𝖢𝗁𝖺𝗍 𝖨𝖣:</b> <code>{chat_id}
<b>𝖬𝖾𝗆𝖻𝖾𝗋𝗌:</b> <code>{members}</code>
<b>𝖲𝖼𝖺𝗆:</b> {is_scam}
<b>𝖱𝖾𝗌𝗍𝗋𝗂𝖼𝗍𝖾𝖽:</b> {is_restricted}
<b><u>𝖣𝖾𝗌𝖼𝗋𝗂𝗉𝗍𝗂𝗈𝗇</u>:</b>
<code>{description}</code>"""
    return [caption, photo_id]


@app.on_message(filters.command("info") & ~BANNED_USERS)
async def info_func(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("𝖯𝗋𝗈𝖼𝖾𝗌𝗌𝗂𝗇𝗀......")
    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await app.download_media(photo_id)

    await message.reply_photo(photo=photo, caption=info_caption, quote=True, parse_mode=ParseMode.HTML)
    await m.delete()
    os.remove(photo)


@app.on_message(filters.command("chatinfo") & ~BANNED_USERS)
async def chat_info_func(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) > 2:
            return await message.reply_text("**ᴜsᴀɢᴇ:** /chatinfo [username|id]")
        if len(message.command) == 1:
            chat = message.chat.id
        elif len(message.command) == 2:
            chat = message.text.split(None, 1)[1]
            
        m = await message.reply_text("𝖯𝗋𝗈𝖼𝖾𝗌𝗌𝗂𝗇𝗀......")
        info_caption, photo_id = await get_chat_info(chat)
        if not photo_id:
            return await m.edit(info_caption, disable_web_page_preview=True)

        photo = await app.download_media(photo_id)
        await message.reply_photo(photo=photo, caption=info_caption, quote=True, parse_mode=ParseMode.HTML)
        await m.delete()
        os.remove(photo)
    except Exception as e:
        await m.edit(e)
     
