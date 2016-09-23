#!/usr/bin/env python3

# -----------------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2016
# Elizabeth Haynes and Kirsten Thomas
# -----------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""Testing file for unit tests"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import actual_rating, movie_year, movies_avg_weighted, customers_avg_weighted
from Netflix import netflix_read, netflix_guess, netflix_error, netflix_print, netflix_solve


class TestNetflix(TestCase):

    """
    Use TestCase class for unit testing
    """
    # ------------
    # netflix_read
    # ------------

    def test_read1(self):
        """
        Test that cache imports
        """
        netflix_read()
        num_keys = actual_rating.keys()
        self.assertNotEqual(num_keys, 0)

    def test_read2(self):
        """
        Test that cache imports
        """
        netflix_read()
        num_keys = movie_year.keys()
        self.assertNotEqual(num_keys, 0)

    def test_read3(self):
        """
        Test that cache imports
        """
        netflix_read()
        num_keys = movies_avg_weighted.keys()
        self.assertNotEqual(num_keys, 0)

    def test_read4(self):
        """
        Test that cache imports
        """
        netflix_read()
        num_keys = customers_avg_weighted.keys()
        self.assertNotEqual(num_keys, 0)

    # -------------
    # netflix_guess
    # -------------

    def test_guess1(self):
        """
        Test that guess is above 0
        """
        netflix_read()
        guess = netflix_guess(788, 613501)
        positive = guess > 0
        self.assertTrue(positive)

    def test_guess2(self):
        """
        Test that guess is below 6
        """
        netflix_read()
        guess = netflix_guess(939, 531806)
        small = guess < 6
        self.assertTrue(small)

    def test_guess3(self):
        """
        Test that guess is a float
        """
        netflix_read()
        guess = netflix_guess(1200, 855860)
        self.assertIsInstance(guess, float)

    # -------------
    # netflix_error
    # -------------

    def test_error1(self):
        """
        Test when guess is too small
        """
        netflix_read()
        error_squared = netflix_error(10010, 1462925, 3.6)
        self.assertEqual("{:.2f}".format(error_squared), "0.16")

    def test_error2(self):
        """
        Test when guess is too big
        """
        netflix_read()
        error_squared = netflix_error(5733, 1168036, 3.7)
        self.assertEqual("{:.2f}".format(error_squared), "2.89")

    def test_error3(self):
        """
        Test when (rounded) guess is exactly right
        """
        netflix_read()
        error_squared = netflix_error(913, 320468, 3.0)
        self.assertEqual(error_squared, 0)

    # -------------
    # netflix_print
    # -------------

    def test_print1(self):
        """
        Test printing movie format
        """
        writer = StringIO()
        netflix_print(writer, "6478:\n", "Movie")
        self.assertEqual(writer.getvalue(), "6478:\n")

    def test_print2(self):
        """
        Test printing rating guess format
        """
        writer = StringIO()
        netflix_print(writer, 3.721318657451, "Rating Guess")
        self.assertEqual(writer.getvalue(), "3.7\n")

    def test_print3(self):
        """
        Test printing RMSE format
        """
        writer = StringIO()
        netflix_print(writer, 0.9722263548654, "RMSE")
        self.assertEqual(writer.getvalue(), "RMSE: 0.97\n")

    # -------------
    # netflix_solve
    # -------------

    def test_solve1(self):
        """
        Test that output is in string format
        """
        reader = StringIO("1:\n30878\n2647871\n1283744\n2488120")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertIsInstance(writer.getvalue(), str)

    def test_solve2(self):
        """
        Test RMSE is small enough
        """
        reader = StringIO(
            "17196:\n2198419\n1755064\n1998353\n1389451\n2432807\n1535594\n314509")
        writer = StringIO()
        netflix_solve(reader, writer)
        string = writer.getvalue()
        num = float(string[-4:])
        small = num < 1
        self.assertTrue(small)

    def test_solve3(self):
        """
        Test RMSE is positive
        """
        reader = StringIO(
            "6476:\n669662\n211046\n465035\n2086504\n1584927\n1535620\n411684")
        writer = StringIO()
        netflix_solve(reader, writer)
        string = writer.getvalue()
        num = float(string[-4:])
        positive = num > 0
        self.assertTrue(positive)

# ----
# main
# ----

if __name__ == "__main__":
    main()
