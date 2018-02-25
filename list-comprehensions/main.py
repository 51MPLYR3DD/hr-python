#!/usr/bin/python3

# List Comprehension
# Solution to HackerRank Python challenge.

def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != n]
    
    print(arr)

if __name__ == '__main__':
    main()