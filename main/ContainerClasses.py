import random


class Container:
    def __init__(self):
        self.is_full = False
        self.members = 0

    def add(self, num:int):
        self.members += num


class Centre(Container):
    def __init__(self):
        super().__init__()
        self.size = 100
        self.remainder = 0

    def add_trainees(self, num=random.randint(20, 30)):

        if num > 20:
            excess_trainees = num - 20
            num = 20
            self.remainder = excess_trainees

        if self.size == self.members:
            self.is_full = True

        elif self.size - self.members > num:
            self.add(num)

        elif self.size - self.members <= num:
            space_available = self.size - self.members
            self.is_full = True
            self.add(space_available)
            self.remainder += num - space_available
        return self.remainder
    # maybe return the remainder to then add to another open centre in the main file?


class WaitingList(Container):
    def __init__(self):
        super().__init__()

    def subtract(self, num: int):
        self.members -= num
