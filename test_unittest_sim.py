import unittest
import SimulationClass
import ContainerClasses

class Simtests(unittest.TestCase):

    sim = SimulationClass.Simulation()
    sim2 = SimulationClass.Simulation()
    not_empty_wait_list = ContainerClasses.WaitingList()
    list_of_cen = [ContainerClasses.Centre()]
    empty_wait_list = ContainerClasses.WaitingList()
    list_of_cen2 = [ContainerClasses.Centre()]

    def test_input_length(self):
        self.assertEqual(self.sim.simulation_length, 5)

    def test_input_starting_cen(self):
        self.assertEqual(self.sim.total_centres, 5)

    def test_generator(self):
        check = list(range(20,31))
        self.assertIn(self.sim.generate_trainees(), check)

    def test_add_from_waiting_list(self):
        self.not_empty_wait_list.members = 50
        self.sim.add_from_waiting_list(self.not_empty_wait_list, self.list_of_cen,self.not_empty_wait_list.members)
        self.assertEqual(self.list_of_cen[0].members, 20)


    def test_total_trainees(self):
        self.assertEqual(self.sim2.total_trainees(self.list_of_cen2), 80)

    def test_assign_too_many_trainees(self):
        for i in range(3):
            self.sim2.add_new_centre(self.list_of_cen2)
        self.sim2.assign_trainees(self.empty_wait_list, self.list_of_cen2, 200)
        self.assertEqual(self.empty_wait_list.members, 120)

