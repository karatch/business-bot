from aiogram import Router, F  # маршрутизатор для обработки сообщений
from aiogram.fsm.context import FSMContext  #  контекст конечного автомата состояний
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from bot.config import settings

# маршрутизатор для обработки входящих сообщений
router = Router()

# форма заявки
class OrderForm(StatesGroup):
    name = State()
    contact = State()
    comment = State()

@router.message(F.text == 'Оформить заявку')
async def order_start(message: Message, state: FSMContext) -> None:
    await message.answer('Как вас зовут?')
    await state.set_state(OrderForm.name)

@router.message(OrderForm.name)
async def order_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text.strip())
    await message.answer('Укажите, пожалуйста, удобный способ связи (телефон или @username).')
    await state.set_state(OrderForm.contact)

@router.message(OrderForm.contact)
async def order_contact(message: Message, state: FSMContext) -> None:
    await state.update_data(contact=message.text.strip())
    await message.answer('Опишите, что именно вас интересует (товар, услуга, время и т.п.).')
    await state.set_state(OrderForm.comment)

@router.message(OrderForm.comment)
async def order_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text.strip())
    data = await state.get_data()
    await state.clear()

    text = (
        '<b>Новая заявка</b>\n'
        f'Имя: {data['name']}\n'
        f'Контакт: {data['contact']}\n'
        f'Комментарий: {data['comment']}'
    )

    await message.answer('Спасибо! Заявка отправлена менеджеру.')
    # await message.bot.send_message(chat_id=settings.admin_chat_id, text=text)
    await message.answer(text)