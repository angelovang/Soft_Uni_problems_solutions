from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def is_delicacy_exist(self, name):
        for d in self.delicacies:
            if d.name == name:
                return d

    def is_booth_exist(self, booth_number):
        for b in self.booths:
            if b.booth_number == booth_number :
                return b

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        current_dd = self.is_delicacy_exist(name)
        if current_dd:
            raise Exception(f"{name} already exists!")

        if type_delicacy == "Gingerbread":
            current_d = Gingerbread(name, price)

        elif type_delicacy == "Stolen":
            current_d = Stolen(name, price)

        else:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(current_d)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == "Open Booth":
            current_b = OpenBooth(booth_number, capacity)

        elif type_booth == "Private Booth":
            current_b = PrivateBooth(booth_number, capacity)

        else:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(current_b)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        current_b = 0
        for b in self.booths:
            if not b.is_reserved and number_of_people <= b.capacity :
                b.reserve(number_of_people)
                return f"Booth {b.booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        current_b = self.is_booth_exist(booth_number)
        if not current_b:
            raise Exception(f"Could not find booth {booth_number}!")

        current_d = self.is_delicacy_exist(delicacy_name)
        if not current_d:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_b.delicacy_orders.append(current_d)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def get_sum_of_orders(self,current_booth):
        return sum([d.price for d in current_booth.delicacy_orders])

    def leave_booth(self, booth_number: int):
        current_b = self.is_booth_exist(booth_number)
        bill = 0
        bill += current_b.price_for_reservation + self.get_sum_of_orders(current_b)
        self.income += bill
        current_b.remove_orders()
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
