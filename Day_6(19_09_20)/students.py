def students_details(n):
    student = []
    for i in range(n):
        name = input(f'Enter the {i+1} student name:')
        m1, m2, m3, m4, m5 = eval(input(f'Enter the {i+1} student mark:'))
        total = m1+m2+m3+m4+m5
        avg = total / 5

        sl = [i+1, name, total, avg]
        student.append(sl)
        # main[single_student[1,sample1,250,50],[2,sanple2,300,55]]

    print_Details(student)


def print_Details(student):
    print('Id\t\tName\t\t\t\tTotal\t\t\tAverage')
    for i in range(len(student)):
        print("{0}\t\t{1}\t\t\t\t{2}\t\t\t{3}".format(
            student[i][0], student[i][1], student[i][2], student[i][3]))


def lists_def():
    main_list = [
        [1, 'Sample', 55, 55],
        [2, 'Sample2', 50, 56]
    ]
    print(main_list[0][1])


if __name__ == "__main__":
    #n = eval(input('Enter the number of students:'))
   # students_details(n)
    lists_def()
