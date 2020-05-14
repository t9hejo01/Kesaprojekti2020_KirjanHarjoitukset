cities = {
    'helsinki': {
            'country': 'finland',
            'population': '655281',
            'fact': 'Capital of Finland',
            },

          'london': {
              'country': 'great britain',
              'population': '8308369',
              'fact': 'Capital of Great Britain',
            },
           'berlin': {
               'country': 'germany',
               'population': '3574830',
               'fact': 'Capital of Germany',
               },
           }

for city, city_info in cities.items():
    print(f"\nCity: {city}")
    full_info = f"{city_info['country']} {city_info['population']}"
    fact = city_info['fact']


    print(f"\tFull info: {full_info.title()}")
    print(f"\tFact: {fact}")
