from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    @abstractmethod
    def draw(self, surface):
        pass