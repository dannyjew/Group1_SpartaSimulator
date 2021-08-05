from functions import clamp


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
        self.added = 0

    def add_trainees(self, num):
        available_space = self.size - self.members
        new_num = clamp(num, 0, min(20 - self.added, available_space))
        self.added += new_num
        self.add(new_num)
        if self.size == self.members:
            self.is_full = True
        return num - new_num


class WaitingList(Container):
    def __init__(self):
        super().__init__()

    def subtract(self, num: int):
        self.members -= num
