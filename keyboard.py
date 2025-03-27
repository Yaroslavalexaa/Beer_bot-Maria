from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup ,
                           InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Популярные сорта и стоимость")],[KeyboardButton(text="Сервиc и доставка")],
                                     [KeyboardButton(text="Написать менеджеру")], [KeyboardButton(text="Запросить прайс")]],
                           resize_keyboard=True)

