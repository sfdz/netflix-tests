#!/usr/bin/env python3
"""
Tests Netflix.py
"""

# pylint: disable=missing-docstring, invalid-name

from io import StringIO
from unittest import main, TestCase
from Netflix import netflix_init_caches, netflix_read, netflix_predict, \
    netflix_calc_rmse, netflix_print, netflix_solve


class TestNetflix(TestCase):

    @classmethod
    def setUpClass(cls):
        actual = {10: {1: 1, 2: 2}, 11: {3: 3, 4: 4, 5: 5}}
        movie_avg = {10: 4, 11: 5}
        cust_avg_dev = {1: -1.0, 2: -0.5, 3: 0.0, 4: 0.5, 5: 1.0}
        netflix_init_caches(actual, movie_avg, cust_avg_dev)

    def test_read_1(self):
        s = '1:\n1\n'.split()
        mcr = netflix_read(s)
        self.assertEqual(mcr, {1: {1: -1}})

    def test_read_2(self):
        s = '1:\n1\n2:\n2\n'.split()
        mcr = netflix_read(s)
        self.assertEqual(mcr, {1: {1: -1}, 2: {2: -1}})

    def test_read_3(self):
        s = '1:\n1\n2\n'.split()
        mcr = netflix_read(s)
        self.assertEqual(mcr, {1: {1: -1, 2: -1}})

    def test_read_4(self):
        s = '10:\n1\n2\n11:\n3\n4\n5\n'.split()
        mcr = netflix_read(s)
        self.assertEqual(mcr, {10: {1: -1, 2: -1}, 11: {3: -1, 4: -1, 5: -1}})

    def test_predict_1(self):
        r = netflix_predict(10, 3)
        self.assertEqual(r, 4.0)

    def test_predict_2(self):
        r = netflix_predict(10, 1)
        self.assertEqual(r, 3.0)

    def test_predict_3(self):
        r = netflix_predict(10, 4)
        self.assertEqual(r, 4.5)

    def test_predict_4(self):
        r = netflix_predict(11, 2)
        self.assertEqual(r, 4.5)

    def test_calc_rmse_1(self):
        mcr = {10: {1: 1}}
        rmse = netflix_calc_rmse(mcr)
        self.assertEqual(rmse, 0.0)

    def test_calc_rmse_2(self):
        mcr = {10: {1: 2}}
        rmse = netflix_calc_rmse(mcr)
        self.assertEqual(rmse, 1.0)

    def test_calc_rmse_3(self):
        mcr = {10: {2: 1}}
        rmse = netflix_calc_rmse(mcr)
        self.assertEqual(rmse, 1.0)

    def test_calc_rmse_4(self):
        mcr = {11: {3: 1, 4: 2, 5: 3}}
        rmse = netflix_calc_rmse(mcr)
        self.assertEqual(rmse, 2.0)

    def test_calc_rmse_5(self):
        mcr = {10: {1: 1, 2: 2}, 11: {3: 3, 5: 1}}
        rmse = netflix_calc_rmse(mcr)
        self.assertEqual(rmse, 2.0)

    def test_print_1(self):
        w = StringIO()
        mcr = {1: {1: 1}}
        netflix_print(w, mcr, 0.0)
        self.assertEqual(w.getvalue(), "1:\n1.0\nRMSE: 0.00\n")

    def test_print_2(self):
        w = StringIO()
        mcr = {1: {1: 1}}
        netflix_print(w, mcr, 2.61)
        self.assertEqual(w.getvalue(), "1:\n1.0\nRMSE: 2.61\n")

    def test_print_3(self):
        w = StringIO()
        mcr = {1: {1: 1, 2: 2}}
        netflix_print(w, mcr, 0.0)
        self.assertEqual(w.getvalue(), "1:\n1.0\n2.0\nRMSE: 0.00\n")

    def test_print_4(self):
        w = StringIO()
        mcr = {1: {1: 1, 2: 2}, 2: {1: 3, 2: 4, 3: 5}}
        netflix_print(w, mcr, 0.0)
        self.assertEqual(
            w.getvalue(), "1:\n1.0\n2.0\n2:\n3.0\n4.0\n5.0\nRMSE: 0.00\n")

    def test_solve_1(self):
        s = '10:\n1\n'.split()
        w = StringIO()
        netflix_solve(s, w)
        self.assertEqual(w.getvalue(), "10:\n3.0\nRMSE: 2.00\n")

    def test_solve_2(self):
        s = '10:\n1\n2\n11:\n3\n4\n5\n'.split()
        w = StringIO()
        netflix_solve(s, w)
        self.assertEqual(
            w.getvalue(), "10:\n3.0\n3.5\n11:\n5.0\n5.5\n6.0\nRMSE: 1.64\n")


if __name__ == "__main__":
    main()
