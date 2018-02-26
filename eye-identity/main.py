#!/usr/bin/python3

# Eye and Identity
# Solution to HackerRank Python challenge.

import numpy as np

def main():
    user_input = input()

    n = int(user_input[0])
    m = int(user_input[2])

    print(np.eye(n, m))

if __name__ == '__main__':
    main()