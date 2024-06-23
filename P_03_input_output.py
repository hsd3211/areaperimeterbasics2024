# ask user for their name

username = input("what is your name? ")

# ask the user for their favourite number

fav_integer = int(input("what is your favourite number? "))

# double, halve, and square the user's favourite number

double = fav_integer * 2
half = fav_integer / 2
square = fav_integer * fav_integer

# greet the user

print(f"\nGreetings {username}, your favourite number is {fav_integer}!")

# output the results of doubling, halving and squaring their favourite integer

print(f"your favourite number doubled is {double}!")
print(f"your favourite number halved is {half}!")
print(f"your favourite number squared is {square}!")

print()

print("have a nice day")