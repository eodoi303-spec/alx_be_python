from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return it for later use if needed

def calculate_future_date(current_date, days_to_add):
    """
    Calculates the future date after adding a specified number of days.
    
    Parameters:
        current_date (datetime): The starting date.
        days_to_add (int): Number of days to add.
    
    Returns:
        datetime: The future date.
    """
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Prompt for number of days to add and calculate future date
    while True:
        try:
            days_input = input("Enter the number of days to add to the current date: ").strip()
            days_to_add = int(days_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer value for days.")
    
    calculate_future_date(current_date, days_to_add)

if __name__ == "__main__":
    main()
