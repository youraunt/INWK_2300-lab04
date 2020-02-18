# Notes from class on February 18, 2020


def greet(name):
    print("This is the greet function!")
    print("Nice to meet your,", name)


def main():
    print("This is the main function!")


def f(x):
    return 2 ** x + 4


def my_fun():
    print("inside my_fun")
    print("When does this print")


def my_fun_1():
    print("inside my_fun_1")
    print("when does this print_1")


def hello(name):
    sentence = 'Hello, ' + name + '!'
    print(sentence)


def add_em(x, y):
    result = x + y
    return result


if __name__ == '__main__':
    main()
    greet('Brice')
    print(f(3))
    my_fun()
    my_fun_1()
    hello('Brice')
    # can pass any type of variable
    print(add_em(99, 99))
    print(add_em("hello", "guys"))
