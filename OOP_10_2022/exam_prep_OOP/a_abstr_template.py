from abc import ABC, abstractmethod


class Movie(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise Exception("abcd")
        self.__name = value


    @abstractmethod
    def details(self):
        ...