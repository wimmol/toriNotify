from aiogram import types

from app.bot.bot import bot
from app.bot.keyboards import generate_remove_list
from app.db.utils.links_utils import get_links


async def display_links_list(callback_query: types.CallbackQuery):
    links_list = get_links(callback_query.message.chat.id)
    list_text = ''.join(map(lambda x: f'{x[0] + 1}. {x[1]["name"]}\n', enumerate(links_list)))
    keyboard = generate_remove_list(links_list)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text='Filters list:\n' + list_text,
        reply_markup=keyboard)