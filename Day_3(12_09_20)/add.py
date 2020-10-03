restart = "yes"
while restart[0] == "y" or restart[0] == "Y":
    a, b = eval(input('Enter the value of a,b:'))
    c = a + b
    print(f'The sum : {a} + {b} = {c}')
    restart = input('Do you want to continue. Press(Yes/No)')
