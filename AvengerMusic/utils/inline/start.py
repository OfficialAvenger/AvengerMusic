from pyrogram.types import InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters

import config
from AvengerMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text="Premium", callback_data="alert_message"),
        ],
    ]
    return buttons


@app.on_callback_query(filters.regex("alert_message"))
def alert_message_func(_, query: CallbackQuery):
    query.answer("Comming soon 🔜", show_alert=True)


# You can add more code to start the Pyrogram client and handle other functionalities.
