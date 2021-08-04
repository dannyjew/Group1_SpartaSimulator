from SimulationClass import *
from ContainerClasses import *
from time import sleep
from CentreCreation import *


sim = Simulation()
waiting_list = WaitingList()

print(f"\nInitial State\n")
sim.update(currentcentre, waiting_list)

while sim.simulation_length >= sim.current_month:
    sleep(0.5)
    if sim.current_month % 2 == 0:
        sim.new_centre()

    currentcentre.add_trainees()
    if currentcentre.is_full:
        sim.reset_centre(currentcentre)

    print(f"Current Month: {sim.current_month}.\n")
    sim.update(currentcentre, waiting_list)
    sim.current_month += 1
