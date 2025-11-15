task = input("Enter your task for today: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Begin generating the reminder
print("\n--- Daily Reminder ---")

# Use match case to handle priority levels
match priority:
    case "high":
        reminder = f"Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Your task '{task}' is of medium priority."
    case "low":
        reminder = f"Your task '{task}' is low priority."
    case _:
        reminder = f"Your task '{task}' has an unknown priority level."

# Add time sensitivity using if
if time_bound == "yes":
    reminder += " This task is time-bound and requires immediate attention today!"
else:
    reminder += " It is not time-sensitive."

# Print the final customized reminder
print(reminder)
