import json

filename = "favorite_number.json"

with open(filename, 'a') as fhand:
    number = json.load(fhand)
    print(f"I know your favorite number! It's {number}.")
