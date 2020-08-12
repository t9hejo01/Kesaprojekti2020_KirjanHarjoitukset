number = input("How many people are in your dinner group? ")
number = int(number)


if number >= 8:
    print(f"\nYou'll have to wait for a table.")
else:
    print(f"\nYour table is ready.")
