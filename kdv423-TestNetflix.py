#!/usr/bin/env python3

import pickle
from io import StringIO
from unittest import main, TestCase
from Netflix import rate, rmse, printmovie, printrmse, solve

#------------
# TestNetflix
#------------

class TestNetflix(TestCase):

    #-----
    # rmse
    #-----

    def test_rmse_1(self):
        expected = [1, 2, 3, 4]
        actual = [1, 2, 3, 4]
        result = rmse(expected, actual)
        self.assertEqual(result, 0)

    def test_rmse_2(self):
        expected = [1, 2, 3, 4]
        actual = [2, 3, 4, 5]
        result = rmse(expected, actual)
        self.assertEqual(result, 1)

    def test_rmse_3(self):
        expected = [1, 2, 3]
        actual = [2, 3, 3]
        result = rmse(expected, actual)
        self.assertEqual(result, .82)

    #-----
    # rate
    #-----

    def test_rate_1(self):
        movieratings = {1: 1}
        customeraverages = 1
        totaverage = 1
        result = rate(1, movieratings, customeraverages, totaverage)
        self.assertEqual(result, 3)

    def test_rate_2(self):
        movieratings = {1: 1}
        customeraverages = 2
        totaverage = 1
        result = rate(1, movieratings, customeraverages, totaverage)
        self.assertEqual(result, 4)

    def test_rate_3(self):
        movieratings = {1: 1}
        customeraverages = 3
        totaverage = 1
        result = rate(1, movieratings, customeraverages, totaverage)
        self.assertEqual(result, 5)

    #-----------
    # printmovie
    #-----------

    def test_printmovie_1(self):
        fout = StringIO()
        movie = '1123'
        ratings = [1, 2, 3]
        printmovie(fout, movie, ratings)
        self.assertEqual(fout.getvalue(), '1123:\n1.0\n2.0\n3.0\n')

    def test_printmovie_2(self):
        fout = StringIO()
        movie = '1123'
        ratings = [1.234, 2, 3]
        printmovie(fout, movie, ratings)
        self.assertEqual(fout.getvalue(), '1123:\n1.2\n2.0\n3.0\n')

    def test_printmovie_3(self):
        fout = StringIO()
        movie = '1123'
        ratings = [1.47, 2, 3]
        printmovie(fout, movie, ratings)
        self.assertEqual(fout.getvalue(), '1123:\n1.5\n2.0\n3.0\n')

    def test_printmovie_4(self):
        fout = StringIO()
        movie = '1123'
        ratings = [1.47, 2.12, 3]
        printmovie(fout, movie, ratings)
        self.assertEqual(fout.getvalue(), '1123:\n1.5\n2.1\n3.0\n')

    #----------
    # printrmse
    #----------

    def test_printrmse_1(self):
        fout = StringIO()
        num = 1.00
        printrmse(fout, num)
        self.assertEqual(fout.getvalue(), 'RMSE: 1.00\n')

    def test_printrmse_2(self):
        fout = StringIO()
        num = .01
        printrmse(fout, num)
        self.assertEqual(fout.getvalue(), 'RMSE: 0.01\n')

    def test_printrmse_3(self):
        fout = StringIO()
        num = .235
        printrmse(fout, num)
        self.assertEqual(fout.getvalue(), 'RMSE: 0.23\n')

    def test_printrmse_4(self):
        fout = StringIO()
        num = .958
        printrmse(fout, num)
        self.assertEqual(fout.getvalue(), 'RMSE: 0.96\n')

    #------
    # solve
    #------

    def test_solve_1(self):
        fout = StringIO()
        fin = StringIO('1:\n1')
        movieratings = {1: 1}
        customeraverages = {1: {1: 1}}
        actual = {1: {1: 1}}
        totaverage = 1
        movieyears = {1: 1}
        solve(fin, fout, actual, movieratings, customeraverages, totaverage, movieyears)
        self.assertEqual(fout.getvalue(), '1:\n3.0\nRMSE: 2.00\n')

#-----
# main
#-----

if __name__ == '__main__':
    main()
