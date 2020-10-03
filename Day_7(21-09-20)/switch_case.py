import sys


def mychoices(ch):
    mydict = {
        1: 'Addition',
        2: 'Subtraction',
        3: 'Exit'
    }

    return mydict.get(ch, 'Invalid Option')


if __name__ == "__main__":
    restart = "yes"
    while restart[0] == 'Y' or restart[0] == 'y':
        print("1. Addition\n2. Subtraction\n3. Exit\nSelect an option:")
        ch = eval(input())
        options = mychoices(ch)
        if options == 'Addition':
            a, b = eval(input('Enter the value of a,b:'))
            print(f'{a} + {b} = {a+b}')
            restart = input('Do you want to continue. Press(Yes/No):')
        elif options == 'Subtraction':
            a, b = eval(input('Enter the value of a,b:'))
            print(f'{a} - {b} = {a-b}')
            restart = input('Do you want to continue. Press(Yes/No):')
        elif options == 'Exit':
            sys.exit()
        else:
            print(options)
            restart = input('Do you want to continue. Press(Yes/No):')
