from aiogram import types
import re
from loader import dp, bot

from .facebook_download import upload_videos

REGEX = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'

def check(content, REGEX):
    if re.match(REGEX, content):
        return True
    else:
        return False
        
# Echo bot
@dp.message_handler(state=None)
async def bot_start(message: types.Message):
    matn = message.text
    user_id = message.from_user.id

    if check(matn, REGEX):
        await bot.send_message(chat_id=user_id, text="Video yuklanmoqda...")
        link_to_video = upload_videos(matn)
        caption = f"👉@download_mediabot"
        print(link_to_video)
        await bot.send_video(chat_id=user_id, video=link_to_video, caption=caption)
    else:
        await bot.send_message(chat_id=user_id, text="📌Iltimos menga Facebook'dagi video linkini jo'nating. \n\n👉@download_mediabot")
        
