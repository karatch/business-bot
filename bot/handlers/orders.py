from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State


router = Router()

class OrderForm(StatesGroup):
    name = State()
