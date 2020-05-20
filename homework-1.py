import time


class TrafficLight:
    __state_switch = [
        (None, 'red'),
        ('red', 'yellow'),
        ('yellow', 'green')
    ]
    def __init__(self):
        self.___color = None

    @property
    def __color(self):
        return self.___color

    @__color.setter
    def __color(self, color):
        if (self.___color, color) not in self.__state_switch:
            raise ValueError
        self.___color = color
        print(self.___color)

    def running(self):
        switch = {
            'red': 7,
            'yellow': 2,
            'green': 1,
        }
        for color, sec in switch.items():
            self.__color = color
            time.sleep(sec)

    def wrong_running(self):
        switch = {
            'red': 7,
            'green': 1,
            'yellow': 2,
        }
        for color, sec in switch.items():
            self.__color = color
            time.sleep(sec)

tl = TrafficLight()
tl.running()

tl = TrafficLight()
tl.wrong_running()