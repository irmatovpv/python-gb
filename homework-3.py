class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())

position = Position('Иван', 'Иванов', 'Разработчик', 10000, 2000)
print(position.get_full_name())
print(position.get_total_income())

print(position.name)
print(position.surname)
print(position.position)
print(position._income)