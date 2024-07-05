import base64
import httpx
import os
import requests 
from pyrogram import filters
from AvengerMusic import app
from pyrogram import filters
import pyrogram
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


@app.on_message(filters.reply & filters.command("upscale"))
async def upscale_image(app, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            await message.reply_text("Please Reply to an Image to Upscale it.")
            return

        image = message.reply_to_message.photo.file_id
        file_path = await app.download_media(image)

        with open(file_path, "rb") as image_file:
            f = image_file.read()

        b = base64.b64encode(f).decode("utf-8")

        async with httpx.AsyncClient() as http_client:
            response = await http_client.post(
                "https://api.qewertyy.me/upscale", data={"image_data": b}, timeout=None
            )

        with open("upscaled.png", "wb") as output_file:
            output_file.write(response.content)

        await client.send_document(
            message.chat.id,
            document="upscaled.png",
            caption="**ʜᴇʀᴇ ɪs ᴛʜᴇ ᴜᴘsᴄᴀʟᴇᴅ ɪᴍᴀɢᴇ!**",
        )

    except Exception as e:
        print(f"Failed to Upscale the Image: {e}")
        await message.reply_text("Failed to Upscale the Image. Please try again later.")
