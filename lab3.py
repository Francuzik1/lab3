#элементами очереди: поиск, добавление, удаление
class Queue:
    def __init__(self, tester=[]):
        self.tester = tester

    def adder(self, what_add):
        for i in what_add:
            self.tester.append(i)

    def pops(self):
        self.tester.pop()

    def printer(self):
        return self.tester

    def searcher_index(self, ind):
        return self.tester[ind]

    def searcher_value(self, value):
        r = 0
        while self.tester[r] != self.tester[-1]:
            r += 1
        if self.tester[r] == value:
            print("В очереди под номером : ", r+1)
        if self.tester[r] != self.tester[-1]:
            print("В очереди под номером : ", r + 1)
        print("Finish")


deter = Queue()
deter.adder([1, 2, 3, 4, 5])
print(deter.printer())
deter.searcher_value(5)
deter.searcher_value(6)
