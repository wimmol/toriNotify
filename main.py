import asyncio
import logging

from app.bot.dispatcher import start_bot

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        start_bot()
    except KeyboardInterrupt:
        print('Exit')
