#!/usr/bin/env python3

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

from Netflix import netflix_solve

# -----------
# TestCollatz
# -----------


class TestNetflix(TestCase):
    # ------------
    # place_holder
    # ------------

    def test_netflix_solve_1(self):
        r = StringIO("13:\n615010\n1860468\n2131832\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "13:\n4.1\n4.7\n4.4\nRMSE: 0.62")

    def test_netflix_solve_2(self):
        r = StringIO("39:")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "39:\nRMSE: 0.00")

    def test_netflix_solve_3(self):
        r = StringIO("13:\n615010\n1860468\n2131832\n39:\n877184\n1013648\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(
            w.getvalue(), "13:\n4.1\n4.7\n4.4\n39:\n3.0\n2.8\nRMSE: 0.67")

# ----
# main
# ----

if __name__ == "__main__":
    main()
