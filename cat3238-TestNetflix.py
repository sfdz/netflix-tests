#!/usr/bin/env python3

"""Unit Tests for Netflix.py"""

# -------
# imports
# -------

import os

from io       import StringIO
from unittest import main, TestCase

from contextlib import contextmanager
from pickle     import dump

from Netflix import (netflix_read, netflix_eval, netflix_load,
                     netflix_print, netflix_rmse, netflix_solve, pickle_load)


@contextmanager
def temp_pickle(data, name, path=''):
    """
    open/close temp filled pickle file
    data a blob of python data
    name a filename string
    path a path/dir string
    """
    filename = path + name
    with open(filename, "wb") as pickle_file:
        dump(data, pickle_file)
    yield
    os.remove(filename)

# -----------
# TestNetflix
# -----------
# pylint: disable=R0904
class TestNetflix(TestCase):
    """Unit Tests for Netflix.py"""
    # ----
    # read
    # ----

    def test_read_1(self):
        """Test netflix_read for a customer ID"""
        string = '123\n'
        data_id, data_type = netflix_read(string)
        self.assertEqual(data_id, 123)
        self.assertEqual(data_type, 'customer')

    def test_read_2(self):
        """Test netflix_read for a movie ID"""
        string = '123:\n'
        data_id, data_type = netflix_read(string)
        self.assertEqual(data_id, 123)
        self.assertEqual(data_type, 'movie')

    def test_read_3(self):
        """Test netflix_read for a string"""
        string = 'abc\n'
        error = False
        try:
            netflix_read(string)
        except ValueError:
            error = True
        self.assertTrue(error)

    # ------
    # pickle
    # ------

    def test_pickle_1(self):
        """Test pickle_load with array"""
        name = 'test_pickle_1.p'
        data_in = ['a', 'b', 'c']
        with temp_pickle(data_in, name):
            data_out = pickle_load(name, *['']*3)
            self.assertEqual(data_in, data_out)

    def test_pickle_2(self):
        """Test pickle_load with dict"""
        name = 'test_pickle_2.p'
        data_in = {'a': 1, 'b': 2, 'c': 3}
        with temp_pickle(data_in, name):
            data_out = pickle_load(name, *['']*3)
            self.assertEqual(data_in, data_out)

    def test_pickle_3(self):
        """Test pickle_load with int"""
        name = 'test_pickle_3.p'
        data_in = 123
        with temp_pickle(data_in, name):
            data_out = pickle_load(name, *['']*3)
            self.assertEqual(data_in, data_out)

    # ----
    # load
    # ----

    def test_load_1(self):
        """Test netflix_cache with pickle load"""
        files = ['total']
        data_in = [3.2281371945000967]
        data_out = netflix_load(files, [])
        self.assertEqual(data_in, data_out)

    def test_load_2(self):
        """Test netflix_cache with no pickle load"""
        data_in = [123]
        data_out = netflix_load('', data_in)
        self.assertEqual(data_in, data_out)

    # ----
    # rmse
    # ----

    def test_rmse_1(self):
        """Test netflix_rmse for correct prediction"""
        rmse = netflix_rmse([(1, 1), (5, 5)])
        self.assertEqual(rmse, 0.0)

    def test_rmse_2(self):
        """Test netflix_rmse for avg rating"""
        rmse = round(netflix_rmse([(3.2, 1), (3.2, 5)]), 2)
        self.assertEqual(rmse, 2.01)

    def test_rmse_3(self):
        """Test netflix_rmse for invalid input"""
        error = False
        try:
            netflix_rmse([(1,)])
        except ValueError:
            error = True
        self.assertTrue(error)


    # ----
    # eval
    # ----

    def test_eval_1(self):
        """Test netflix_eval"""
        rating, actual = netflix_eval(30878, 1)
        self.assertEqual(rating, 3.7255000228804325)
        self.assertEqual(actual, 4)

    def test_eval_2(self):
        """Test netflix_eval"""
        rating, actual = netflix_eval(1952305, 10)
        self.assertEqual(rating, 2.9539170532434964)
        self.assertEqual(actual, 3)

    def test_eval_3(self):
        """Test netflix_eval"""
        rating, actual = netflix_eval(1485175, 10012)
        self.assertEqual(rating, 3.782384142757868)
        self.assertEqual(actual, 3)

    def test_eval_4(self):
        """Test netflix_eval"""
        rating, actual = netflix_eval(430376, 10014)
        self.assertEqual(rating, 3.2289684823453744)
        self.assertEqual(actual, 3)

    # -----
    # print
    # -----

    def test_print_1(self):
        """Test netflix_print for an int"""
        writer = StringIO()
        netflix_print(writer, 10)
        self.assertEqual(writer.getvalue(), '10\n')

    def test_print_2(self):
        """Test netflix_print for a string"""
        writer = StringIO()
        netflix_print(writer, 'abc')
        self.assertEqual(writer.getvalue(), 'abc\n')

    def test_print_3(self):
        """Test netflix_print for 2 lines"""
        writer = StringIO()
        netflix_print(writer, 'abc\n123')
        self.assertEqual(writer.getvalue(), 'abc\n123\n')

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """Test netflix_solve"""
        reader = StringIO('1123:\n448549\n2444222\n1522889\n')
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), '1123:\n3.3\n2.9\n4.1\nRMSE: 0.4148335185443161\n')

    def test_solve_2(self):
        """Test netflix_solve"""
        reader = StringIO('1:\n1989766\n\n1989766\n')
        writer = StringIO()
        error = False
        try:
            netflix_solve(reader, writer)
        except ValueError:
            error = True
        self.assertTrue(error)

    def test_solve_3(self):
        """Test netflix_solve"""
        reader = StringIO('1:\n1989766\n')
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), '1:\n4.0\nRMSE: 0.0\n')

# ----
# main
# ----

if __name__ == "__main__":
    main()
