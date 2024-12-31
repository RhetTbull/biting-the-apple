"""Create a reminder in Reminders.app

To use: `python3 -m pip install mac-pyxa` (doesn't work with Python 3.13)
"""

from datetime import datetime

import PyXA


def create_reminder(name, due_date=None):
    """Creates a new reminder in the Mac Reminders app's default list."""
    try:
        reminders_app = PyXA.Application("Reminders")
        due_date = datetime.fromisoformat(due_date) if due_date else None
        reminder = reminders_app.new_reminder(name=name, due_date=due_date)
        print(f"Reminder '{name}' created successfully.")
    except Exception as e:
        print(f"Failed to create reminder: {e}")


create_reminder("Finish HSV.py talk", due_date="2025-02-01T17:00:00")
