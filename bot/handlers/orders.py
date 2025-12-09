from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

router = Router()

class OrderForm(StatesGroup):
    name = State()

@router.message(F.text == 'Оформить заявку')
async def order_start(message: Message, state: FSMContext) -> None:
    await message.answer('Как вас зовут?')
    await state.set_state(OrderForm.name)