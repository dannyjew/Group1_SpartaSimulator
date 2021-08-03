import random

class container():
    def __init__(self):
        self.is_full = False
        self.members = 0

    def add(self, num:int):
        self.members += num

class centre(container):
    def __init__(self):
        super().__init__()
        self.size = 100
        self.remainder = 0

    def add_trainees(self):
        num = random.randint(20,30)
        excess_trainees = num - 20
        if self.size == self.members:
            self.is_full = True

        elif self.size - self.members > 20:
            self.add(20)

        elif self.size - self.members < 20:
            space_avaliable = self.size - self.members
            self.is_full = True
            self.add(space_avaliable)
            self.remainder += 20 - space_avaliable + excess_trainees


class waiting_list(container):
    def __init__(self):
        super().__init__()

    def subtract(self, num:int):
        self.members -= num

