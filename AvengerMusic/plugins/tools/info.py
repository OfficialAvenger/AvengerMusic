from pyrogram import filters, enums, Client
from pyrogram.types import Message
from AvengerMusic import app

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
        await message.reply_text(f"**The sticker ID is:**\n `{sticker_id}`")
    else:
        await message.reply_text("Please reply to a sticker to get its ID.")
