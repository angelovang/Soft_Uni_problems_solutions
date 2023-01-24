class Player:
    def __init__(self, name:str, hp:int, mp:int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self,skill_name:str, mana_cost:int):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return f"Skill already added"

    def player_info(self):
        result = [f"Name: {self.name}",
                  f"Guild: {self.guild}",
                  f"HP: {self.hp}",
                  f"MP: {self.mp}"
                  ]

        for sk , mnc in self.skills.items():
            result.append(f"==={sk} - {mnc}\n")

        return '\n'.join(result)


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
