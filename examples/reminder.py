"""Create a reminder in Reminders.app

To use: `python3 -m pip install mac-pyxa` (doesn't work with Python 3.13)
"""

import datetime

import PyXA

reminders_app = PyXA.Application("Reminders")
reminders_app.new_reminder(
    name="Finish HSV.py talk", due_date=datetime.datetime(2025, 2, 10)
)
