number = input("Enter a number and I'll tell you if number is a multiple of 10 or not.")
number = int(number)


if number % 10 == 0:
    print(f"\nThe number {number} is multiple of 10.")
else:
    print(f"\nThe number is not multiple of 10.")
