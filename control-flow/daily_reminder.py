# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize the reminder message using match case
match priority:
    case "high":
        priority_text = "high priority"
    case "medium":
        priority_text = "medium priority"
    case "low":
        priority_text = "low priority"
    case _:
        priority_text = "unknown priority"

# Construct reminder based on time sensitivity
if time_bound == "yes":
    reminder = f"Reminder: '{task}' is a {priority_text} task that requires immediate attention today!"
else:
    reminder = f"Note: '{task}' is a {priority_text} task. Consider completing it when you have free time."

# Print the final reminder
print(reminder)
