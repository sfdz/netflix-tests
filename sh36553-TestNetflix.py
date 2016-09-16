#!/usr/bin/env python3

"""
TestNetflix.py
    Tests Netflix.py for correct functionality
    Unit Testing
"""

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print
from Netflix import netflix_print_summary, netflix_solve, Caches

# -----------
# TestNetflix
# -----------


class TestNetflix(TestCase): #pylint: disable=R0904

    """
        Tests Netflix.py for correct functionality
        Unit Testing
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
            Tests read to see if it reads a movie line correctly
        """
        s_line = "1:\n"
        i, j = netflix_read(s_line)
        self.assertEqual(i, True)
        self.assertEqual(j, 1)

    def test_read_2(self):
        """
            Tests read to see if it reads a customer id correctly
        """
        s_line = "1564536453\n"
        i, j = netflix_read(s_line)
        self.assertEqual(i, False)
        self.assertEqual(j, 1564536453)

    def test_read_3(self):
        """
            Tests read to see if it reads a multidigit movie line correctly
        """
        s_line = "100253:\n"
        i, j = netflix_read(s_line)
        self.assertEqual(i, True)
        self.assertEqual(j, 100253)

    def test_print_1(self):
        """
            Tests print to see if prints a movie line correctly
        """
        writer = StringIO()
        netflix_print(writer, True, 2153330)
        self.assertEqual(writer.getvalue(), "2153330:\n")

    def test_print_2(self):
        """
            Tests print to see if prints a prediction line correctly
        """
        writer = StringIO()
        netflix_print(writer, False, 3.5)
        self.assertEqual(writer.getvalue(), "3.5\n")

    def test_print_3(self):
        """
            Tests print to see if prints a prediction line correctly
        """
        writer = StringIO()
        netflix_print(writer, False, 3.59648694869)
        self.assertEqual(writer.getvalue(), "3.6\n")

    def test_print_summary_1(self):
        """
            Tests print_summary to see if it calculates RMSE and total records
        """
        writer = StringIO()
        cache = Caches()
        cache.review_prediction_count = 1
        netflix_print_summary(writer, cache)
        self.assertEqual(writer.getvalue(), "RMSE: 0.00\n")

    def test_print_summary_2(self):
        """
            Tests print_summary to see if it calculates RMSE and
            total records with commas
        """
        writer = StringIO()
        cache = Caches()
        cache.rmse = 125000
        cache.review_prediction_count = 5000
        netflix_print_summary(writer, cache)
        self.assertEqual(writer.getvalue(), "RMSE: 5.00\n")

    def test_print_summary_3(self):
        """
            Tests print_summary to see if it calculates RMSE and
            total records with commas
        """
        writer = StringIO()
        cache = Caches()
        cache.rmse = 395803456.452523
        cache.review_prediction_count = 2135468
        netflix_print_summary(writer, cache)
        self.assertEqual(
            writer.getvalue(), "RMSE: 13.61\n")

    def test_eval_1(self):
        """
            Tests the predictions of the customer's rating of movie
        """
        cache = Caches()
        prediction = netflix_eval(864647, 3196, cache)
        self.assertEqual(prediction, 3.628994439391601)

    def test_eval_2(self):
        """
            Tests the predictions of the customer's rating of movie
            where prediction was less than 1
        """
        cache = Caches()
        prediction = netflix_eval(420915, 7120, cache)
        self.assertEqual(prediction, 1.0)

    def test_eval_3(self):
        """
            Tests the predictions of the customer's rating of movie
            where prediction was greater than 5
        """
        cache = Caches()
        prediction = netflix_eval(1007965, 4522, cache)
        self.assertEqual(prediction, 5.0)

    def test_solve_1(self):
        """
            Tests solve using test version
        """
        reader = StringIO("8191:\n2104692\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "8191:\n4.3\nRMSE: 0.31\n")

    def test_solve_2(self):
        """
            Tests solve using test version
        """
        reader = StringIO("8739:\n1484655\n16903:\n1060617\n942192\n1644088")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "8739:\n3.8\n16903:\n4.0\n4.0\n4.5\nRMSE: 0.70\n")

    def test_solve_3(self):
        """
            Tests solve using test version
        """
        reader = StringIO("8191:\n2104692\n430:\n433080\n1417709\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "8191:\n4.3\n430:\n3.7\n4.6\nRMSE: 0.49\n")

    # ----
    # caches
    # ----

    def test_caches_init_1(self):
        """
            Tests to see that Caches' review_prediction_count
            value is initialized to 0
        """
        cache = Caches()
        self.assertEqual(cache.review_prediction_count, 0)

    def test_caches_init_2(self):
        """
            Tests to see that Caches' rmse value is initialized to 0
        """
        cache = Caches()
        self.assertEqual(cache.rmse, 0)

    def test_caches_init_3(self):
        """
            Tests to see that Caches' test version has actual ratings
        """
        cache = Caches()
        self.assertEqual(cache.actual_ratings[2874][747972], 4)

    def test_caches_increment_count_1(self):
        """
            Tests to see that review_prediction_count is incremented by 1
        """
        cache = Caches()
        cache.increment_count()
        self.assertEqual(cache.review_prediction_count, 1)

    def test_caches_increment_count_2(self):
        """
            Tests to see that review_prediction_count is incremented by 1
        """
        cache = Caches()
        cache.review_prediction_count = 55
        cache.increment_count()
        self.assertEqual(cache.review_prediction_count, 56)

    def test_caches_increment_count_3(self):
        """
            Tests to see that review_prediction_count is incremented by 1
        """
        cache = Caches()
        cache.review_prediction_count = -1
        cache.increment_count()
        self.assertEqual(cache.review_prediction_count, 0)

    def test_caches_increment_rmse_1(self):
        """
            Tests to see that rmse is incremented by the value provided
        """
        cache = Caches()
        cache.increment_rmse(0.2335785)
        self.assertEqual(cache.rmse, 0.2335785)

    def test_caches_increment_rmse_2(self):
        """
            Tests to see that rmse is incremented by the value provided
        """
        cache = Caches()
        cache.rmse = 25
        cache.increment_rmse(-2.6)
        self.assertEqual(cache.rmse, 22.4)

    def test_caches_increment_rmse_3(self):
        """
            Tests to see that rmse is incremented by the value provided
        """
        cache = Caches()
        cache.rmse = -1
        cache.increment_rmse(0)
        self.assertEqual(cache.rmse, -1)

# ----
# main
# ----

if __name__ == "__main__":
    main()
