class Date:
    def __init__(self, date_string):
        self.__date_string = date_string
        self.day, self.month, self.year = self.parse(date_string)

    @classmethod
    def parse(cls, date):
        day, month, year = date.split('-')
        day, month, year = int(day), int(month), int(year)
        cls.assert_valid(day, month, year)
        return day, month, year

    @staticmethod
    def assert_valid(day, month, year):
        assert  0 < month <= 12
        if month in [1, 3, 5, 7, 8, 10, 12]:
            assert 0 < day <= 31
        if month in [4, 6, 9, 11]:
            assert 0 < day <= 30
        if month  == 2:
            if year % 4 == 0:
                assert 0 < day <= 29
            else:
                assert 0 < day <= 28


date = Date("01-12-1985")
print(date.day, date.month, date.year)

date = Date("32-12-1985")