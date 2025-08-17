#!/usr/bin/env python3

num = 5654

num_list = str(num)
list_num = list(num_list)
sorted_list = sorted(list_num, reverse=True)
new_string = "".join(sorted_list)
num = int(new_string)
print(new_string)
