""" Telegram Bot manager. """

import src.server
from aiogram import executor
from src.db.core import database_state


def dispatcher_register() -> None:
    src.server.dp.register_message_handler(src.server.start_command, commands=["start", "help"])
    src.server.dp.register_message_handler(src.server.show_categories, commands="categories")


if __name__ == "__main__":
    database_state()
    dispatcher_register()
    executor.start_polling(src.server.dp, skip_updates=True)
