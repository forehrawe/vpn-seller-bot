from aiogram import Dispatcher, Bot
from config import BOT_TOKEN
from routers import setup_routers
from aiogram.client.telegram import TelegramAPIServer
import asyncio
from aiogram.client.session.aiohttp import AiohttpSession

api = TelegramAPIServer.from_base(
    base="http://127.0.0.1:8081"
)

session = AiohttpSession(api=api)

bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()

setup_routers(dp)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())