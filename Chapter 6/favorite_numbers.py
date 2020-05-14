favorite_numbers = {'jari': ['10','22'],
                    'taneli': [ '6', '31'],
                    'juhana': ['60', '24'],
                    'aleksi': ['16', '26'],
                    'henri': ['29', '30'],
                    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number.title()}")
