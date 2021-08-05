import unittest
import ContainerClasses


class Methodtests(unittest.TestCase):

    con = ContainerClasses.Container()
    cen = ContainerClasses.Centre()
    wait = ContainerClasses.WaitingList()
    new_cen = ContainerClasses.Centre()
    new_con = ContainerClasses.Container()
    month_cen = ContainerClasses.Centre()
    full_cen = ContainerClasses.Centre()


    def test_created_cen_check(self):
        self.assertFalse(self.cen.is_full)

    def test_empty_container(self):
        self.assertEqual(self.new_con.members, 0)

    def test_container_add(self):
        self.con.add(5)
        self.assertEqual(self.con.members, 5)

    def test_empty_centre(self):
        self.assertEqual(self.new_cen.members, 0)

    def test_add_trainees(self):
        self.cen.add_trainees(20)
        self.assertEqual(self.cen.members, 20)

    def test_monthly_cap_cen(self):
        self.month_cen.add_trainees(30)
        self.month_cen.add_trainees(20)
        self.assertEqual(self.month_cen.members, 20)

    def test_full_cen(self):
        self.full_cen.add_trainees(20)
        self.full_cen.added = 0
        self.full_cen.add_trainees(20)
        self.full_cen.added = 0
        self.full_cen.add_trainees(20)
        self.full_cen.added = 0
        self.full_cen.add_trainees(20)
        self.full_cen.added = 0
        self.full_cen.add_trainees(20)
        self.full_cen.added = 0
        self.full_cen.add_trainees(20)
        self.full_cen.added = 0
        self.assertEqual(self.full_cen.members,100)







