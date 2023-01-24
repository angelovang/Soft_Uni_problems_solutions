from exams.project_23_08_2021.project_23_08_21.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 50)

    def breathe(self):
        self.oxygen -= 10
