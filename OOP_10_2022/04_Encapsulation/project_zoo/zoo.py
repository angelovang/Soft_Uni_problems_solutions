from Encapsulation.project_zoo.animal import Animal
from Encapsulation.project_zoo.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker:Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name:str):
        try:
            worker_to_fire = next(filter(lambda w: w.name == worker_name , self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker_to_fire)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        sum_of_salaries = sum(w.salary for w in self.workers)
        if self.__budget < sum_of_salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum_of_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"


    def tend_animals(self):
        sum_to_care = sum(anml.money_for_care for anml in self.animals)
        if self.__budget < sum_to_care:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= sum_to_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        sorted_animals = {
            "Lions" : [],
            "Tigers": [],
            "Cheetahs": [],
        }
        for anml in self.animals:
            if anml.__class__.__name__ == "Lion" :
                sorted_animals["Lions"].append(anml)

            elif anml.__class__.__name__ == "Tiger" :
                sorted_animals["Tigers"].append(anml)

            elif anml.__class__.__name__ == "Cheetah" :
                sorted_animals["Cheetahs"].append(anml)

        result = [f"You have {len(self.animals)} animals"]
        for k , v  in sorted_animals.items():
            result.append(f"----- {len(sorted_animals[k])} {k}:")
            for x in v:
                result.append(str(x))

        return '\n'.join(result)

    def workers_status(self):
        sorted_workers = {
            "Keepers" : [],
            "Caretakers": [],
            "Vets": [],
        }
        for wrk in self.workers:
            if wrk.__class__.__name__ == "Keeper" :
                sorted_workers["Keepers"].append(wrk)

            elif wrk.__class__.__name__ == "Caretaker" :
                sorted_workers["Caretakers"].append(wrk)

            elif wrk.__class__.__name__ == "Vet" :
                sorted_workers["Vets"].append(wrk)

        result = [f"You have {len(self.workers)} workers"]
        for k , v  in sorted_workers.items():
            result.append(f"----- {len(sorted_workers[k])} {k}:")
            for x in v:
                result.append(str(x))

        return '\n'.join(result)








