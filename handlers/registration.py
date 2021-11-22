from aiogram.dispatcher.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, bot, _


@dp.message_handler(Command('start'))
async def registration(message: Message):
    chat_id = message.from_user.id
    await message.answer(text='Choose ur language')
    # Отдадим пользователю клавиатуру с выбором языков
    languages_markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(text="Русский", callback_data="lang_ru")],
            [
                InlineKeyboardButton(text="English", callback_data="lang_en"),
                InlineKeyboardButton(text="Українська", callback_data="lang_uk"),
            ]
        ]
    )

    # Для многоязычности, все тексты, передаваемые пользователю должны передаваться в функцию "_"
    # Вместо "текст" передаем _("текст")

    text = _("Приветствую вас!!\n")
    await bot.send_message(chat_id, text, reply_markup=languages_markup)
