name = input('Enter the name:')
m1, m2, m3, m4, m5 = eval(input('Enter the students mark:'))
total = m1+m2+m3+m4+m5
avg = total/5
if avg >= 45 and avg <= 55:
    grade = 'C grade'
elif avg >= 56 and avg <= 65:
    grade = 'B Grade'
elif avg >= 66 and avg <= 75:
    grade = 'A Grade'
elif avg >= 76 and avg <= 100:
    grade = 'A+'
else:
    grade = 'Fail'


print(f'Name: {name} Total: {total} Average:{avg}% Grade: {grade}')
