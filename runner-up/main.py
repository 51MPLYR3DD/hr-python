#!/usr/bin/python3

# Find the Runner-Up Score!
# Solution to HackerRank Python challenge.

def main():
    n = int(input())
    arr = map(int, input().split())
    scores = []
    for i in arr:
        scores.append(i)
        
    upper = max(scores)
    for i in scores:
        while max(scores) == upper:
            scores.remove(max(scores))
            
    scores.sort()    
    print(scores[-1])

if __name__ == '__main__':
    main()