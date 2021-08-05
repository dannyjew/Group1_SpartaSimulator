from functions import is_int
from ContainerClasses import *
import random


class Simulation:
    def __init__(self):
        self.simulation_length = 0
        self.current_month = 0
        self.total_centres = 0
        self.full_centres = 0
        self.welcome_func()
        self.input_func()
        self.open_centres = self.total_centres - self.full_centres

    def welcome_func(self):
        print("\n     *** Welcome to this Sparta Simulation ***\n")

    def input_func(self):
        answer = 'None'
        self.simulation_length = int(is_int('How long do you want the simulation to last (in months)?: ', answer))
        self.total_centres = int(is_int('\nHow many open centres do you want to start with?: ', answer))

    def add_new_centre(self, centre_list):
        self.total_centres += 1
        centre_list.append(Centre())

    def add_from_waiting_list(self, waiting_list, centres_list, num):
        waiting_list.members = 0
        for centre in centres_list:
            num = centre.add_trainees(num)
        waiting_list.add(num)

    def assign_trainees(self, waiting_list, centres_list, num):
        total = 0
        for centre in centres_list:
            num = centre.add_trainees(num)
            if centre.is_full:
                total += 1
        waiting_list.add(num)
        self.full_centres = total

    def total_trainees(self, centres):
        total = 0
        for centre in centres:
            total += centre.members
        return total

    def generate_trainees(self):
        num = random.randint(20, 30)
        # print(f"rand number = {num}")
        return num

    def update(self, centre_name, waiting_list_name):

        print(f"Current Month: {self.current_month}.\n"
              f"-Total number of Open centres: {self.total_centres}.\n"
              f"-Total number of Full centres: {self.full_centres}.\n"
              f"-Total number of Trainees currently training: {self.total_trainees(centre_name)}.\n"
              f"-Total number of Trainees on the waiting list: {waiting_list_name.members}.\n\n")
