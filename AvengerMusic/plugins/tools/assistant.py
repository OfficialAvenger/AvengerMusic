from AvengerMusic.core.userbot import assistants
from AvengerMusic import userbot as us, app
from pyrogram import filters
from pyrogram.types import Message
from AvengerMusic.misc import SUDOERS
from config import BANNED_USERS, OWNER_ID


@app.on_message(filters.command(["asspfp", "setpfp"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("𝖢𝗁𝖺𝗇𝗀𝗂𝗇𝗀 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍'𝗌 𝖯𝗋𝗈𝖿𝗂𝗅𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾.....")
        img = await message.reply_to_message.download()
        if 1 in assistants:
           ubot = us.one
        try:
            await ubot.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"- {ubot.me.mention} 𝖯𝗋𝗈𝖿𝗂𝗅𝖾 𝗉𝗂𝖼𝗍𝗎𝗋𝖾 𝖼𝗁𝖺𝗇𝗀𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒."
            )
        except:
            return await fuk.edit_text("𝖥𝖺𝗂𝗅𝖾𝖽 𝗍𝗈 𝖼𝗁𝖺𝗇𝗀𝖾 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍'𝗌 𝖯𝗋𝗈𝖿𝗂𝗅𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾.")
    else:
        await message.reply_text(
            "𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝖯𝗁𝗈𝗍𝗈 𝖿𝗈𝗋 𝖢𝗁𝖺𝗇𝗀𝖾 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍'𝗌 𝖯𝗋𝗈𝖿𝗂𝗅𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾."
        )


@app.on_message(filters.command(["delpfp", "delasspfp"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
    try:
        if 1 in assistants:
           ubot = us.one
        pfp = [p async for p in ubot.get_chat_photos("me")]
        await ubot.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text( "𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 𝖣𝖾𝗅𝖾𝗍𝖾𝖽 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍'𝗌 𝖯𝗋𝗈𝖿𝗂𝗅𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾." )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("𝖥𝖺𝗂𝗅𝖾𝖽 𝗍𝗈 𝖽𝖾𝗅𝖾𝗍𝖾 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍'𝗌 𝖯𝗋𝗈𝖿𝗂𝗅𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾.")


@app.on_message(filters.command(["assbio", "setbio"]) & filters.user(OWNER_ID))
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            if 1 in assistants:
               ubot = us.one
            await ubot.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {ubot.me.mention} 𝖡𝗂𝗈 𝖢𝗁𝖺𝗇𝗀𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        if 1 in assistants:
           ubot = us.one
        await ubot.update_profile(bio=newbio)
        return await message.reply_text(f"» {ubot.me.mention} 𝖡𝗂𝗈 𝖢𝗁𝖺𝗇𝗀𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒.")
    else:
        return await message.reply_text(
            "𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗈𝗋 𝗀𝗂𝗏𝖾 𝗌𝗈𝗆𝖾 𝗍𝖾𝗑𝗍 𝗍𝗈 𝗌𝖾𝗍 𝗂𝗍 𝖺𝗌 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍'𝗌 𝖡𝗂𝗈."
        )


@app.on_message(filters.command(["assname", "setname"]) & filters.user(OWNER_ID))
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            if 1 in assistants:
               ubot = us.one
            await ubot.update_profile(first_name=name)
            return await message.reply_text(
                f"» {ubot.me.mention} 𝖭𝖺𝗆𝖾 𝖢𝗁𝖺𝗇𝗀𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        if 1 in assistants:
           ubot = us.one
        await ubot.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {ubot.me.mention} 𝖭𝖺𝗆𝖾 𝖢𝗁𝖺𝗇𝗀𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒.")
    else:
        return await message.reply_text(
            "𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗈𝗋 𝗀𝗂𝗏𝖾 𝗌𝗈𝗆𝖾 𝗍𝖾𝗑𝗍 𝗍𝗈 𝗌𝖾𝗍 𝗂𝗍 𝖺𝗌 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝗍'𝗌 𝖭𝖺𝗆𝖾."
        )
