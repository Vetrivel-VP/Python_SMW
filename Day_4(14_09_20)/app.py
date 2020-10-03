def my_function():
    print("This is  my first function")
    name = input('Enter your name:')
    print(f'{name} executed the function successfully')


def addition():
    """
        Addition  Function:
            Helps you to add two numberic values.
            Read the value and proccess and display the out.
    """
    a, b = eval(input('Enter the value of a,b:'))
    c = a + b
    print(f'{a} + {b} = {c}')


def printmyname(name):
    print(f'I\'m printing the function parameter name: {name}')


def add(a, b):
    return a+b, a, b


def sum_naturals(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i

    return sum


if __name__ == "__main__":
    x = eval(input('Enter the value of n:'))
    print(f'The sum of {x} natural number is : {sum_naturals(x)}')
