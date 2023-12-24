from datetime import date, timedelta

def count_sundays_since_birth(birth_date):
    current_date = date.today()
    birth_date = date(*map(int, birth_date.split('-')))
    days_lived = (current_date - birth_date).days

    sundays_count = 0
    for day in range(days_lived + 1):
        current_day = birth_date + timedelta(days=day)
        if current_day.weekday() == 6:  # Sunday is represented by 6 in the weekday() function
            sundays_count += 1

    return sundays_count

# Example usage:
birth_date_input = input("Enter your birth date in YYYY-MM-DD format: ")
sundays_count = count_sundays_since_birth(birth_date_input)
print(f"You have lived through {sundays_count} Sundays since your birth date.")