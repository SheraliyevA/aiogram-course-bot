import logging

from keyboards.inline.callback_data import course_callback, book_callback
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, books_menu, telegram_keyboard, \
    algorithm_keyboard, django_keyboard
from aiogram.types import Message, CallbackQuery
from loader import dp


@dp.message_handler(text_contains='Kurslar')
async def select_category(message: Message):
    await message.answer('Kursni tanlang', reply_markup=categoryMenu)

@dp.message_handler(text_contains='Qo\'llanma')
async def select_category(message: Message):
    await message.answer('Botdan foydalanish uchun 📔Kurslar bo\'limiga kiring!')

@dp.callback_query_handler(text='courses')
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    logging.info(f"{call.from_user.id=}")
    await call.message.answer('Kursni tanlang', reply_markup=coursesMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains='books')
async def buy_books(call: CallbackQuery):
    await call.message.answer('Kitobni tanlang', reply_markup=books_menu)
    await call.message.delete()
    await call.answer(cache_time=60)


# Callback yordamida filtrlash

@dp.callback_query_handler(course_callback.filter(item_name='telegram'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuchidan qaytgam callbackni ko'ramiz!

    logging.info(f"{callback_data=}")
    await call.message.answer("Siz mukammmal telegram bot kursini tanladingiz", reply_markup=telegram_keyboard)
    await call.answer(cache_time=60)


@dp.callback_query_handler(course_callback.filter(item_name='algorithm'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuchidan qaytgam callbackni ko'ramiz!

    logging.info(f"{callback_data=}")
    await call.message.answer("Siz ma'lumotlar tuzilmasini va algoritmlar kursini tanladingiz",
                              reply_markup=algorithm_keyboard)
    await call.answer(cache_time=60)


@dp.callback_query_handler(course_callback.filter(item_name='django'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuchidan qaytgam callbackni ko'ramiz!

    logging.info(f"{callback_data=}")
    await call.message.answer("Siz django kursini tanladingiz", reply_markup=django_keyboard)
    await call.answer(cache_time=60)


@dp.callback_query_handler(course_callback.filter(item_name='python'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuchidan qaytgam callbackni ko'ramiz!

    logging.info(f"{callback_data=}")
    await call.message.answer("Siz python asoslari kursini tanladingiz", reply_markup=algorithm_keyboard)
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name='python_book'))
async def buying_book(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuchidan qaytgam callbackni ko'ramiz!

    logging.info(f"{callback_data=}")
    await call.answer("So'rovingiz qabul qilindi!", cache_time=60, show_alert=True)


@dp.callback_query_handler(book_callback.filter(item_name='cpp_book'))
async def buying_book(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuchidan qaytgam callbackni ko'ramiz!

    logging.info(f"{callback_data=}")
    await call.answer("So'rovingiz qabul qilindi!", cache_time=60, show_alert=True)


@dp.callback_query_handler(book_callback.filter(item_name='js_book'))
async def buying_book(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuchidan qaytgam callbackni ko'ramiz!

    logging.info(f"{callback_data=}")
    await call.answer("So'rovingiz qabul qilindi!", cache_time=60, show_alert=True)


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    # oynada javob qaytaramiz
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()
