from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menyumain = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="starter"),
            KeyboardButton(text="Frontend"),
        ],
        [
            KeyboardButton(text="Dasturlash"),
            KeyboardButton(text="Dizayn"),
        ]
    ],
    resize_keyboard=True
)


menyuBack = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Orqaga qaytish")
        ]
    ],
    resize_keyboard=True
)