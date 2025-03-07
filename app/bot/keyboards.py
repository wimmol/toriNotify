from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Add a filter', callback_data='main:add'),
    ],
    [
        InlineKeyboardButton(text='Filters list', callback_data='main:list'),
    ],
])
#❌
just_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Back', callback_data='main:back'),
    ]
])

def generate_remove_list(links_list):
    n = len(links_list)
    keyboard = [[InlineKeyboardButton(text='Back', callback_data='main:back')]]
    line = []
    for i in range(n):
        line.append(InlineKeyboardButton(text=f'❌{i + 1}', callback_data=f'remove:{links_list[i]["id"]}'))
        if (i+1) % 4 == 0 or i + 1 == n:
            keyboard.append(line)
            line = []
    print(keyboard)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)