from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, base


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.first_name
    username = message.from_user.username
    tg_id = message.from_user.id

    try:
        base.foydalanuvchi_qoshish(
            name=name,
            username=username, 
            tg_id=tg_id
            )
    except Exception:
        pass


    await message.answer(f"Assalom alekum, <b>{message.from_user.full_name}</b>! \n\n📌Facebook'dagi videolarni yuklab beruvchi bot ishga tushdi, facebook'dan video linkini menga jo'nating, men sizga videoni yuboraman. \n\n👨🏼‍💻Author: <a href='https://t.me/Asadbek_Muxtorov'>Asadbek Muxtorov</a>")

