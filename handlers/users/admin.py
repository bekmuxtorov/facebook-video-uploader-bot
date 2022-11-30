from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, base, bot

@dp.message_handler(commands='list_users', chat_id = ('1603330179', '1362417011'))
async def bot_echo(message: types.Message):
    text = ''
    user_id = message.from_user.id
    list_users = base.select_users()
    for i in range(len(list_users)):
        text += f"\n<b>{i+1}-user</b>\n" \
                f"<b>Ismi:</b> {list_users[i][0]}\n" \
                f"<b>ID:</b> {list_users[i][2]}\n" \
                f"<b>Username:</b> @{list_users[i][1]}\n" \
                f"{'➖'*10}"
    
    await bot.send_message(chat_id=user_id, text=text)
