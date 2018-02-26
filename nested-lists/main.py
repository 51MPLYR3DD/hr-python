#!/usr/bin/python3

# Nested Lists
# Solution to HackerRank Python challenge.

def main():
    class_list = []
    for _ in range(int(input())):
        name = str(input())
        score = float(input())
        class_list.append([name, score])

    class_list.sort(key = lambda student: (student[1], student[0]))

    second_lowest= [student[1] for student in class_list if student[1] != class_list[0][1]][0]
    for name in [student for student in class_list if student[1] == second_lowest]:
        print(name[0])

if __name__ == '__main__':
    main()