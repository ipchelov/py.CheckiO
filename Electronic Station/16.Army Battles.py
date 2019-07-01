class Warrior(object):
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Army(object):
    def __init__(self):
        self.soldiers = []

    def add_units(self, soldier_to_add, soldier_to_add_amount):
        if soldier_to_add == Warrior:
            for i in range(soldier_to_add_amount):
                self.soldiers.append(Warrior())
        elif soldier_to_add == Knight:
            for i in range(soldier_to_add_amount):
                self.soldiers.append(Knight())

    def __len__(self):
        return len(self.soldiers)


class Battle(object):
    def __init__(object):
        pass

    def fight(self, army1, army2):
        while len(army1) > 0 and len(army2) > 0:
            is_soldier1_won = fight(army1.soldiers[0], army2.soldiers[0])
            if is_soldier1_won:
                army2.soldiers.pop(0)
            else:
                army1.soldiers.pop(0)

        if len(army1) > 0:
            return True
        else:
            return False


def fight(unit_1, unit_2):
   while True:
       unit_2.health-=unit_1.attack
       if not unit_2.is_alive:
           break
       unit_1.health-=unit_2.attack
       if not unit_1.is_alive:
           break
   if unit_1.is_alive:
       return True
   else:
       return False

if __name__ == '__main__':
        # These "asserts" using only for self-checking and not necessary for auto-testing

        # fight tests
        chuck = Warrior()
        bruce = Warrior()
        carl = Knight()
        dave = Warrior()
        mark = Warrior()

        assert fight(chuck, bruce) == True
        assert fight(dave, carl) == False
        assert chuck.is_alive == True
        assert bruce.is_alive == False
        assert carl.is_alive == True
        assert dave.is_alive == False
        assert fight(carl, mark) == False
        assert carl.is_alive == False

        # battle tests
        my_army = Army()
        my_army.add_units(Knight, 3)

        enemy_army = Army()
        enemy_army.add_units(Warrior, 3)

        army_3 = Army()
        army_3.add_units(Warrior, 20)
        army_3.add_units(Knight, 5)

        army_4 = Army()
        army_4.add_units(Warrior, 30)

        battle = Battle()

        assert battle.fight(my_army, enemy_army) == True
        assert battle.fight(army_3, army_4) == False
        print("Coding complete? Let's try tests!")
