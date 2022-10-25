from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class AccessMiddleware(BaseMiddleware):
    def __init__(self, access_id):
        super().__init__()
        self.access_id = access_id

    async def on_process_message(self, message, _):
        if int(message.from_user.id) != int(self.access_id):
            await message.answer("Access denied.")
            raise CancelHandler()
