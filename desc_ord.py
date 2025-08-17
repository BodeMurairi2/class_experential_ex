#!/usr/bin/env python3

def descending_order(num):
    i = 0
    my_list = []
    while num != 0:
        my_list.append(num % 10)
        num = int(num/10)
    for index in range(len(my_list)):
        for number in my_list:
            if my_list[i] != my_list[-1]:
                if my_list[i] < my_list[i+1]:
                    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    
    new_num = "".join(str(i) for i in my_list)
    return new_num

print(descending_order(5963782))
