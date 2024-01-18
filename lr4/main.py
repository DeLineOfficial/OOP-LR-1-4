# Программирование на языке высокого уровня (Python).
# Задание №4.3.4. Вариант 8 ( по списку 18 )
#
# Выполнил: Столяр А.М.
# Группа: ПИН-Б-З-22-1
# E-mail: artem.stolyar.2002@mail.ru


import json

class Queue:
    def __init__(self):
        self.items = [1512321312,12312312312312312,21312312312312321,3232323,11111]
        self.value = self.items

    def __str__(self):
        print(f"Человеческий вид: {self.items}")

    def is_empty(self):
        return len(self.items) == 0
    
    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.value, file)

    def load(self, filename):
        with open(filename, 'r') as file:
            self.data = json.load(file)

    def from_string(self, item):
        self.items.append(item)



filename = "data.json"
queue = Queue()

queue.from_string('hello curva')
queue.save("queue.json")
queue.load(filename)



queue.__str__()
print(f"Выгрузился и спит: {queue.data}")



