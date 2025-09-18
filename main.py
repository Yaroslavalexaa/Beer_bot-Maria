import asyncio
from handlers import FSMContext
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.state import State, StatesGroup
from handlers import router, Message, F, CallbackQuery

class Order (StatesGroup):
    price = State()
    ask = State()


paused_users = set()


manager_id = id

async def main ():
    bot = Bot(token='your token', default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.include_router(router)
    router.bot = bot
    await dp.start_polling(bot)

@router.message (F.text == 'Написать менеджеру')
async def pause_bot (message: Message, state:FSMContext):
    await state.set_state(Order.ask)
    await message.answer(
        "Наши менеджеры оперативно на связи и готовы помочь. Напишите ваш вопрос:")

@router.message(Order.ask)
async def send_to_manager(message: Message, state: FSMContext):
    await state.update_data(ask=message.text)
    bot = router.bot
    data = await state.get_data()
    user_username = message.from_user.username if message.from_user.username else "Без username"

    await bot.send_message(chat_id=manager_id,
        text=f"⚠️ Клиент {message.from_user.full_name} ({user_username}) запросил общение с менеджером.\n\n"
                           f'Вопрос клиента: {data["ask"]}')

    await message.answer( "Спасибо за обращение! Скоро мы с вами свяжемся.")
    await state.clear()



@router.message (F.text == 'Запросить прайс')
async def noyes ( message: Message, state:FSMContext):
    await state.set_state(Order.price)
    await state.update_data(price=message.text)
    await message.answer(
        'Для отправки запроса прайса, напишите, пожалуйста, ваше имя и удобный способ связи (телефон, имейл, вотсап).\n\n '
        '*предоставляя данные, вы соглашаетесь с политикой конфиденциальности\n'
        " link")

@router.message(Order.price)
async def send_price_request(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    bot = router.bot
    user_username = message.from_user.username if message.from_user.username else "Без username"

    await bot.send_message(chat_id=MANAGER_ID,
                           text=f"⚠️ Клиент {message.from_user.full_name} ({user_username}) запросил стоимость.\n"
                                f'Данные клиента: {data["price"]}')

    await message.answer(
        "Отлично, отправили ваш запрос. Скоро мы с вами свяжемся.")
    await state.clear()





if __name__ == '__main__':
    try:
        asyncio.run (main())
    except KeyboardInterrupt:
         print ('Бот выключен')

