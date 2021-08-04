class Simulation:
    def __init__(self):
        self.simulation_length = 0
        self.current_month = 1
        self.total_centres = 0
        self.full_centres = 0
        self.input()
        self.open_centres = self.total_centres - self.full_centres

    def input(self):
        self.simulation_length += int(input('How long do you want the simulation to be (in months)?: '))
        self.total_centres = int(input('How many open centres you want to start with?: '))

    def new_centre(self):
        self.total_centres += 1

    def reset_centre(self, centre_name):
        self.full_centres += 1
        centre_name.members = centre_name.remainder
        centre_name.is_full = False

    def total_trainees(self, centre_name):
        return (self.full_centres*100) + centre_name.members

    def update(self, centre_name, waiting_list_name):

        print(f"-Total number of Open centres: {self.total_centres}.\n"
              f"-Total number of Full centres: {self.full_centres}.\n"
              f"-Total number of Trainees currently training in centres: {self.total_trainees(centre_name)}.\n"
              f"-Total number of Trainees on the waiting list: {waiting_list_name.members}.\n\n")
