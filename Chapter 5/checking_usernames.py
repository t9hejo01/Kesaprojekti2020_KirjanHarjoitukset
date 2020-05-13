current_users = ['admin', 'jaden', 'magical',
                 'drippin', 'essence']

new_users =['drippin', 'essence', 'dev1ce',
            'jamppi', 'xseven']
for username in new_users:
    if username in current_users:
        print("The person need to enter a new username.")
    else:
        print("The username is available.")
