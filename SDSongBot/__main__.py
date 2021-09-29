#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm powerful Song Downloader Bot 🎵
🎧 Just send me the song name you want to download.🎧
      eg:```/song Pretty savage black pink 🖤 ```
      
A bot by @IMkashyapaa
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
                        text="Dev🎵", url="https://t.me/IMkashyapaa"
                    ),
                    InlineKeyboardButton(
                        text="⚒️🎙️share my bot🎙️⚒️", url="https://t.me/share/url?url=t.me/Kashyapasgdlbot"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ KashyapaSongBot is online.")
idle()
