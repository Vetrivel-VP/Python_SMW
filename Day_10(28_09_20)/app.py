def DevisionError():
    a, b = eval(input('Enter the value of a,b:'))
    try:
        c = a / b
        print(f'Ans : {a}/{b} = {c}')

    except Exception as er:
        print(f'Warning : {er}')


if __name__ == "__main__":
    DevisionError()
