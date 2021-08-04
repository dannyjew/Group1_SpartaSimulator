import random


class Container:
    def __init__(self):
        self.is_full = False
        self.members = 0

    def add(self, num: int):
        self.members += num


class Centre(Container):
    def __init__(self):
        super().__init__()
        self.size = 100
        self.remainder = 0
        self.used_up = False
        self.added = 0

    def add_trainees(self, num):
        available_space = self.size - self.members
        new_num = clamp(num, 0, min(20 - self.added, available_space))
        self.added += new_num
        self.add(new_num)
        if self.size == self.members:
            self.is_full = True
        return num - new_num

    # def add_trainees(self, num):
    #     self.remainder = 0
    #     if num >= 20:
    #         excess_trainees = num - 20
    #         num = 20
    #         self.remainder = excess_trainees
    #         self.used_up = True
    #
    #     if self.size - self.members > num:
    #         self.add(num)
    #
    #     elif self.size - self.members <= num:
    #         space_available = self.size - self.members
    #         self.is_full = True
    #         self.add(space_available)
    #         self.remainder += num - space_available
    #     print(f"remainder = {self.remainder}")
    #     return self.remainder
    # maybe return the remainder to then add to another open centre in the main file?


class WaitingList(Container):
    def __init__(self):
        super().__init__()

    def subtract(self, num: int):
        self.members -= num


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)