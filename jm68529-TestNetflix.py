"""
Module that runs unittest on Netflix
"""
import math
from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_print, netflix_find_rating, \
     netflix_solve, calculate_rmse

# pylint: disable=C0111
# pylint: disable=R0904


class TestNetflix(TestCase):

    # ----
    # read
    # ----
    def test_read1(self):
        reader = StringIO("123:\n2\n3\n4\n")
        movies = netflix_read(reader)
        self.assertIsNotNone(movies[123])
        self.assertEqual(movies[123], [2, 3, 4])

    def test_read2(self):
        reader = StringIO("123:\n2009\n384\n4\n")
        movies = netflix_read(reader)
        self.assertIsNotNone(movies[123])
        self.assertEqual(movies[123], [2009, 384, 4])

    def test_read3(self):
        reader = StringIO("14756:\n1027056\n1149588\n1394012\n1406595\n")
        movies = netflix_read(reader)
        self.assertIsNotNone(movies[14756])
        self.assertEqual(movies[14756], [1027056, 1149588, 1394012, 1406595])

    def test_read4(self):
        reader = StringIO("")
        self.assertRaises(AssertionError, netflix_read, reader)

    # ----
    # print
    # ----
    def test_print1(self):
        writer = StringIO()
        self.assertRaises(AssertionError, netflix_print, writer, {}, 1.0)

    def test_print2(self):
        writer = StringIO()
        ratings = {123: [(2009, 5), (384, 2), (4, 1)]}
        netflix_print(writer, ratings, 0.926364526016373)
        self.assertEqual(writer.getvalue(), "123:\n5\n2\n1\nRMSE: 0.93\n")

    def test_print3(self):
        writer = StringIO()
        ratings = {123: [(2009, 5), (384, 2), (4, 1)]}
        self.assertRaises(AssertionError, netflix_print, writer, ratings, -1)

    # -----------
    # find_rating
    # -----------
    def test_find_rating1(self):
        movies = {10010: [52050, 650466, 2224061]}
        ratings = netflix_find_rating(movies)
        self.assertEqual(ratings,
                         {10010: [(52050, 2), (650466, 2), (2224061, 3)]})

    def test_find_rating2(self):
        self.assertRaises(AssertionError, netflix_find_rating, {})

    def test_find_rating3(self):
        movies = {10010: [52050, 650466, 2224061], 10: [1531863]}
        ratings = netflix_find_rating(movies)
        self.assertEqual(ratings,
                         {10010: [(52050, 2), (650466, 2), (2224061, 3)],
                          10: [(1531863, 3)]})


    # -----
    # solve
    # -----

    def test_solve1(self):
        reader = StringIO("")
        writer = StringIO()
        self.assertRaises(AssertionError, netflix_solve, reader, writer)

    # pylint: disable=C0301
    def test_solve2(self):
        reader = StringIO("1:\n30878\n2647871\n1283744\n" +
                          "10:\n1952305\n1531863\n1000:\n2326571\n977808\n1010534")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "1:\n3\n3\n4\n10:\n3\n3\n1000:\n3\n2\n2\nRMSE: 0.71\n")

    def test_solve3(self):
        reader = StringIO("1:\n30878\n2647871\n1283744\n")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1:\n3\n3\n4\nRMSE: 1.00\n")

    # ----
    # rmse
    # ----
    def test_calculate_rmse1(self):
        ratings = {17770: [(54864, 3), (1196966, 1), (2334295, 2)]}
        rmse = calculate_rmse(ratings)
        self.assertEqual(rmse, math.sqrt(2))

    def test_calculate_rmse2(self):
        ratings = {17770: [(54864, 1), (1196966, 2), (2334295, 3)]}
        rmse = calculate_rmse(ratings)
        self.assertEqual(rmse, 0)

    def test_calculate_rmse3(self):
        self.assertRaises(AssertionError, calculate_rmse, {})

if __name__ == "__main__":  # pragma: no cover
    main()
