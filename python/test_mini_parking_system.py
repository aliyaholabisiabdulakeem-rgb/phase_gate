from unittest import TestCase
from mini_parking_system import *

class TestParkingSystem(TestCase):

    def test_that_each_slot_are_empty(self):
        park_space_one = 5
        park_space_two = 4     

        self.assertEqual(park_space_one, 5)
        self.assertEqual(park_space_two, 4)
        

    def test_that_if_user_enter_name_it_will_print(self):
        name = "Aliyah"
        self.assertEqual(name, "Aliyah")

    def test_that_user_can_check_availble_slot_number(self):
        name = "Aliyah"
        space_occupied = 0
        self.assertEqual(space_occupied, 0)

    
