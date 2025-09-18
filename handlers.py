from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import keyboard as kb

 #для class dialog
from aiogram.fsm.context import FSMContext
from keyboard import InlineKeyboardMarkup, InlineKeyboardButton



router = Router ()

@router.message (CommandStart())
async def cmd_start (message: Message):
    await message.answer(f"{message.from_user.first_name}, добро пожаловать в бот! Выберите пункт меню.", reply_markup=kb.main)


@router.message (F.text == 'Популярные сорта и стоимость')
async def dia (message:Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text='Популярные сорта и стоимость',
            url='link',
        )]
    ])
    await message.answer("Перейдите по ссылке. ", reply_markup = markup)



@router.message(F.text == 'Сервиc и доставка')
async def delivery (message: Message):
    await message.answer(
        "Мы предлагаем самые конкурентоспособные цены напрямую от производителя.\n\n "
        "Для наших постоянных партнеров - индивидуальные условия, такие как отсрочка платежа, дополнительные скидки и фирменный мерч.\n\n"
        "Полное документальное сопровождение.\n\n"
        "Необходимый температурный режим и упаковку при перевозке и хранении.\n\n"
        "<b>Доставка:</b>\n\n"
        "Мы предоставляем услуги доставки по Москве и Московской области.\n"
        "<b>В пределах МКАД стоимость доставки составляет 700 рублей.</b>\n"
        "При заказе от <b>15 000 рублей</b> доставка по городу <b>БЕСПЛАТНО</b>.\n"
        "При доставке <b>за пределы МКАД и в регионы России</b> стоимость рассчитывается индивидуально.\n"
        "При регулярных поставках предусмотрены <b>специальные условия</b>.",
        parse_mode="HTML"
    )






