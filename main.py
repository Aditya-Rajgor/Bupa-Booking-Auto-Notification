from botBupa import BotBupa
import time
from datetime import datetime
import pytz

if __name__ == '__main__':

    while True:
        current_time = datetime.now(pytz.timezone('Australia/Melbourne'))
        print("Melbourne time: ", current_time)
        print("Bupa visa application availibility checking")
        bupa_bot = BotBupa("https://bmvs.onlineappointmentscheduling.net.au/oasis/")
        bupa_bot.check_slot_by_time()
        print("Sleeping for 5 min")
        time.sleep(60*15)