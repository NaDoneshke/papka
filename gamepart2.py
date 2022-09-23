import random
import time


class Human:
    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.money = 200
        self.car = None

    def nothing(self):
        print(
            f"{self.name} ничего не делает. Счастье: {self.gladness} Деньги: {self.money}")

    def rest(self):
        cost = 15
        # Проверяем достаточно ли денег
        # Если нет, то человек ничего не делает
        # Если есть, то действия ниже
        if self.money >= cost:
            self.gladness += random.randint(3, 5)
            # Уровень счастья не может быть больше 100
            if self.gladness >= 100:
                self.gladness = 100
            # =======================================
            self.money -= cost
            print(
                f"{self.name} отдыхает. Счастье: {self.gladness} Деньги: {self.money}")
        else:
            self.nothing()

    def work(self):
        self.gladness -= random.randint(2, 5)
        # Уровень счастья не может быть меньше 0
        if self.gladness <= 0:
            self.gladness = 0
        # =======================================
        self.money += 20
        print(f"{self.name} работает. Счастье: {self.gladness} Деньги: {self.money}")

    # Добавить использование функции drive машины
    def drive(self):
        if self.car:
            self.car.drive()


class Player(Human):
    def __init__(self, name):
        Human.__init__(self, name)

    def day(self):
        print(f"Имя: {self.name}")
        print(f"Счастье: {self.gladness}")
        print(f"Деньги: {self.money}")
        print("1. Ничего не делать")
        print("2. Отдохнуть")
        print("3. Работать")

    def game(self):
        choose = int(input("-> "))
        if choose == 1:
            self.nothing()
        elif choose == 2:
            self.rest()
        elif choose == 3:
            self.work()
        else:
            self.game()


class Car:
    def __init__(self, brend, price):
        self.brend = brend
        self.price = price
        self.owner = None

    def drive(self):
        if self.owner:
            print("Car is driving")

    def buy(self, human):
        # Проверяем есть ли у машины хозяин
        # Проверяем хватит ли человеку денег
        # Связываем машину с человеком
        # В принт выводим кто купил какую машину
        if not self.owner:
            if human.money >= self.price:
                human.money -= self.price
                self.owner = human
                self.owner.car = self
                print(f"{human.name} купил {self.brend}")
            else:
                print(
                    f"{human.name} не хватает {self.price - human.money} на покупку {self.brend}")
        else:
            print(f"У {self.brend} уже есть хозяин {self.owner.name}")


player = Player("Stephan")

humans = [
    Human(name="Andrey"),
    Human(name="Anton"),
    Human(name="Maxim"),
]

cars = [
    # Создать 3 машины
    Car("Audi", 200),
    Car("Bentli", 100),
    Car("Nissan", 700),
]

days = 1
while True:
    print(f"Day: {days}")
    player.day()
    player.game()
    for human in humans:
        action = random.choice([human.nothing, human.rest, human.work])
        action()
        # Каждый день человек с шансом 5% хочет купить себе случайну машину
        if random.randint(1, 100) <= 5:
            car = random.choice(cars)
            car.buy(human)
    days += 1
    time.sleep(0.1)

days = 1
while True:
    print(f"Day: {days}")
    player.day()
    player.game()
    for theif in theif:
        action = random.choice([theif.nothing, theif.thinks, theif.work])
        action()
        # Каждый день человек с шансом 10% может обокрасть случайного игрока
        if random.randint(1, 100) <= 10:
            rob = random.choice(player)
            their.rob(player)

    days += 1
    time.sleep(0.1)
    class Thief:
        def __init__(self, name):
            self.name = noname
            self.anger = 0
            self.money = 200
            self.car = Bobcat

        def nothing(self):
            print(
                f"{self.name} крадёт имущество. Хитрость: {self.gladness} Деньги: {self.money}")

        def rest(self):
            cost = 1000
            # Проверяем достаточно ли денег
            # Если нет, то человек ничего не делает
            # Если есть, то действия ниже
            if self.money >= cost:
                self.gladness += random.randint(3, 5)
                # Уровень счастья не может быть больше 100
                if self.anger >= 50:
                    self.anger = 50
                # =======================================
                self.money -= cost
                print(
                    f"{self.name} придумывает план. Думает: {self.gladness} Деньги: {self.money}")
            else:
                self.nothing()

        def work(self):
            self. anger -= random.randint(2, 5)
            # Уровень счастья не может быть меньше 0
            if self.intelligence <= 5:
                self.intelligence = 5
            # =======================================
            self.money += 500
            print(f"{self.name} ворует. радость: {self.gladness} Деньги: {self.money}")
