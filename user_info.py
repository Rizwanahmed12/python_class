# User input section
name = input("Enter Your Name: ")
city = input("Enter Your City: ")
age = int(input("How Old Are You: "))
siblings = input("How many siblings do you have? ")
best_friend = input("Who is your best friend? ")
location = input("Your current location: ")
qualification = input("Your qualification: ")
occupation = input("Your occupation: ")
cnic_number = input("Enter your CNIC number: ")
nationality = input("Your nationality: ")
mobile_number = input("Enter your mobile number: ")
religion = input("Your religion: ")
hobbies = input("Your hobbies: ")
favourite_character = input("Your favourite character: ")
language = input("Languages you speak: ")
height = input("Your height (e.g., 5'8\"): ")
weight = input("Your weight (in kg): ")
gender = input("Your gender: ")

# Demonstration of variable swap
a = 200
b = ["500", "1000", "1200"]

# Swap values
a, b = b, a

# Output section
print("\n--- Data Summary ---\n")
print(f"My Name Is {name}.")
print(f"I am from {city}.")
print(f"I am {age} years old.")
print(f"I have {siblings} sibling(s).")
print(f"My best friend is {best_friend}.")
print(f"I currently live in {location}.")
print(f"My qualification is {qualification}.")
print(f"I work as a(n) {occupation}.")
print(f"My CNIC number is {cnic_number}.")
print(f"I am a citizen of {nationality}.")
print(f"My mobile number is {mobile_number}.")
print(f"My religion is {religion}.")
print(f"My hobbies include {hobbies}.")
print(f"My favourite character is {favourite_character}.")
print(f"I can speak {language}.")
print(f"My height is {height}.")
print(f"My weight is {weight} kg.")
print(f"My gender is {gender}.")

# Show results of the swap
print("\n--- Variable Swap Results ---")
print(f"Length of list 'a': {len(a)}")  # a is now the list
print(f"Type of variable 'b': {type(b)}")  # b is now an integer