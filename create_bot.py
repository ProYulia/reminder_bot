from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config as c

storage = MemoryStorage()
bot = Bot(token=c.r_token)
dp = Dispatcher(bot, storage=storage)