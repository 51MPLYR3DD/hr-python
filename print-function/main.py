#!/usr/bin/python3

# Print Function
# Solution to HackerRank Python challenge.

def main():
    n = int(input())
    print(*range(1, n + 1), sep="")

if __name__ == '__main__':
    main()