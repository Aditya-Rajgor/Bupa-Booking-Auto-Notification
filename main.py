from botBupa import BotBupa
import time

if __name__ == '__main__':
    while True:
        bupa_bot = BotBupa("https://bmvs.onlineappointmentscheduling.net.au/oasis/", "No available slot")
        bupa_bot.check_slot_by_time()
        #time.sleep(20)


