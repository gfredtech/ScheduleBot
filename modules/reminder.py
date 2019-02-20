import threading
import time

import schedule

from modules import lesson_controller

"""
Reminder module runs in the background for reminding users
It uses the schedule library
"""


def notify_need_remind(call_when_needed):
    """
    Adds remind times in schedule and sets given function to be called

    :param call_when_needed: function
    """
    for time_start in lesson_controller.get_reminder_times():
        schedule.every().day.at(time_start).do(call_when_needed)


def reminders_pending():
    """
    Runs in the background thread and
    wakes schedule to check if there are new reminders
    """
    while 1:
        schedule.run_pending()
        time.sleep(30)


# start reminders_pending in background thread
# daemon=True means die if main thread dies
threading.Thread(target=reminders_pending, daemon=True).start()
