#!/usr/bin/env python3

def persistance(n):
    """Finding persistance"""
    count = 0
    new_string = str(n)

    while len(new_string)!=1:
        product = 1
        for i in new_string:
            product *= int(i)
        new_string = str(product)
        count+=1

    print(f"Number of time to reach one digit: {count}")
    print(f"One digit {new_string}")

persistance(n=999)
