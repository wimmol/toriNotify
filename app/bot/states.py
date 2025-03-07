from aiogram.fsm.state import StatesGroup, State

class LinksList(StatesGroup):
    addingText = State()
    message_id = State()
