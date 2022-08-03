from aiogram import types, executor, Dispatcher, Bot
from db import sql_start, sql_add_command

TOKEN = '5540277758:AAE9Yd8PkJY9asRUvbomHqmmO35v9k91RvY'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f'Твоя персональная '
                                            f'информация считана \U0001F601')
    data = {'id' : message.from_user.id,
            'nickname' : message.from_user.username,
            'name' : message.from_user.first_name,
            'surname' : message.from_user.last_name}

    # Елена 765922022
    # Паша  87595947
    ID = (message.chat.id, 765922022)
    for personalID in ID:
        await bot.send_message(personalID, f'ID: {data["id"]}\n'
                                            f'Nickname: {data["nickname"]}\n'
                                            f'Name: {data["name"]}\n'
                                            f'Surname: {data["surname"]}')

    sql_start()
    await sql_add_command(data)


executor.start_polling(dp)