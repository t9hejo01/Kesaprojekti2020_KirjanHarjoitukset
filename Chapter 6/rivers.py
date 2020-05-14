rivers = {'nile': 'Egypt',
          'rhine': 'Germany',
          'danube': 'Hungary'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")
    
for river in rivers.keys():
    print(f"\n{river.title()}")

for country in rivers.values():
    print(f"\n{country.title()}")
    
