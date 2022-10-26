""" Telegram Bot manager. """

import src.server
from aiogram import executor
from src.db.core import database_state


if __name__ == "__main__":
    database_state()
    executor.start_polling(src.server.dp, skip_updates=True)

# Tasks:
# 1) Interactive /last.
# 2) Aliases fix.
# 3) Add or remove category.
# 4) Add or remove aliases.
# 5) Statistics by category.
