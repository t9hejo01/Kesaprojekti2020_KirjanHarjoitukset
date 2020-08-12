sandwich_orders = ['tuna', 'pastrami', 'chicken teriyaki','pastrami', 'cheese', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')



while sandwich_orders:
    ready_sandwich = sandwich_orders.pop()


    print(f"I made your {ready_sandwich.lower()} sandwich.")
    finished_sandwiches.append(ready_sandwich)

print("\nThe following sandwiches have been made.")
for ready_sandwich in finished_sandwiches:
    print(ready_sandwich.title())
