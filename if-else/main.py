#!/usr/bin/python3

# If-Else
# Simple comparison based decision program.

def main():
    n = int(input())
    while n < 1 or n > 100:
        print("Invaid entry, please try again.")

    if n % 2 != 0:
        print("Weird")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")

if __name__ == '__main__':
    main()