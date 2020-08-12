filename = "a_discourse_on_trade.txt"

with open(filename) as fhand:
    contents = fhand.read()
    print(f"Without a space, the number of 'the' is: {contents.count('the')}")
    print(f"Adding a space, the number of 'the' is: {contents.count('the ')}")
