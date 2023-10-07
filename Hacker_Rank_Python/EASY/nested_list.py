if __name__ == '__main__':
    records = []   
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    student_sort = sorted(set([x[1]for x in records]))
    #to get 2nd lowest grade
    student_second_lowest = student_sort[1]
    list_in_order = []
    for student in records:
        if (student_second_lowest == student[1]):
            list_in_order.append(student[0])
    for student in sorted(list_in_order):
        print(student)
        