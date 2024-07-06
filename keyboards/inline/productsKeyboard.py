from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

from keyboards.inline.callback_data import course_callback, book_callback

#1-usul

categoryMenu=InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
        InlineKeyboardButton(text="📑Kurslar",callback_data='courses'),
        InlineKeyboardButton(text="📕Kitoblar",callback_data="books"),
    ],
    [
        InlineKeyboardButton(text="🐍Python saytiga kirish",url="https://docs.python.org/")
    ],
    [
        InlineKeyboardButton(text='🔍Qidirsh',switch_inline_query_current_chat="")
    ],
    [
        InlineKeyboardButton(text='📤Ulashish',switch_inline_query='zo\'r bot ekan')
    ],
    ]
)


#kurslar uchun menyu

coursesMenu=InlineKeyboardMarkup(row_width=1)

python=InlineKeyboardButton(text='🐍Python asoslari',callback_data=course_callback.new(item_name='python'))
coursesMenu.insert(python)

django=InlineKeyboardButton(text="🌐Django Web Dasturlash",callback_data=course_callback.new(item_name='django'))
coursesMenu.insert(django)

telegram=InlineKeyboardButton(text="♾Mukammal Telegram bot",callback_data='course:telegram')
coursesMenu.insert(telegram)

algorithm=InlineKeyboardButton(text='🔗Malumotlar va algoritm tuzilmasi',callback_data='course:algorithm')
coursesMenu.insert(algorithm)

back_button=InlineKeyboardButton(text="🔙Ortga",callback_data='cancel')
coursesMenu.insert(back_button)

#3-usul

books={
    "Python.Dasturlash asoslari":"python_book",
    "C++.Dasturlash asoslari":"cpp_book",
    "Mukammal Dasturlash.JavaScript":"js_book"
}

books_menu=InlineKeyboardMarkup(row_width=1)
for key,value in books.items():
    books_menu.insert(InlineKeyboardButton(text=key,callback_data=book_callback.new(item_name=value)))
books_menu.insert(back_button)

#har bir kurs uchun tugma

telegram_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Kursni ko\'rish',url="https://mohirdev.uz/kurslar/telegram/")
        ],
    ],
)

algorithm_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ma'lumotlar tuzilmasi va algoritm kursi",url="https://mohirdev.uz/kurslar/algoritmlar/")
        ],
    ],
)

django_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Django Framework dokumentatsiyasini ko\'rish',url="https://docs.djangoproject.com/en/5.0/")
        ]
    ]
)

python_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Python asoslari bilan tanishish",url="https://python.sariq.dev/")
        ]
    ]
)

