from SimulationClass import *
from ContainerClasses import *
from time import sleep


centre_list = []
sim = Simulation()
waiting_list = WaitingList()

for i in range(sim.total_centres):
    centre_list.append(Centre())

print(f"\nInitial State\n")
sim.update(centre_list, waiting_list)
sim.current_month += 1

while sim.simulation_length >= sim.current_month:
    # sleep(0.5)
    for centre in centre_list:
        centre.added = 0

    if sim.current_month % 2 == 0:
        sim.add_new_centre(centre_list)

    sim.add_from_waiting_list(waiting_list, centre_list, waiting_list.members)
    sim.assign_trainees(waiting_list, centre_list, sim.generate_trainees())

    # for centre in centre_list:
    #     print(centre_list.index(centre), centre.members, centre.remainder)

    sim.update(centre_list, waiting_list)
    sim.current_month += 1
