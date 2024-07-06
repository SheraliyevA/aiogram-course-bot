from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menuStart=ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🗂Kurslar"),
            KeyboardButton(text="📑Qo'llanma")
        ],
    ],
    resize_keyboard=True
)