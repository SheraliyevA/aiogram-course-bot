from aiogram import types
from loader import dp


@dp.message_handler(commands='info_html')
async def bot_info(message: types.Message):
    text = f"Assalomu Alaykum <b>{message.from_user.full_name}</b>!\n"
    text += "Bu <a href='https://github.com/SheraliyevA'>Github profilim</a>\n"
    await message.answer(text)


