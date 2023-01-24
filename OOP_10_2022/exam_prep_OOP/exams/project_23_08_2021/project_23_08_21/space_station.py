from exams.project_23_08_2021.project_23_08_21.astronaut.astronaut_repository import AstronautRepository
from exams.project_23_08_2021.project_23_08_21.astronaut.biologist import Biologist
from exams.project_23_08_2021.project_23_08_21.astronaut.geodesist import Geodesist
from exams.project_23_08_2021.project_23_08_21.astronaut.meteorologist import Meteorologist
from exams.project_23_08_2021.project_23_08_21.planet.planet import Planet
from exams.project_23_08_2021.project_23_08_21.planet.planet_repository import PlanetRepository


class SpaceStation:
    ok_missions = 0
    not_ok_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        current_astr = self.astronaut_repository.find_by_name(name)
        if current_astr:
            return f"{name} is already added."

        if astronaut_type == "Biologist":
            current_astr = Biologist(name)

        elif astronaut_type == "Geodesist":
            current_astr = Geodesist(name)

        elif astronaut_type == "Meteorologist":
            current_astr = Meteorologist(name)

        else:
            raise Exception("Astronaut type is not valid!")

        self.astronaut_repository.add(current_astr)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        curr_pl = self.planet_repository.find_by_name(name)
        if curr_pl:
            return f"{name} is already added."

        curr_pl = Planet(name)
        curr_pl.items.extend(items.split(', '))
        self.planet_repository.add(curr_pl)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        curr_astr = self.astronaut_repository.find_by_name(name)
        if not curr_astr:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(curr_astr)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astr in self.astronaut_repository.astronauts:
            astr.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        pl = self.planet_repository.find_by_name(planet_name)
        if not pl:
            raise Exception("Invalid planet name!")

        tim = self.astronaut_repository.choose_astr
        count_astr = 0
        for astr in tim:
            if len(pl.items) == 0:
                break

            while astr.oxygen > 0:
                astr.backpack.append(pl.items.pop())
                astr.breathe()
                if len(pl.items) == 0:
                    break
            count_astr += 1

        if len(pl.items) == 0:
            self.ok_missions += 1
            return f"Planet: {planet_name} was explored. {count_astr} astronauts participated in collecting items."
        else:
            self.not_ok_missions += 1
            return "Mission is not completed."

    def report(self):
        result = [
            f"{self.ok_missions} successful missions!",
            f"{self.not_ok_missions} missions were not completed!",
            "Astronauts' info:"
        ]
        for astr in self.astronaut_repository.astronauts:
            result.append(
                f"Name: {astr.name}\nOxygen: {astr.oxygen}\nBackpack items: {', '.join(astr.backpack) if len(astr.backpack) != 0 else 'none'}")

        return '\n'.join(result)
