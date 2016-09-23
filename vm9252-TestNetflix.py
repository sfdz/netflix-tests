#!/usr/bin/env/python3
# pylint: disable=R0904
"""
Unit tests for Netflix module
"""

from io import StringIO
from unittest import main, TestCase
from Netflix import solve, predict

class TestNetflix(TestCase):
    """
    Contains tests for Netflix
    """
    def test_solve_format(self):
        """Tests that solve print the same movie ids on the right line"""
        reader = StringIO("1:\n30878\n10016:\n1751359\n234929\n")
        writer = StringIO()
        solve(reader, writer)
        line = writer.getvalue().split('\n', 5)
        self.assertEqual(line[0], "1:")
        self.assertEqual(line[2], "10016:")

    def test_solve_format_2(self):
        """Tests that solve prints predictions in the right format"""
        reader = StringIO("1:\n30878\n10016:\n1751359\n234929\n")
        writer = StringIO()
        solve(reader, writer)
        line = writer.getvalue().split('\n', 5)
        for line_number in (1, 3, 4):
            self.assertEqual(len(line[line_number]), 3)
            self.assertTrue(line[line_number][0].isdigit())
            self.assertEqual(line[line_number][1], ".")
            self.assertTrue(line[line_number][2].isdigit())

    def test_solve_format_3(self):
        """Tests that solve prints RMSE in the right format"""
        reader = StringIO("1:\n30878\n10016:\n1751359\n234929\n")
        writer = StringIO()
        solve(reader, writer)
        line = writer.getvalue().split('\n', 5)
        self.assertEqual(len(line[5]), 11)
        self.assertEqual(line[5][:6], "RMSE: ")
        self.assertTrue(line[5][6].isdigit())
        self.assertEqual(line[5][7], ".")
        self.assertTrue(line[5][8].isdigit())
        self.assertTrue(line[5][9].isdigit())

    def test_prediction(self):
        """Tests that predictions of valid input are between 1 and 5"""
        value = predict(1, 30878)
        self.assertTrue(1.0 <= value and 5.0 >= value)

    def test_prediction_2(self):
        """Tests that predictions of valid input are between 1 and 5"""
        value = predict(10016, 1751359)
        self.assertTrue(1.0 <= value and 5.0 >= value)

    def test_prediction_3(self):
        """Tests that predictions of valid input are between 1 and 5"""
        value = predict(10016, 234929)
        self.assertTrue(1.0 <= value and 5.0 >= value)

if __name__ == "__main__":
    main()
