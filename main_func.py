from ContainerClasses import *


def main(sim, often=2):
    centre_list = []
    waiting_list = WaitingList()

    for i in range(sim.total_centres):
        centre_list.append(Centre())

    result = "Initial State\n" + sim.update(centre_list, waiting_list)
    sim.current_month += 1

    while sim.simulation_length >= sim.current_month:
        for centre in centre_list:
            centre.added = 0

        if sim.current_month % often == 0:
            sim.add_new_centre(centre_list)

        sim.add_from_waiting_list(waiting_list, centre_list, waiting_list.members)
        sim.assign_trainees(waiting_list, centre_list, sim.generate_trainees())

        result += sim.update(centre_list, waiting_list)
        sim.current_month += 1

    return result
