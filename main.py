import asyncio
import confing
from aiogram import Bot, Dispatcher
import logging
from handlers.city import weather_search_ko, weather_search_lo, weather_search_mo
from handlers import common, weather_in_the_city



async def main():
    #Логирование
    logging.basicConfig(level=logging.INFO)

    #Обьект бота
    bot = Bot(token=confing.tokentelegrambot)

    #Обьект диспетчера
    dp = Dispatcher()

    dp.include_router(weather_in_the_city.router_weather)
    dp.include_router(common.router_common)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
