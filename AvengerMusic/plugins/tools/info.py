from pyrogram import filters 
from pyrogram.types import Message
from AvengerMusic import app

@app.on_message(filters.command("id"), group=10)
async def uid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    mention_user = message.from_user.mention
    message_id = message.id
    reply = message.reply_to_message

    text = f"User **{mention_user}**'s ID is `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            user_mention = (await client.get_users(split)).mention 
            text += f"**[{user_mention}](tg://user?id={user_id})** » `{user_id}`\n"

        except Exception:
            return await message.reply_text("**No User Found**")

    text += f"\n**[Chat ID](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if not getattr(reply, "empty", True) and not message.forward_from_chat and not reply.sender_chat:
        text += f"**[Replied User ID](tg://user?id={reply.from_user.id})** » `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"The Forwarded Channel, {reply.forward_from_chat.title}, Has an ID of: `{reply.forward_from_chat.id}`\n\n"        
    
    if reply and reply.sender_chat:
        text += f"The ID of Replied Chat/Channel: `{reply.sender_chat.id}`"
        
    await message.reply(text)
