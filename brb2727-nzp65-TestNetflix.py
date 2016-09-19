#!/usr/bin/env python3

# ---------------------------
# Copyright (C) 2016
# Brian Bechtel
# ---------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""
Test harness for collatz conjecture program
"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase, expectedFailure

from Netflix import init, reset, netflix_solve, netflix_eval, check_init
import Netflix
# -----------
# TestNetflix
# -----------


class TestNetflix(TestCase):

    """
    Unit Test Class
    """
    actual_ratings = {
        123: {1: 1.0, 2: 4.0, 3: 5.0}, 456: {1: 3.0, 2: 1.0, 3: 4.0},
        789: {1: 2.0, 2: 5.0, 3: 4.0}, 349: {1: 3.0, 2: 1.0, 3: 3.0}}
    movie_averages = {123: 3.33, 456: 2.67, 789: 3.67, 349: 2.33}
    customer_averages = {1: 2.25, 2: 2.75, 3: 4.0}
    customer_year_averages = {
        1: {2004: 1.0, 1987: 3.0, 1964: 2.0, 1976: 3.0},
        2: {2004: 4.0, 1987: 1.0, 1964: 5.0, 1976: 1.0},
        3: {2004: 5.0, 1987: 4.0, 1964: 4.0, 1976: 3.0}}
    movie_years = {123: 2004, 456: 1987, 789: 1964, 349: 1976}

    @staticmethod
    def setup():
        "reset / unitialize the caches"
        reset()

    def test_reset1(self):
        " test that reset() works"
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        reset()
        self.assertEqual({}, Netflix.actual_ratings)
        self.assertEqual({}, Netflix.movie_averages)
        self.assertEqual({}, Netflix.customer_averages)
        self.assertEqual({}, Netflix.customer_year_averages)
        self.assertEqual({}, Netflix.movie_years)
        self.assertFalse(Netflix.initialized)

    @staticmethod
    @expectedFailure
    def test_check_init1():
        """ test check_init fails if did not call init """
        check_init()

    def test_check_init2(self):
        """ test check_init works after calling init """
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        check_init()  # will pass if check_init does not throw exception

    def test_init1(self):
        """ tests init works on one test caches """
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        self.assertEqual(self.actual_ratings, Netflix.actual_ratings)
        self.assertEqual(self.movie_averages, Netflix.movie_averages)
        self.assertEqual(self.customer_averages, Netflix.customer_averages)
        self.assertEqual(
            self.customer_year_averages, Netflix.customer_year_averages)
        self.assertEqual(self.movie_years, Netflix.movie_years)
        self.assertTrue(Netflix.initialized)

    def test_init2(self):
        """ tests init works on None """
        init(None, None, None, None, None)
        self.assertEqual(None, Netflix.actual_ratings)
        self.assertEqual(None, Netflix.movie_averages)
        self.assertEqual(None, Netflix.customer_averages)
        self.assertEqual(None, Netflix.customer_year_averages)
        self.assertEqual(None, Netflix.movie_years)
        self.assertTrue(Netflix.initialized)

    def test_init3(self):
        """ test that initialized variable is false at start """
        reset()
        self.assertFalse(Netflix.initialized)

    @staticmethod
    @expectedFailure
    def test_netflix_eval_1():
        """ makes sure an exception is raised if not initialized """
        reset()
        netflix_eval(2, 456)

    def test_netflix_eval2(self):
        """ tests netflix_eval on test data """
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        prediction = netflix_eval(2, 456)
        self.assertEqual(prediction, 2.1)

    def test_netflix_eval3(self):
        """ tests netflix_eval on test data """
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        prediction = netflix_eval(3, 789)
        self.assertEqual(prediction, 3.9)

    def test_netflix_eval4(self):
        """ tests netflix_eval on test data """
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        prediction = netflix_eval(1, 349)
        self.assertEqual(prediction, 2.5)

    def test_netflix_eval5(self):
        """ tests netflix_eval on test data """
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        prediction = netflix_eval(3, 123)
        self.assertEqual(prediction, 4.1)

    def test_netflix_eval6(self):
        """ tests netflix_eval on test data """
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        prediction = netflix_eval(2, 789)
        self.assertEqual(prediction, 3.8)

    @staticmethod
    @expectedFailure
    def test_netflix_not_initialized():
        """ makes sure an exception is raised if not initialized """
        netflix_solve("", "")

    def test_netflix_sample(self):
        """ tests netflix_solve on sample test data """
        reader = StringIO("123:\n1\n2\n3")
        writer = StringIO()
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "123:\n2.2\n3.4\n4.1\nRMSE: 0.93\n")

    def test_netflix_all(self):
        """ tests netflix_solve on a test data """
        init(self.actual_ratings, self.movie_averages, self.customer_averages,
             self.customer_year_averages, self.movie_years)
        reader = StringIO(
            "123:\n1\n2\n3\n456:\n1\n2\n3\n789:\n1\n2\n3\n349:\n1\n2\n3\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "123:\n2.2\n3.4\n4.1\n"
                         + "456:\n2.6\n2.1\n3.6\n"
                         + "789:\n2.6\n3.8\n3.9\n"
                         + "349:\n2.5\n2.0\n3.1\n"
                         + "RMSE: 0.78\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
