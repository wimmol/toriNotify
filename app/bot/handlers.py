import os

from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from aiogram import Router, types
from dotenv import load_dotenv

from app.bot.bot import bot
from app.bot.keyboards import main_keyboard, just_back_keyboard
from app.bot.states import LinksList
from app.bot.utils.display_links_list import display_links_list
from app.db.utils.links_utils import add_link, remove_link

load_dotenv()
ALLOWED_CHAT_ID = int(os.getenv("ALLOWED_CHAT_ID", "0"))

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    if message.chat.id != ALLOWED_CHAT_ID:
        return
    print(message.from_user.first_name)
    await message.answer(
        text=f'Hey, {message.from_user.first_name}.\n '
             f'There is a bot that sends notifications '
             f'for every new listed product on tori depend '
             f'on manageable filters',
        reply_markup=main_keyboard
    )

@router.callback_query(lambda c: c.data and c.data.startswith('main:'))
async def list_action(callback_query: types.CallbackQuery, state: FSMContext):
    main_action = callback_query.data.split(':')[1]
    if main_action == 'add':
        await state.set_state(LinksList.addingText)
        await state.update_data(message_id=callback_query.message.message_id)
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text='Send me a message:\n'
                 '<Filter name>!<Link>\n'
                 'In other words, in one message write'
                 'a name of a filter, then symbol "!"'
                 'and then paste the filter link',
            reply_markup=just_back_keyboard
        )
    if main_action == 'list':
        await display_links_list(callback_query)
    if main_action == 'back':
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text=f'Hey, {callback_query.message.from_user.first_name}.\n '
                 f'There is a bot that sends notifications '
                 f'for every new listed product on tori depend '
                 f'on manageable filters',
            reply_markup=main_keyboard
        )

@router.message(LinksList.addingText)
async def list_adding(message: Message, state: FSMContext):
    my_state = await state.get_data()
    textArray = message.text.split('!')
    add_link(message.chat.id ,textArray[0], textArray[1])
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=my_state['message_id'],
        text='✅ The filter has been added',
        reply_markup = main_keyboard
    )
    await state.clear()

@router.callback_query(lambda c: c.data and c.data.startswith('remove:'))
async def remove_action(callback_query: types.CallbackQuery):
    link_id = callback_query.data.split(':')[1]
    remove_link(int(link_id))

    await display_links_list(callback_query)