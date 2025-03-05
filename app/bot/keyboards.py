from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Добавить', callback_data='main:add'),
    ],
    [
        InlineKeyboardButton(text='Список', callback_data='main:list'),
    ],
])
