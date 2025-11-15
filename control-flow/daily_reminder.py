
# daily_reminder.py

task = input("Enter your task for today: ").strip()
priority = input("Enter the task priority (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        reminder = f"Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Your task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task '{task}' is LOW priority."
    case _:
        reminder = f"Your task '{task}' has an unknown priority level."

if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

print(reminder)
