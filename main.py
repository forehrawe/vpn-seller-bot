from aiogram import Dispatcher, Bot
from config import BOT_TOKEN
from routers import setup_routers
import asyncio

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

setup_routers(dp)

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())