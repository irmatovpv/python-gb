class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

        self.deep = 5
        self.weight_asfalt = 25

    def weight(self):
        return  self._length * self._width * self.deep * self.weight_asfalt

print(Road(5000, 20).weight())