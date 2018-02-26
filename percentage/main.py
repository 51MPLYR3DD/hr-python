#!/usr/bin/python3

# Finding the Percentage
# Solution to HackerRank Python challenge.

def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for student in student_marks:
        if query_name == student:
            sum = float()
            for grade in student_marks[student]:
                sum += grade
                avg = sum / len(student_marks[student])
            print("%.2f" % avg)

if __name__ == '__main__':
    main()