class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []
        self.count = 0

    def add_item(self, item: str):
        if self.__capacity > self.count:
            self.items.append(item)
            self.count += 1
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - self.count}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
