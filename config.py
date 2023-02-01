from aiogram import types, Bot, executor, Dispatcher
from data import Api_token
from buttons import menyumain, menyuBack

bot = Bot(token=Api_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start(message:types.Message):
    await message.answer("✋Salom bu bot mars it school kurslari \nHaqida malumot beradigan bot", reply_markup=menyumain)

@dp.message_handler(text='starter')
async def info_starter(message:types.Message):
    await message.answer("👉Bu kursimiz 3 oy davom etadi.\nSiz bu kursda kompyuter ishlatishni organasiz",reply_markup=menyuBack)

@dp.message_handler(text='Orqaga qaytish')
async def info_starter(message:types.Message):
    await message.answer("👇Kerakli bolimni tanlang",reply_markup=menyumain)

@dp.message_handler(text='Frontend')
async def info_starter(message:types.Message):
    await message.answer("👉Bu kursimiz 6 oy davom etadi.\nBu kursda kodlar yozishni o'rganasiz",reply_markup=menyuBack)

@dp.message_handler(text='Dasturlash')
async def info_starter(message:types.Message):
    await message.answer("👉Bu kursimiz 6 oy davom etadi.\nBu kursda saytlar qilishni o'rganasiz",reply_markup=menyuBack)

@dp.message_handler(text='Dizayn')
async def info_starter(message:types.Message):
    await message.answer("👉Bu kursimiz 6 oy davom etadi.\nBu kursda 3D yasashni organasiz",reply_markup=menyuBack)

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)