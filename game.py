import random


class Dog:
    def __init__(self, name):
        self.name = Rex
        self.progress = 0
        self.gladness = random.randint(20, 40)

    def sleep(self):
        # Уменьшается прогресс, но повышается счастье
        self.progress -= random.randint(2, 5)
        self.gladness += random.randint(3, 5)
        pass

def sleep(self):
    print(f"{self.name} спит")

    def jump(self):
        # Уменьшается счастье, но повышается прогресс
        self.progress += random.randint(3, 5)
        self.gladness -= random.randint(2, 5)
        pass


dogs = [
    Dog(name="Rex"),
    Dog(name="Finn"),
    Dog(name="Ollie"),
]


days = 1
end = False
while True:
    print(f"Day: {days}")
    for student in students:
        # Выбираем случайное действие студента
        action = random.choice([student.rest, student.study])
        action()
        if student.progress > 100:
            end = True
    if end:
        break
    days += 1

print(students[0].progress, students[1].progress, students[2].progress)
