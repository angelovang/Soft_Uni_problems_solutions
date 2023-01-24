from exams.project_10_04_2022.project_10_04_22.player import Player
from exams.project_10_04_2022.project_10_04_22.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        current_pl_list = []
        for pl in players:
            if pl not in self.players:
                self.players.append(pl)
                current_pl_list.append(pl.name)
        return f"Successfully added: {', '.join(current_pl_list)}"

    def add_supply(self, *supply : Supply):
        for spl in supply:
            self.supplies.append(spl)

    def find_player(self,player_name):
        for pl in self.players:
            if player_name == pl.name:
                return pl

    def __take_last_supply(self,supply_type):
        for i in range(len(self.supplies)-1,0,-1):
            if supply_type == type(self.supplies[i]).__name__ :
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def sustain(self, player_name: str, sustenance_type: str):
        current_pl = self.find_player(player_name)

#        if current_pl.stamina == "100" :
        if not current_pl.need_sustenance:
            return f"{player_name} have enough stamina."

        current_spl = self.__take_last_supply(sustenance_type)
        if current_spl:
            current_pl.sustain_pl(current_spl.energy)
            return f"{player_name} sustained successfully with {current_spl.name}."

    @staticmethod
    def find_winner(pl1,pl2):
        pl2.stamina -= pl1.stamina/2

        pl1.stamina -= pl2.stamina/2
        if pl1.stamina <= 0:
            pl1.stamina = 0

        if pl2 < pl1:
            return f"Winner: {pl1.name}"
        else:
            return f"Winner: {pl2.name}"

    @staticmethod
    def check_stamina(*players):
        result = []
        for pl in players:
            if pl.stamina == 0:
                result.append(F"Player {pl.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    def duel(self, first_player_name: str, second_player_name: str):
        first_pl = self.find_player(first_player_name)
        second_pl = self.find_player(second_player_name)

        zero_stamina = self.check_stamina(first_pl, second_pl)
        if zero_stamina:
            return zero_stamina

        if first_pl < second_pl:
            return self.find_winner(first_pl, second_pl)
        else:
            return self.find_winner(second_pl, first_pl)

    def next_day(self):
        for pl in self.players:
            pl.stamina -= pl.age*2
            if pl.stamina <= 0:
                pl.stamina = 0

        for pl in self.players:
            self.sustain(pl.name,"Food")
            self.sustain(pl.name,"Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(player.__str__())
        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)


# pl1 = Player('a',20,100)
# pl2 = Player('b',22,80)

# s1 = Drink("K",10)
# s2 = Food("L",20)

# cont = Controller()
# cont.add_supply((s1,s2))
# cont.add_player((pl1,pl2))

# print(cont)