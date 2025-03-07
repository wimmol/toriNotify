import logging


from app.bot.dispatcher import start_bot
from app.parser.tori_task import tori_task

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        tori_task()
        start_bot()
    except KeyboardInterrupt:
        print('Exit')
