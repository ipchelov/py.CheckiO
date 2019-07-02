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

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1

class Vampire(Warrior):
    def __init__(self):
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5




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
        elif soldier_to_add == Defender:
            for i in range(soldier_to_add_amount):
                self.soldiers.append(Defender())
        elif soldier_to_add == Vampire:
            for i in range(soldier_to_add_amount):
                self.soldiers.append(Vampire())


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
    def damage_get(unit_1, unit_2):
        if unit_2.__class__ == Defender:
            if unit_2.defense < unit_1.attack:
                get_damage=unit_1.attack - unit_2.defense
                unit_2.health -= get_damage
        else:
            get_damage = unit_1.attack
            unit_2.health-=get_damage
        if unit_1.__class__ == Vampire:
            unit_1.health+=get_damage * unit_1.vampirism

        return unit_2.is_alive

    while True:
        if not damage_get(unit_1, unit_2):
            break

        if not damage_get(unit_2, unit_1):
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

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

