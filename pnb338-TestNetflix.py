#!/usr/bin/env python3

# -------------------------------
# projects/netflix/TestNetflix.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""
Unit tests for Netflix
"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_rmse, netflix_predict, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix(TestCase):
    """
    run unit tests on Netflix
    """

    # ----
    # rmse
    # ----

    def test_rmse_1(self):
        """
        test rmse of dicts with equal rating
        """
        predictions = {1 : {1 : 3}}
        actual_ratings = {1 : {1 : 3}}
        rmse = netflix_rmse(predictions, actual_ratings)
        self.assertEqual(rmse, 0)

    def test_rmse_2(self):
        """
        test rmse of dicts with different ratings
        """
        predictions = {2 : {2 : 3}}
        actual_ratings = {2 : {2 : 4}}
        rmse = netflix_rmse(predictions, actual_ratings)
        self.assertEqual(rmse, 1)

    def test_rmse_3(self):
        """
        test rmse of dicts with different ratings
        """
        predictions = {3 : {3 : 5}}
        actual_ratings = {3 : {3 : 1}}
        rmse = netflix_rmse(predictions, actual_ratings)
        self.assertEqual(rmse, 4)

    def test_rmse_4(self):
        """
        test rmse of two movies with one rating each
        """
        predictions = {4 : {4 : 3}, 5 : {5 : 3}}
        actual_ratings = {4 : {4 : 5}, 5 : {5 : 2}}
        rmse = round(netflix_rmse(predictions, actual_ratings), 2)
        self.assertEqual(rmse, 1.58)

    # -------
    # predict
    # -------

    def test_predict_1(self):
        """
        test reading of our dict and the pickle dicts
        """
        movie = 1
        customer = 30878
        predict_dict = {movie : {}}
        prediction = netflix_predict(predict_dict, movie, customer)
        self.assertEqual(prediction, 3.7)

    def test_predict_2(self):
        """
        test reading of our dict and the pickle dicts
        """
        movie = 10
        customer = 1952305
        predict_dict = {movie : {}}
        prediction = netflix_predict(predict_dict, movie, customer)
        self.assertEqual(prediction, 2.91)

    def test_predict_3(self):
        """
        test reading of our dict and the pickle dicts
        """
        movie = 10001
        customer = 262828
        predict_dict = {movie : {}}
        prediction = netflix_predict(predict_dict, movie, customer)
        self.assertEqual(prediction, 3.42)

    def test_predict_4(self):
        """
        test reading of our dict and the pickle dicts
        """
        movie = 10011
        customer = 1624701
        predict_dict = {movie : {}}
        prediction = netflix_predict(predict_dict, movie, customer)
        self.assertEqual(prediction, 4.42)

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        test netflix_solve
        """
        reader = StringIO("1:\n30878\n548064\n10:\n1952305\n1531863\n")
        output = StringIO()
        netflix_solve(reader, output)
        self.assertEqual(output.getvalue(), "1:\n3.70\n3.54\n10:\n2.91\n2.66\nRMSE: 0.77\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
