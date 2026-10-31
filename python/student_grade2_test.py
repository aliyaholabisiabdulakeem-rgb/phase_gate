from unittest import TestCase
from student_grade2 import *

def calculate_position(total, position, students_number):
    for index in range(students_number):
        position[index] = 1
        for count in range(students_number):
            if total[count] > total[index]:
                position[index] += 1

class TestStudentGrade(TestCase):

    def test_grade_for_a_student(self):
        total = [100]
        position = [0]
        calculate_position(total, position, 1)
        self.assertEqual(position, [1])

    def that_more_than_one_students_can_get_a_first_place(self):
        total = [100, 100]
        position = [0, 0]
        calculate_position(total, position, 2)
        self.assertEqual(position, [1, 1])

    def test_that_display_works(self):
        scores = [[24, 23], [23, 26]]
        total = [47, 49]
        position = [2, 1]

    def test_that_all_scores_can_be_zero(self):
        total = [0, 0]
        position = [0, 0]
        calculate_position(total, position, 2)
        self.assertEqual(position, [1, 1])
