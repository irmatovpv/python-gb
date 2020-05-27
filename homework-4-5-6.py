class NoSuchItemInWarehouse(Exception):
    pass
class NotEnoughItemInWarehouse(Exception):
    pass

class OfficeEquipment:
    def __init__(self, vendor, name):
        self.vendor = vendor
        self.name = name

    def print_specs(self):
        print(self.vendor)
        print(self.name)

class Printer(OfficeEquipment):
    def __init__(self, vendor, name, ppm):
        super().__init__(vendor, name)
        self.ppm = ppm

    def print_specs(self):
        print(self.vendor)
        print(self.name)
        print(self.ppm)


class Scaner(OfficeEquipment):
    def __init__(self, vendor, name, resolution):
        super().__init__(vendor, name)
        self.resolution = resolution

    def print_specs(self):
        print(self.vendor)
        print(self.name)
        print(self.resolution)


class Xerox(OfficeEquipment):
    def __init__(self, vendor, name, one_page_cost):
        super().__init__(vendor, name)
        self.one_page_cost = one_page_cost

    def print_specs(self):
        print(self.vendor)
        print(self.name)
        print(self.one_page_cost)


class Warehouse:
    def __init__(self):
        self.items = {}

    def add(self, item, amount):
        assert isinstance(amount, int)

        if not isinstance(item, OfficeEquipment):
            raise ValueError
        self.items[item] = amount

    def extract(self, item, amount):
        assert isinstance(amount, int)

        if self.items.get(item, None) is None:
            raise NoSuchItemInWarehouse()
        if self.items.get(item, None) < amount:
            raise NotEnoughItemInWarehouse()
    def print_stock(self):
        for item, amount in self.items.items():
            print()
            item.print_specs()
            print(amount)

w = Warehouse()
w.add(Xerox("Xerox", '5c', 1), 5)
w.add(Scaner("Scaner", 'Scaner', 3), 2)
w.add(Xerox("Printer", '5c', 1), 50)
w.print_stock()

w.add(Xerox("Printer", '5c', 1), "50")