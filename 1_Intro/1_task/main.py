x = [1, 2, 3, 4, 5]


def f(y):
    for i in range(len(y)):
        if i % 2 == 0:
            print("even:", y[i])
        else:
            print("odd:", y[i])


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("hi my name is", self.name, "and I am", self.age, "years old")


def main():
    p = Person("Roma", 20)
    p.say_hi()
    f(x)
    if True:
        print("done")


if __name__ == "__main__":
    main()
