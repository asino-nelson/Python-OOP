class Player:
    def __init__(
                self, 
                firstName: str, 
                lastName: str,
                height:float, 
                age: int, 
                team:str, 
                PPG:float, 
                APG:float, 
                health:float,
                contract
            ):
        self.firstName = firstName
        self.lastName = lastName
        self.height = height
        self.age = age
        self.team = team
        self.PPG = PPG
        self.APG = APG
        self.health = health
        self.contract = contract

    def situation(self):
        if self.health < 40:
            print(f"{self.firstName} is benched")
        else:
            print(f"{self.firstName} is in the starting 5 lineup")

class Contract:
    def __init__(self, duration: int, amount_signed: int):
        self.duration = duration
        self.amount_signed = amount_signed

contract1 = Contract(3, 250000000)
contract2 = Contract(5, 550000000)
contract3 = Contract(5, 3000000)


player1 = Player("Nelson", "Asino", 6.0, 22, "Phoenix Suns", 50, 12, 88, contract1)
print(f"{player1.firstName} {player1.lastName}, Height:{player1.height}, Age:{player1.age}, Team:{player1.team} ")
player1.situation()
print(player1.contract.amount_signed)
print("")

player2 = Player("Kevin", "Durant", 6.11, 35, "Phoenix Suns", 70, 12, 94, contract2)
print(f"{player2.firstName} {player2.lastName}, Height:{player2.height}, Age:{player2.age}, Team:{player2.team} ")
player2.situation()
print(player2.contract.amount_signed)
print("")


player3 = Player("Josh", "Christopher", 6.4, 24, "Miami Heat", 3.2, 0.7, 18, contract3)
print(f"{player3.firstName} {player3.lastName}, Height:{player3.height}, Age:{player3.age}, Team:{player3.team}")
player3.situation()
print(player3.contract.amount_signed)





        