#!/usr/bin/env python3

"""
module to test Netflix.py
"""

from io import StringIO
from unittest import main, TestCase
from Netflix import (netflix_predict, netflix_solve)

# -----------
# TestNetflix
# -----------


class TestNetflix(TestCase):

    """
    class to Netflix.py
    """

    # -----
    # predict
    # -----

    def test_predict_1(self):
        """
        test predictions
        """
        test_prediction = netflix_predict(1916275, 2000, 3.51)
        self.assertTrue(abs(test_prediction - 3) < 1)

    def test_predict_2(self):
        """
        test predictions
        """
        test_prediction = netflix_predict(2338807, 2003, 3.53)
        self.assertTrue(abs(test_prediction - 4) < 1)

    def test_predict_3(self):
        """
        test predictions
        """
        test_prediction = netflix_predict(845452, 2004, 4.1)
        self.assertTrue(abs(test_prediction - 4) < 1)

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        test solve
        """
        reader = StringIO("1:\n30878\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1:\n3.7\nRMSE: 0.3\n")

    def test_solve_2(self):
        """
        test solve
        """
        reader = StringIO("7240:\n420661\n1355247\n1453495\n282169\n2535515\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "7240:\n3.2\n3.7\n3.9\n3.8\n4.1\nRMSE: 0.44\n")

    def test_solve_3(self):
        """
        test solve
        """
        reader = StringIO("12399:\n1523893\n1143571\n2118117\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "12399:\n3.1\n4.3\n3.3\nRMSE: 0.77\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
