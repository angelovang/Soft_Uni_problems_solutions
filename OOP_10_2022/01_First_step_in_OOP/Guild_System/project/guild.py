from Inheritance.Need_for_Speed.project import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        else:
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            else:
                return f"Player {player.name} is in another guild."

    def kick_player(self,player_name: str):
        for element in self.players :
            if player_name == element.name:
                element.guild = "Unaffiliated"
                self.players.remove(element)
                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."


    def guild_info(self):
        result = [f"Guild: {self.name}"]
        for pl in self.players:
            result.append(pl.player_info())
        return '\n'.join(result)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
print(guild.kick_player("George"))