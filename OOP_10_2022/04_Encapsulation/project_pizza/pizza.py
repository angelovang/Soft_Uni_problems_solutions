from Encapsulation.project_pizza.dough import Dough
from Encapsulation.project_pizza.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")

        self.__name = value
        return self.name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError("You should add dough to the pizza")

        self.__dough = value
        return self.__dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")

        self.__toppings_capacity = value
        return self.__toppings_capacity

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0

        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        total_weight = self.dough.weight + sum(self.toppings[pz] for pz in self.toppings)
        return total_weight
