from exams.project_10_04_2022.project_10_04_22.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name):
        super().__init__(name, 15)

    def details(self):
        return f"Drink: {self.name}, {self.energy}"

