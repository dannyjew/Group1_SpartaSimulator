# As a user I want to be able to input length of the simulation
simulation_length = input('How long do you want the simulation to be (in months)')
print(simulation_length)
Start_trainingcentre = input('How many open centres you want to start with?  ')

# I want to be able to create training centre class so i can model training centres
class container():
    def __init__(self):
        self.is_full = False #This means it is open
        self.members = 0

    def add(self, num):
        self.members += num

class centre(container):
    def __init__(self):
        super().__init__(self)
        self.size = 100
        self.capacity = 0
        self.remainder = 0

    def add_trainees(self, num):
        if self.size == self.capacity:
            self.is_full = True

        elif self.size - self.capacity > num:
            self.add(num)

        elif self.size - self.capacity < num:
            space_avaliable = self.size - self.capacity
            self.add(space_avaliable)
            self.remainder += num - space_avaliable


class waiting_list(container):
    def __init__(self):
        super().__init__(self)

    def subtract(self, num):
        self.members -= num


# I want to be able to generate a random number
