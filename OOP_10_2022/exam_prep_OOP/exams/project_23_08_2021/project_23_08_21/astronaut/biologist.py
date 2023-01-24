from exams.project_23_08_2021.project_23_08_21.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name):
        super().__init__(name , 70)

    def breathe(self):
        self.oxygen -= 5
