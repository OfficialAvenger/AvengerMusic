from pyrogram.types import InlineKeyboardButton
import config

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [           
            InlineKeyboardButton(
                text="𝖸𝗈𝗎𝖳𝗎𝖻𝖾", url=f"https://youtube.com/"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
