from exams.project_11_12_2022.project_11_12_21.car.muscle_car import MuscleCar
from exams.project_11_12_2022.project_11_12_21.car.sports_car import SportsCar
from exams.project_11_12_2022.project_11_12_21.driver import Driver
from exams.project_11_12_2022.project_11_12_21.race import Race


class Controller:
    cars_type = ["MuscleCar", "SportsCar"]

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if model in [c.model for c in self.cars]:
            raise Exception(f"Car {model} is already created!")

        if car_type in self.cars_type:
            if car_type == "MuscleCar":
                current_car = MuscleCar(model, speed_limit)

            else:
                current_car = SportsCar(model, speed_limit)

            self.cars.append(current_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [dr.name for dr in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

        current_driver = Driver(driver_name)
        self.drivers.append(current_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in self.races:
            raise Exception("Race {name} is already created!")

        current_race = Race(race_name)
        self.races.append(current_race)
        return f"Race {race_name} is created."

    def get_last_car(self, car_type):
        for car in self.cars[::-1]:
            if car_type == type(car).__name__ and not car.is_taken:
                return car
        else:
            raise Exception(f"Car {car_type} could not be found!")

    def driver_is_exist(self, driver_name):
        for dr in self.drivers:
            if driver_name == dr.name:
                return dr
        else:
            raise Exception(f"Driver {driver_name} could not be found!")

    def add_car_to_driver(self, driver_name: str, car_type: str):
        current_driver = self.driver_is_exist(driver_name)
        current_car = self.get_last_car(car_type)
        if current_driver.car:
            old_car_model = current_driver.car
            current_driver.car = current_car
            current_car.is_taken = True
            old_car_model.is_taken = False
            return f"Driver {driver_name} changed his car from {old_car_model.model} to {current_car.model}."
        else:
            current_driver.car = current_car
            current_car.is_taken = True
            return f"Driver {driver_name} chose the car {current_car.model}."

    def race_is_exist(self, race_name):
        for race in self.races:
            if race_name == race.name:
                return race
        else:
            raise Exception(f"Race {race_name} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        current_race = self.race_is_exist(race_name)
        current_driver = self.driver_is_exist(driver_name)
        if current_driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if current_driver in current_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        current_race = self.race_is_exist(race_name)
        if len(current_race.drivers) < 3:
            raise Exception("Race {race_name} cannot start with less than 3 participants!")

        result = sorted(current_race.drivers, key=lambda x: x.car.speed_limit, reverse=True)[0:3]
        res = []
        for el in result:
            el.number_of_wins += 1
            res.append(f"Driver {el.name} wins the {race_name} race with a speed of {el.car.speed_limit}.")

        return '\n'.join(res)
