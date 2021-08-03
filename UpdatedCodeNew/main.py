from Simulationclass import *
from ContainerClasses import *
from time import sleep
from centre_creation import *

sim = simulation()
waitinglist = waiting_list()

print(f"Initial State\n")
sim.update(currentcentre, waitinglist)

while sim.simulation_length > 0:
    sleep(0.5)
    if sim.current_month %2 ==0:
        sim.new_centre()

    currentcentre.add_trainees()
    if currentcentre.is_full:
        sim.reset_centre(currentcentre)


    sim.simulation_length -= 1
    print(f"Current Month: {sim.current_month}.\n")
    sim.update(currentcentre, waitinglist)
    sim.current_month += 1

