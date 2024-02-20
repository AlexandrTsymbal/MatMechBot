from os import getenv
from aiogram import Dispatcher


def get_token():
    token = getenv("BOT_TOKEN_FIRST")
    return token


def get_dispatcher():
    dp = Dispatcher()
    return dp
