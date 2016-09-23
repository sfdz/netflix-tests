#!/usr/bin/env python3

# TestNetflix.py

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import parse_movies, rmse, predict_rating, predict_all

# -----------
# TestCollatz
# -----------


class TestNetflix(TestCase):
    # ------------
    # parse_movies
    # ------------

    def test_parse_movies_1(self):
        s = StringIO("1:\n532\n68934\n32\n2:\n48\n2\n")
        movie_list = parse_movies(s)
        expected = {'1': ['532', '68934', '32'], '2': ['48', '2']}
        self.assertEqual(movie_list, expected)

    def test_parse_movies_2(self):
        s = StringIO("3:\n  55\n 1234\n222\n 4:\n555\n666\n777\n ")
        movie_list = parse_movies(s)
        expected = {'3': ['55', '1234', '222'], '4': ['555', '666', '777']}
        self.assertEqual(movie_list, expected)

    def test_parse_movies_3(self):
        s = StringIO("e:\n 8912\n 34\n 5:\n67\nd\n32\n")
        movie_list = parse_movies(s)
        expected = {'5': ['67', '32']}
        self.assertEqual(movie_list, expected)
    # ----
    # rmse
    # ----

    def test_rmse_1(self):
        actual = {1: {1: 3, 2: 4, 3: 3}}
        prediction = {1: {1: 3, 2: 4, 3: 3}}
        self.assertEqual(rmse(actual, prediction), '0.00')

    def test_rmse_2(self):
        actual = {1: {1: 2, 2: 3, 3: 4}}
        prediction = {1: {1: 4, 2: 1, 3: 7}}
        self.assertEqual(rmse(actual, prediction), "2.38")

    def test_rmse_3(self):
        actual = {1: {1: 2, 2: 3, 3: 4}}
        prediction = {1: {1: 3, 2: 2, 3: 5}}
        self.assertEqual(rmse(actual, prediction), "1.00")
    # --------------
    # predict_rating
    # --------------

    def test_predict_rating_1(self):
        rating = predict_rating(1, 4, 4)
        self.assertEqual(rating, 3)

    def test_predict_rating_2(self):
        rating = predict_rating(10, 1, 1)
        self.assertEqual(rating, 4)

    def test_predict_rating_3(self):
        rating = predict_rating(3, 6, 3)
        self.assertEqual(rating, 4)

    # -----------
    # predict_all
    # -----------
    def test_predict_all_1(self):
        r = StringIO("1:\n14756\n1059319\n470861\n")
        w = StringIO()
        predict_all(r, w)
        result = "1:\n3.69\n3.14\n4.29\nRMSE: 0.46"
        self.assertEqual(w.getvalue(), result)

    def test_predict_all_2(self):
        r = StringIO("10:\n1952305\n1531863\n")
        w = StringIO()
        predict_all(r, w)
        result = "10:\n3.29\n3.19\nRMSE: 0.25"
        self.assertEqual(w.getvalue(), result)

    def test_predict_all_3(self):
        r = StringIO("10001:\n262828\n2609496\n1474804\n")
        w = StringIO()
        predict_all(r, w)
        result = "10001:\n3.64\n4.13\n3.63\nRMSE: 0.31"
        self.assertEqual(w.getvalue(), result)
# ----
# main
# ----

if __name__ == "__main__":
    main()
