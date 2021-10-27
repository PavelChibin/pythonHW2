my_list = [True, False, complex(5, 7), 5, 7.7, oct(123), bin(45), hex(456), range(99), {34, 11}]
for i, item in enumerate(my_list, 1):
    print(f"{1} {item} - {type(item)}")
    