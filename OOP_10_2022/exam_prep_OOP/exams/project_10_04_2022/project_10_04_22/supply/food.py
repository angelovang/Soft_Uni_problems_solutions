from exams.project_10_04_2022.project_10_04_22.supply.supply import Supply


class Food(Supply):
    def __init__(self, name, energy=25):
        super().__init__(name, energy)

    def details(self):
        return f"Food: {self.name}, {self.energy}"
