from datetime import datetime

def calculate_age(birth_date):
   
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    current_date = datetime.now()

    days_difference = (current_date - birth_date).days

    years = days_difference // 365
    remaining_days = days_difference % 365
    months = remaining_days // 30
    days = remaining_days % 30

    return years, months, days

if __name__ == "__main__":
    birth_date_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        years, months, days = calculate_age(birth_date_input)
        print(f"Your age is {years} years, {months} months, and {days} days.")
    except ValueError:
        print("Please enter the date in the correct format (YYYY-MM-DD).")
