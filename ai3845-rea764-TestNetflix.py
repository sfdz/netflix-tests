#!/usr/bin/env python3

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt
"""
Unit tests for Netflix.py functions
"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_eval, netflix_print, netflix_solve

# -----------
# Testnetflix
# -----------


class TestNetflix(TestCase):

    """
    All test cases
    """

    # -----
    # eval
    # -----

    def test_netflix_eval_1(self):
        """
        Test 1 netflix_eval to see if it
        makes the correct prediction
        """
        movie_cache = {'1': 3.7, '2': 1, '3': 1}
        movie_year_cache = {1: 2000, 2: 1999, 3: 1995}
        cust_year_cache = {1: {1999: 1}, 2: {2000: 3.7}, 3: {1995: 1}}
        self.assertEqual(
            netflix_eval(1, movie_cache, 2, movie_year_cache, cust_year_cache), 3.7)

    def test_netflix_eval_2(self):
        """
        Test 2 netflix_eval to see if it
        makes the correct prediction
        """
        movie_cache = {'1': 4.0, '2': 1, '3': 1}
        movie_year_cache = {1: 2005, 2: 1999, 3: 1995}
        cust_year_cache = {1: {2010: 1.5}, 2: {2005: 5}, 3: {1995: 4}}
        self.assertEqual(
            netflix_eval(1, movie_cache, 2, movie_year_cache, cust_year_cache), 5)

    def test_netflix_eval_3(self):
        """
        Test 3 netflix_eval to see if it
        makes the correct prediction
        """
        movie_cache = {'1': 5, '2': 1.9, '3': 3.2}
        movie_year_cache = {1: 2005, 2: 1999, 3: 1995}
        cust_year_cache = {1: {2010: 1.5}, 2: {2005: 5}, 3: {1995: 4}}
        self.assertEqual(
            netflix_eval(3, movie_cache, 3, movie_year_cache, cust_year_cache), 3.5)

    def test_netflix_eval_4(self):
        """
        Test 4 netflix_eval to see if it
        makes the correct prediction
        """
        movie_cache = {'1': 3.7, '2': 1, '3': 4}
        movie_year_cache = {1: 2005, 2: 1999, 3: 1995}
        cust_year_cache = {1: {2010: 1.5}, 2: {2005: 5}, 3: {1995: 2.0}}
        self.assertEqual(
            netflix_eval(3, movie_cache, 3, movie_year_cache, cust_year_cache), 2.3)

    def test_netflix_eval_5(self):
        """
        Test 5 netflix_eval to see if it
        makes the correct prediction
        """
        movie_cache = {'1': 3.7, '2': 1, '3': 4}
        movie_year_cache = {1: 2005, 2: 1999, 3: 1995}
        cust_year_cache = {1: {2010: 1.5}, 2: {1999: 1.0}, 3: {1995: 2.0}}
        self.assertEqual(
            netflix_eval(2, movie_cache, 2, movie_year_cache, cust_year_cache), 1)

    def test_netflix_eval_6(self):
        """
        Test 6 netflix_eval to see if it
        makes the correct prediction
        """
        movie_cache = {'1': 3.7, '2': 3.5, '3': 4}
        movie_year_cache = {1: 2005, 2: 1999, 3: 1995}
        cust_year_cache = {1: {2010: 1.5}, 2: {1999: 1.9}, 3: {2005: 2.0}}
        self.assertEqual(
            netflix_eval(1, movie_cache, 3, movie_year_cache, cust_year_cache), 2.0)

    # -----
    # print
    # -----
    def test_netflix_print_1(self):
        """
        Test 1 netflix_print to see if
        movies are formatted correctly
        """
        write = StringIO()
        netflix_print(write, '123:', 'movie')
        self.assertEqual(write.getvalue(), '123:\n')

    def test_netflix_print_2(self):
        """
        Test 2 netflix_print to see if
        movies are formatted correctly
        """
        write = StringIO()
        netflix_print(write, '199999:', 'movie')
        self.assertEqual(write.getvalue(), '199999:\n')

    def test_netflix_print_3(self):
        """
        Test 3 netflix_print to see if
        ratings are formatted correctly
        """
        write = StringIO()
        netflix_print(write, 3.5456465, 'rating')
        self.assertEqual(write.getvalue(), '3.5\n')

    def test_netflix_print_4(self):
        """
        Test 4 netflix_print to see if
        ratings are formatted correctly
        """
        write = StringIO()
        netflix_print(write, 1, 'rating')
        self.assertEqual(write.getvalue(), '1.0\n')

    def test_netflix_print_5(self):
        """
        Test 5 netflix_print to see if the
        rmse is formatted correctly
        """
        write = StringIO()
        netflix_print(write, .9849846, 'rmse')
        self.assertEqual(write.getvalue(), 'RMSE: 0.98\n')

    def test_netflix_print_6(self):
        """
        Test 6 netflix_print to see if the
        rmse is formatted correctly
        """
        write = StringIO()
        # NOTE: We round instead of truncate. Is this permissable?
        netflix_print(write, .555555, 'rmse')
        self.assertEqual(write.getvalue(), 'RMSE: 0.56\n')

    # -----
    # solve
    # -----
    def test_netflix_solve_1(self):
        """
        Test 1 to see if
        solving correctly
        """
        read = StringIO(
            "10002:\n1450941\n1213181\n308502\n2581993\n10003:\n1515111")
        write = StringIO()
        actual_ratings = {
            10002: {1450941: 2, 1213181: 3, 308502: 4, 2581993: 3}, 10003: {1515111: 1}}
        movie_cache = {'10002': 3.7, '10003': 1.75}
        movie_year_cache = {10002: 2005, 10003: 1999}
        cust_year_cache = {1450941: {2005: 3.5}, 1213181: {2005: 4.987},
                           308502: {2005: 5}, 2581993: {2005: 3}, 1515111: {1999: 3}}
        netflix_solve(read, write, actual_ratings,
                      movie_cache, movie_year_cache, cust_year_cache)
        self.assertEqual(
            write.getvalue(), "10002:\n3.5\n5.0\n5.0\n3.0\n10003:\n1.0\nRMSE: 1.20\n")

    def test_netflix_solve_2(self):
        """
        Test 2 to see if
        solving correctly
        """
        read = StringIO(
            "1:\n1\n2\n3\n4\n2:\n5")
        write = StringIO()
        actual_ratings = {1: {1: 2, 2: 3, 3: 4, 4: 3}, 2: {5: 1}}
        movie_cache = {'1': 3.7, '2': 1.75}
        movie_year_cache = {1: 1988, 2: 1975}
        cust_year_cache = {
            1: {1988: 1}, 2: {1988: 4.987}, 3: {1988: 5}, 4: {1988: 3}, 5: {1975: 3}}
        netflix_solve(read, write, actual_ratings,
                      movie_cache, movie_year_cache, cust_year_cache)
        self.assertEqual(
            write.getvalue(), "1:\n1.0\n5.0\n5.0\n3.0\n2:\n1.0\nRMSE: 1.09\n")

    def test_netflix_solve_3(self):
        """
        Test 3 to see if
        solving correctly
        """
        read = StringIO(
            "1:\n1\n2\n3\n4\n2:\n5")
        write = StringIO()
        actual_ratings = {1: {1: 2, 2: 3, 3: 4, 4: 3}, 2: {5: 1}}
        movie_cache = {'1': 4.5, '2': 2.1525}
        movie_year_cache = {1: 1988, 2: 1975}
        cust_year_cache = {
            1: {1988: 1}, 2: {1988: 4.987}, 3: {1988: 5}, 4: {1988: 3}, 5: {1975: 3}}
        netflix_solve(read, write, actual_ratings,
                      movie_cache, movie_year_cache, cust_year_cache)
        self.assertEqual(
            write.getvalue(), "1:\n1.8\n5.0\n5.0\n3.8\n2:\n1.5\nRMSE: 1.08\n")

    def test_netflix_solve_4(self):
        """
        Test 4 to see if
        solving correctly
        """
        read = StringIO(
            "1:\n1\n2\n3\n4\n2:\n5")
        write = StringIO()
        actual_ratings = {1: {1: 2, 2: 3, 3: 4, 4: 3}, 2: {5: 1}}
        movie_cache = {'1': 3.7, '2': 1.75}
        movie_year_cache = {1: 1988, 2: 1975}
        cust_year_cache = {1: {1988: 1.5}, 2: {1988: 2.5}, 3: {
            1988: 4.6}, 4: {1988: 2.9}, 5: {1975: 3.6}}
        netflix_solve(read, write, actual_ratings,
                      movie_cache, movie_year_cache, cust_year_cache)
        self.assertEqual(
            write.getvalue(), "1:\n1.5\n2.5\n4.6\n2.9\n2:\n1.6\nRMSE: 0.51\n")

    def test_netflix_solve_5(self):
        """
        Test 5 to see if
        solving correctly
        """
        read = StringIO(
            "1:\n1\n2\n3\n4\n2:\n5")
        write = StringIO()
        actual_ratings = {1: {1: 4, 2: 5, 3: 5, 4: 5}, 2: {5: 5}}
        movie_cache = {'1': 3.7, '2': 1.75}
        movie_year_cache = {1: 1988, 2: 1975}
        cust_year_cache = {1: {1988: 1.5}, 2: {1988: 2.5}, 3: {
            1988: 4.6}, 4: {1988: 2.9}, 5: {1975: 3.6}}
        netflix_solve(read, write, actual_ratings,
                      movie_cache, movie_year_cache, cust_year_cache)
        self.assertEqual(
            write.getvalue(), "1:\n1.5\n2.5\n4.6\n2.9\n2:\n1.6\nRMSE: 2.38\n")

    def test_netflix_solve_6(self):
        """
        Test 6 to see if
        solving correctly
        """
        read = StringIO(
            "1:\n1\n2\n3\n4\n2:\n5")
        write = StringIO()
        actual_ratings = {1: {1: 4, 2: 5, 3: 5, 4: 5}, 2: {5: 5}}
        movie_cache = {'1': 4.5, '2': 2.1525}
        movie_year_cache = {1: 1988, 2: 1975}
        cust_year_cache = {1: {1988: 2.5}, 2: {1988: 2.0}, 3: {
            1988: 4.3}, 4: {1988: 4.9}, 5: {1975: 3.9}}
        netflix_solve(read, write, actual_ratings,
                      movie_cache, movie_year_cache, cust_year_cache)
        self.assertEqual(
            write.getvalue(), "1:\n3.3\n2.8\n5.0\n5.0\n2:\n2.4\nRMSE: 1.57\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
