from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для запуска бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, с чем может помочь бот'),
        types.BotCommand(command='/info', description='Информация о боте'),
        types.BotCommand(command='/authors', description='Создатели бота'),
        types.BotCommand(command='/support', description='Поддержка проекта')

    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.reply('Привет, я эхо-бот')

@dp.message_handler(commands= 'help')
async def start(message: types.Message):
    await message.reply('Я могу помочь тебе с твоей проблемой')

@dp.message_handler(commands= 'info')
async def start(message: types.Message):
    await message.reply('Бот, который дублирует ваше сообщение')

@dp.message_handler(commands= 'authors')
async def start(message: types.Message):
    await message.reply('Создатель бота: @blyadec')

@dp.message_handler(commands= 'support')
async def start(message: types.Message):
    await message.reply('Помогите')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)