#!/usr/bin/env python3
""" Run as __main__ to do unit testing. """

from io import StringIO
from itertools import zip_longest
import pickle
from unittest import main, TestCase
import Netflix as nfx

class TestNetflix(TestCase):
    """
    This class defines unit tests for Netflix
    as instance methods.
    """

    #netflix_read
    def test_read_customer_1200(self):
        line = "1200"
        movie_id, customer_id = nfx.netflix_read(line)
        self.assertIsNone(movie_id)
        self.assertEqual(customer_id, 1200)

    def test_read_customer_2649429(self):
        line = "2649429"
        movie_id, customer_id = nfx.netflix_read(line)
        self.assertIsNone(movie_id)
        self.assertEqual(customer_id, 2649429)

    def test_read_movie_100000(self):
        line = "100000:"
        movie_id, customer_id = nfx.netflix_read(line)
        self.assertEqual(movie_id, 100000)
        self.assertIsNone(customer_id)

    #netflix_print
    def test_print_score_5_0(self):
        out = StringIO()
        score = 5.0
        nfx.netflix_print(out, score=score)
        self.assertEqual(out.getvalue(), "5.0\n")

    def test_print_movie_12345(self):
        out = StringIO()
        movie = 12345
        nfx.netflix_print(out, movie_id=movie)
        self.assertEqual(out.getvalue(), "12345:\n")

    def test_print_rmse_0_333(self):
        out = StringIO()
        rmse = 0.333
        nfx.netflix_print(out, rmse=rmse)
        self.assertEqual(out.getvalue(), "RMSE: 0.33\n")

    #netflix_run
    def test_run_1(self):
        """
        Test netflix_run with input:

        17770:
        533482
        54864
        10000:
        523108
        200206
        """
        ids = "17770:\n533482\n54864\n10000:\n523108\n200206\n"
        reader = StringIO(ids)
        writer = StringIO()
        nfx.netflix_run(reader, writer)

        in_lines = ids.split()
        out_lines = writer.getvalue().split()
        rmse = out_lines[-2:]
        with self.subTest(rmse=out_lines[-2:]):
            self.assertTrue(rmse[0] == "RMSE:")
            self.assertTrue(float(rmse[1]) < 1.0)
        out_lines = out_lines[:-2]
        for id_in, output in zip_longest(in_lines, out_lines, fillvalue=None):
            with self.subTest(id_in=id_in, output=output):
                self.assertTrue(TestNetflix.matches(id_in, output))

    @staticmethod
    def matches(id_in, output):
        """
        Check if an id is matched to the correct to the output.
        A movie id should be copied exactly in the output.
        A customer id should yield a float in the range [1.0, 5.0].

        id_in  a str id of either a movie or customer
        output the str output for id_in
        """
        if id_in is None or output is None:
            return False
        if id_in.endswith(":") and id_in == output:
            return True
        if not id_in.endswith(":") and 1.0 <= float(output) <= 5.0:
            return True
        return False

if __name__ == "__main__":
    PREFIX = "/u/downing/cs/netflix-cs373/"
    nfx.ACTUAL = pickle.load(open(PREFIX + "cat3238-actual.p", "rb"))
    nfx.MOVIE_AVG = pickle.load(open(PREFIX + "jic539_movie_avg.p", "rb"))
    nfx.MOVIE_YEAR = pickle.load(open(PREFIX + "cat3238-years.p", "rb"))
    nfx.CUSTOMER_YEAR = pickle.load(open(PREFIX + "cat3238-customer.p", "rb"))
    main()
