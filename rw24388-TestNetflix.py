"""
TestCollatz.py
"""
#!usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_solve, netflix_eval

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    Test cases for Netflix.py
    """
    # ----
    # read
    # ----

    def test_solve1(self):
        """
        testing netflix_solve
        """
        read = StringIO("1:\n30878\n2647871\n1283744\n")
        write = StringIO()
        netflix_solve(read, write)
        self.assertEqual(write.getvalue(), "1:\n3.7\n3.0\n3.9\nRMSE: 0.79\n")

    def test_solve2(self):
        """
        testing netflix_solve
        10:
        1952305
        1531863
        1000:
        2326571
        977808
        """
        read = StringIO("10:\n1952305\n1531863\n1000:\n2326571\n977808\n")
        write = StringIO()
        netflix_solve(read, write)
        self.assertEqual(write.getvalue(), "10:\n3.1\n3.0\n1000:\n3.8\n2.4\nRMSE: 0.49\n")

    def test_solve3(self):
        """
        testing netflix_solve
        10004:
        1737087
        1270334
        1262711
        10005:
        254775
        1892654
        10006:
        1093333
        """
        read = StringIO("10004:\n1737087\n1270334\n1262711\n10005:\n254775\n1892654\n")
        write = StringIO()
        netflix_solve(read, write)
        self.assertEqual(write.getvalue(), "10004:\n5.4\n4.7\n4.2\n10005:\n3.3\n4.8\nRMSE: 1.24\n")

    def test_eval1(self):
        """
        testing netflix_eval
        """
        cust_average = 3.2
        movie_average = 3.4
        average_for_year = -.2
        result = netflix_eval(cust_average, movie_average, average_for_year)
        self.assertEqual(round(result, 1), 3.1)

    def test_eval2(self):
        """
        testing netflix_eval
        """
        cust_average = 4.1
        movie_average = 2.9
        average_for_year = .4
        result = netflix_eval(cust_average, movie_average, average_for_year)
        self.assertEqual(round(result, 1), 3.9)

    def test_eval3(self):
        """
        testing netflix_eval
        """
        cust_average = 2.6
        movie_average = 1.7
        average_for_year = .6
        result = netflix_eval(cust_average, movie_average, average_for_year)
        self.assertEqual(round(result, 1), 2.8)



# ----
# main
# ----

if __name__ == "__main__":
    main()