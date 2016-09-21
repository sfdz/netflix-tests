#!/usr/bin/env python3

"""Unit Tests for Netflix.py"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix(TestCase):
    """Unit Tests for Netflix.py"""
    # ----
    # read
    # ----

    def test_read_1(self):
        """Test netflix_read for a customer ID"""
        string = '123\n'
        data_id, data_type = netflix_read(string)
        self.assertEqual(data_id, 123)
        self.assertEqual(data_type, 'customer')

    def test_read_2(self):
        """Test netflix_read for a movie ID"""
        string = '123:\n'
        data_id, data_type = netflix_read(string)
        self.assertEqual(data_id, 123)
        self.assertEqual(data_type, 'movie')

    def test_read_3(self):
        """Test netflix_read for a string"""
        string = 'abc\n'
        error = False
        try:
            netflix_read(string)
        except ValueError:
            error = True
        self.assertTrue(error)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """Test netflix_eval"""
        rating, actual = netflix_eval(30878, 1)
        self.assertEqual(rating, 3.7255000228804325)
        self.assertEqual(actual, 4)

    def test_eval_2(self):
        """Test netflix_eval"""
        rating, actual = netflix_eval(1952305, 10)
        self.assertEqual(rating, 2.9539170532434964)
        self.assertEqual(actual, 3)

    def test_eval_3(self):
        """Test netflix_eval"""
        rating, actual = netflix_eval(1485175, 10012)
        self.assertEqual(rating, 3.782384142757868)
        self.assertEqual(actual, 3)

    def test_eval_4(self):
        """Test netflix_eval"""
        rating, actual = netflix_eval(430376, 10014)
        self.assertEqual(rating, 3.2289684823453744)
        self.assertEqual(actual, 3)

    # -----
    # print
    # -----

    def test_print_1(self):
        """Test netflix_print for an int"""
        writer = StringIO()
        netflix_print(writer, 10)
        self.assertEqual(writer.getvalue(), "10\n")

    def test_print_2(self):
        """Test netflix_print for a string"""
        writer = StringIO()
        netflix_print(writer, 'abc')
        self.assertEqual(writer.getvalue(), "abc\n")

    def test_print_3(self):
        """Test netflix_print for 2 lines"""
        writer = StringIO()
        netflix_print(writer, 'abc\n123')
        self.assertEqual(writer.getvalue(), "abc\n123\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """Test netflix_solve"""
        reader = StringIO("1123:\n448549\n2444222\n1522889\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1123:\n3.3\n2.9\n4.1\nRMSE: 0.4148335185443161\n")

    def test_solve_2(self):
        """Test netflix_solve"""
        reader = StringIO("1:\n1989766\n\n2380848\n")
        writer = StringIO()
        error = False
        try:
            netflix_solve(reader, writer)
        except ValueError:
            error = True
        self.assertTrue(error)

# ----
# main
# ----

if __name__ == "__main__":
    main()
