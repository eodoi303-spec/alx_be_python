# daily_reminder.py

# Prompt the user for task details and clean input
task = input("Enter your task for today:").strip()
priority = input("Enter the task priority (high/medium/low):").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Determine reminder based on priority
if priority == "high":
    reminder = f"Your task '{task}' is HIGH priority."
elif priority == "medium":
    reminder = f"Your task '{task}' is MEDIUM priority."
elif priority == "low":
    reminder = f"Your task '{task}' is LOW priority."
else:
    reminder = f"Your task '{task}' has an unknown priority level."

# Add time-sensitive message if applicable
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the final reminder
print(reminder)
