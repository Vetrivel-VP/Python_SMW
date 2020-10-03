class CompileTime:
    def add(self, a, b, c=0):
        print(f'Ans : {a+b+c}')


class FirstCLass:
    def run(self):
        print('Inside the Firstclass Run method')


class SecondCLass(FirstCLass):
    def run(self):
        print('Inside the Second Class Run Method')


class Encapsulation:
    def __init__(self):
        self.a = 50
        self.__b = 60


if __name__ == "__main__":
    o = Encapsulation()
    print(f'A : {o.a}, {o.__b}')
