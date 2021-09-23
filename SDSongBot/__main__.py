#CgsOfficialBOTs <https://t.me/cgs_official>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """ 
https://telegra.ph/file/73422b014dca50b1023e6.jpg Hey [{}](tg://user?id={}), I'm Song Downloader Bot Made by @IMkashyapaa🎵

🎶🎧 Just send me the song name you want to download.😋
      eg:```/song Kill this love```

👻Main supporter @Kmsrk     
🤖A bot by @IMkashyapaa
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Our Channel🎧", url="https://t.me/cgs_official"
                    ),
                    InlineKeyboardButton(
                        text="Contact me🔥", url="https://telegram.me/IMkashyapaa"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ CgsOfficialBOTs is online.")
idle()
