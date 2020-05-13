ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ord_num in ordinal_numbers:
    if ord_num < 2:
        print(str(ord_num) + "st")
    elif ord_num < 3:
        print(str(ord_num) + "nd")
    elif ord_num < 4:
        print(str(ord_num) + "rd")
    else:
        print(str(ord_num) + "th")
