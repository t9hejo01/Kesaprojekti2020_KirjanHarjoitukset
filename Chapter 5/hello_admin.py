usernames = ['admin', 'jaden', 'magical',
             'drippin', 'essence']
if usernames:
    for name in usernames:
        if name == 'admin':
            print("Hello admin, wolud you like to see status report?")
        if name == 'jaden':
            print(f"\nHello {name.title()}, thank you for logging again.")
        if name == 'magical':
            print(f"\nHello {name.title()}, thank you for logging again.")
        if name == 'drippin':
            print(f"\nHello {name.title()}, thank you for logging again.")
        if name == 'essence':
            print(f"\nHello {name.title()}, thank you for logging again.")

else:
    print("We need to find some users!")
