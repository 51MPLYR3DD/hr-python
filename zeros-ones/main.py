#!/usr/bin/python3

# Zeros and Ones
# Solution to HackerRank Python challenge.

import numpy as np

def main():
    user_input = input()
    user_input = user_input.replace(" ", "")

    arr = []
    for i in user_input:
        arr.append(int(i))

    print(np.zeros((arr), dtype = np.int))
    print(np.ones((arr), dtype = np.int))

if __name__ == '__main__':
    main()