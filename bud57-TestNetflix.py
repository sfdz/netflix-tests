#!/usr/bin/env python3
"""Unit tests for Netflix.py"""

# errors from running autopep8
# pylint: disable = bad-continuation
# pylint: disable = line-too-long

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_predict_rating, netflix_rmse, netflix_solve

# -----------
# TestNetflix
# -----------


class TestNetflix(TestCase):

    """Unit tests for Netflix.py"""

    # ----
    # rmse
    # ----

    def test_netflix_rmse_1(self):
        """Test netflix_rmse"""
        guess_dict = {0: 4, 1: 4, 2: 7}
        true_dict = {0: 2, 1: 2, 2: 4}
        self.assertEqual(netflix_rmse(guess_dict, true_dict), 2.38)

    def test_netflix_rmse_2(self):
        """Test netflix_rmse"""
        guess_dict = {0: 0, 1: 90, 2: 7}
        true_dict = {0: 10, 1: 20, 2: 20, 80: 1}
        self.assertEqual(netflix_rmse(guess_dict, true_dict), 41.50)

    def test_netflix_rmse_3(self):
        """Test netflix_rmse"""
        guess_dict = {123: 1}
        true_dict = {123: 1}
        self.assertEqual(netflix_rmse(guess_dict, true_dict), 0.00)

    # ----------------------
    # netflix_predict_rating
    # ----------------------

    def test_netflix_predict_rating_1(self):
        """Test netflix_predict_rating"""
        self.assertEqual(netflix_predict_rating(3.14159, 0), 3.1)

    def test_netflix_predict_rating_2(self):
        """Test netflix_predict_rating"""
        self.assertEqual(netflix_predict_rating(3, 1), 4.0)

    def test_netflix_predict_rating_3(self):
        """Test netflix_predict_rating"""
        self.assertEqual(netflix_predict_rating(10, 1.1), 11.1)

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """Test netflix_solve"""
        reader = StringIO("1:\n1\n2\n3\n4\n5\n6\n2:\n1\n2\n3\n4\n")
        writer = StringIO()

        true_dict = {("1", "1"): 5, ("1", "2"): 1, ("1", "3"): 2, ("1", "4"): 4, ("1", "5")
                      : 1, ("1", "6"): 2, ("2", "1"): 5, ("2", "2"): 4, ("2", "3"): 5, ("2", "4"): 5}
        movie_avg_dict = {1: 3.2, 2: 4.1}
        cust_avg_dev_dict = {1: 0.7, 2: 0.3, 3: 0.1, 4: 0.1, 5: 0.5, 6: 0.8}
        netflix_solve(
            reader, writer, true_dict, movie_avg_dict, cust_avg_dev_dict)

        self.assertEqual(writer.getvalue(),
                         "1:\n3.9\n3.5\n3.3\n3.3\n3.7\n4.0\n2:\n4.8\n4.3\n4.1\n4.1\n1.5")

    def test_solve_2(self):
        """Test netflix_solve"""
        reader = StringIO("1:\n1\n")
        writer = StringIO()

        true_dict = {("1", "1"): 1}
        movie_avg_dict = {1: 3}
        cust_avg_dev_dict = {1: 0.1}
        netflix_solve(
            reader, writer, true_dict, movie_avg_dict, cust_avg_dev_dict)

        self.assertEqual(writer.getvalue(), "1:\n3.1\n2.1")

    def test_solve_3(self):
        """Test netflix_solve"""
        reader = StringIO("1:\n5\n3\n2:\n1\n2\n4\n")
        writer = StringIO()

        true_dict = {("1", "1"): 5, ("1", "2"): 1, ("1", "3"): 2, ("1", "4"): 4, ("1", "5")
                      : 1, ("1", "6"): 2, ("2", "1"): 5, ("2", "2"): 4, ("2", "3"): 5, ("2", "4"): 5}
        movie_avg_dict = {1: 4.7, 2: 4.1}
        cust_avg_dev_dict = {1: 0.3, 2: 0.1, 3: 0.1, 4: 0.2, 5: 0.4}
        netflix_solve(
            reader, writer, true_dict, movie_avg_dict, cust_avg_dev_dict)

        self.assertEqual(
            writer.getvalue(), "1:\n5.1\n4.8\n2:\n4.3\n4.1\n4.3\n2.26")

# ----
# main
# ----

if __name__ == "__main__":
    main()
