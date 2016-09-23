#!/usr/bin/env python3

# -------------------------------
# projects/netflix/Testnetflix.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

"""
This document tests the netflix python file
"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

import Netflix

# -----------
# Testnetflix
# -----------

class Testnetflix(TestCase):
    """
    Tests various aspects of the netflix Methods
    """
    # ----
    # read
    # ----

    def test_read_movie1(self):
        """Test read movie_id"""
        string = "100:"
        result = Netflix.netflix_read(string)
        self.assertEqual(result, 0)

    def test_read_movie2(self):
        """Test read movie_id"""
        string = "100"
        result = Netflix.netflix_read(string)
        self.assertNotEqual(result, 0)

    def test_read_movie3(self):
        """Test read movie_id"""
        string = "00"
        result = Netflix.netflix_read(string)
        self.assertNotEqual(result, 0)

    def test_read_customer1(self):
        """Test read customer_id"""
        string = "101\n"
        result = Netflix.netflix_read(string)
        self.assertEqual(result, 1)

    def test_read_customer2(self):
        """Test read customer_id"""
        string = "101:\n"
        result = Netflix.netflix_read(string)
        self.assertNotEqual(result, 1)

    def test_read_customer3(self):
        """Test read customer_id"""
        string = "10:\n"
        result = Netflix.netflix_read(string)
        self.assertNotEqual(result, 1)

    def test_read_customer4(self):
        """Test read customer_id"""
        string = "10\n"
        result = Netflix.netflix_read(string)
        self.assertNotEqual(result, 0)

    # -----
    # print
    # -----

    def test_print_1(self):
        """Test print1"""
        write = StringIO()
        Netflix.netflix_print(write, 1.3)
        self.assertEqual(write.getvalue(), "1.3\n")

    def test_print_2(self):
        """Test print2"""
        write = StringIO()
        Netflix.netflix_print(write, 1.3)
        self.assertNotEqual(write.getvalue(), ".3\n")

    def test_print_3(self):
        """Test print3"""
        write = StringIO()
        Netflix.netflix_print(write, 1000)
        self.assertEqual(write.getvalue(), "1000\n")

    def test_print_4(self):
        """Test print4"""
        write = StringIO()
        Netflix.netflix_print(write, 189)
        self.assertNotEqual(write.getvalue(), "9\n")

    # ----
    # load
    # ----

    def test_load_average(self):
        """Test total_average pulls int"""
        Netflix.load_files()
        self.assertNotEqual(Netflix.TOTAL_AVERAGE, 0.0)

    def test_load_movie_years(self):
        """ test movie_year set is modified"""
        Netflix.load_files()
        self.assertNotEqual(Netflix.MOVIE_YEARS, {})

    def test_load_actual_rating(self):
        """Test total_average pulls int"""
        Netflix.load_files()
        self.assertNotEqual(Netflix.ACTUAL_RATING, {})

    def test_load_customer_averages(self):
        """ test movie_year set is modified"""
        Netflix.load_files()
        self.assertNotEqual(Netflix.CUSTOMER_AVERAGES, {})

    def test_load_movie_averages(self):
        """ test movie_year set is modified"""
        Netflix.load_files()
        self.assertNotEqual(Netflix.MOVIE_AVERAGES, {})

    def test_load_movie_id(self):
        """movie_id should still be 0 here"""
        Netflix.load_files()
        self.assertEqual(Netflix.MOVIE_ID, 0)

    def test_load_customer_id(self):
        """ customer_id should still be 0 here"""
        Netflix.load_files()
        self.assertEqual(Netflix.CUSTOMER_ID, 0)

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        test solve
        """
        read = StringIO("10089:\n662823\n1693997\n1985602\n2345955\n1205751\n")
        word = StringIO()
        Netflix.netflix_solve(read, word)
        self.assertEqual(word.getvalue(), "10089:\n2.4\n4.4\n2.8\n3.0\n5.0\nRMSE: 0.59\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
