from abc import abstractmethod


class Clothes:
    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, name, V):
        super().__init__(name)
        self._V = V

    @property
    def fabric_consumption(self):
        return self._V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, H):
        super().__init__(name)
        self._H = H

    @property
    def fabric_consumption(self):
        return 2 * self._H + 0.3

class Warehouse:
    def __init__(self, items):
        self._items = items

    @property
    def consumption(self):
        return sum([i.fabric_consumption for i in self._items])

warehouse = Warehouse([Coat("Холод", 4), Coat("Жара", 4)])
print(warehouse.consumption)