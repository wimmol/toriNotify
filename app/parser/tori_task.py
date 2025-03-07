import time
import schedule

async def job():
    print('test blya')

def tori_task():
    schedule.every(1).minute.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)