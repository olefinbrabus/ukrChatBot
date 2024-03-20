import asyncio
import logging
import config

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from database.db_manager_rules import DatabaseManagerRules
from site_manager.manager import SiteManager
from views.handlers import router


async def main():
    # Starts the bot
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types())


def initialize_db():
    manager = SiteManager()
    examples = DatabaseManagerRules("examples")
    examples.update_db(manager.get_proceed_rules)


if __name__ == '__main__':
    initialize_db()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

