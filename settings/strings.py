from settings.config import REMIND_WHEN_LEFT_MINUTES

"""
All constant strings are stored in this file
"""

TEXT_DAYS_OF_WEEK = ("Mo", "Tu", "We", "Th", "Fr", "Sa")
TEXT_BUTTON_NOW = "NOW❗"
TEXT_BUTTON_DAY = "DAY⌛"
TEXT_BUTTON_WEEK = "WEEK 🗓️"

MESSAGE_HI = "Hi there!✋"
MESSAGE_HELP = """Class Schedule bot for GTUC students.
See your class timetable and get reminders when you have a class
Some commands, that might be useful for you:

/start - Start bot
/help - Display Help
/configure - Configure your year and course
/reminder - Set reminders"""

MESSAGE_USER_NOT_CONFIGURED = "Sorry. I do not know your course yet. 😥\n" \
                              " Please use /configure command to set it up"
MESSAGE_FREE_DAY = "No lessons on this day! You're so lucky :)"
MESSAGE_YES = "Yes 🙋"
MESSAGE_NO = "No 🙅"
MESSAGE_SETTINGS_SAVED = "Your settings have been saved successfully!"
MESSAGE_ERROR = "Sorry, I did not understand you"

REQUEST_COURSE = "What year are you in?"
REQUEST_GROUP = "What's your course?"
REQUEST_REMINDERS = f"Would you like to get reminders {REMIND_WHEN_LEFT_MINUTES} minutes " \
    "before every lecture, tutorial and lab? 🚨"
REQUEST_WEEKDAY = "Select some day of the week"

HEADER_NOW = "\n"
HEADER_NEXT = "\n"
HEADER_REMIND = "⏰\n"
HEADER_NO_NEXT_LESSONS = "                  🗽"
HEADER_SEPARATOR = "\n"
