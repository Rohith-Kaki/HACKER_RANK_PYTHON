if __name__ == '__main__':
    n = int(input())  #takes input
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
sum = 0
for x in student_marks[query_name]:
        sum += x
sum = sum / 3
print(f"{sum:.2f}")

