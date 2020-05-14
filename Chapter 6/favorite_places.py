favorite_places = {
    'taneli': ['oulainen', 'kempele'],
    'pekka': ['dubai', 'pudasjarvi'],
    'hannes': ['tyrnava', 'oulu'],
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
