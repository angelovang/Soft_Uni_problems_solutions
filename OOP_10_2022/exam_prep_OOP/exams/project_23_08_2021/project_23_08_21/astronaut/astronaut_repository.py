from exams.project_23_08_2021.project_23_08_21.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astr in self.astronauts :
            if name == astr.name:
                return astr

    @property
    def choose_astr(self):
        choosen_astr = []
        for astr in self.astronauts:
            if astr.oxygen > 30:
                choosen_astr.append(astr)
                if len(choosen_astr) == 5:
                    break
        else:
            raise Exception("You need at least one astronaut to explore the planet!")

        return sorted(choosen_astr, key=lambda x: -x.oxygen)




