from datetime import datetime

# Ask for name
name = input("What is your name? ")
# Ask for age and ensure it's a number
age = int(input("How old are you? "))
try:
    age = int(age_input = input("How old are you? "))
except ValueError:
    print("That's not a number!")
    exit()

# Get the current year
current_year = datetime.now().year

# Calculate year they turn 100
year_when_100 = current_year + (100 - age)

# Print the message
print(f"Hi {name}! You’ll turn 100 years old in the year {year_when_100}.")