from math import log2 , ceil, floor
from abc import ABC, abstractmethod


class Computer(ABC):
    AV_PROCESSORS = {}

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0
        
    @property
    def manufacturer(self):
        return self.__manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
       ...

    @staticmethod
    def power_of_two(number):
        res = log2(number)
        return floor(res) == ceil(res)

    def set_parts(self, processor, ram):
        self.processor = processor
        self.ram = ram
        self.price += self.AV_PROCESSORS[processor]
        self.price += int(log2(ram)) * 100

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"