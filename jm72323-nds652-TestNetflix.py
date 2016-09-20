#!/usr/bin/env python3

"""
Test Harness for Netflix
"""

from io import StringIO
from unittest import main, TestCase
from Netflix import netflix_eval, netflix_print, netflix_solve, calc_rmse


class TestNetflix(TestCase):

    """Test class to test the methods in Netflix.py file"""

    def test_print_0(self):
        """ Test the printing functionallity in Netflix.py """
        writer = StringIO()
        netflix_print(
            writer, "1", {30878: 1, 2647871: 2, 123744: 3}, [30878, 2647871, 123744])
        self.assertEqual(writer.getvalue(), "1:\n1\n2\n3\n")

    def test_print_1(self):
        """ Test the printing functionallity in Netflix.py """
        writer = StringIO()
        netflix_print(
            writer, "150", {123: 5, 456: 2, 938: 1, 9999: 0}, [9999, 938, 456, 123])
        self.assertEqual(writer.getvalue(), "150:\n0\n1\n2\n5\n")

    def test_print_2(self):
        """ Test the printing functionallity in Netflix.py """
        writer = StringIO()
        netflix_print(writer, "5", {53: 3, 827: 2, 128: 4}, [827, 128, 53])
        self.assertEqual(writer.getvalue(), "5:\n2\n4\n3\n")

    def test_eval_0(self):
        """
        Movie id: 1
        customer: 30878 rating: 4
        customer: 2647871 rating: 4
        customer: 1283744 rating: 3
        customer: 2488120 rating: 5
        customer: 317050 rating: 5
        customer: 1904905 rating: 4
        customer: 1989766 rating: 4
        customer: 14756 rating: 4
        """
        movie_id = 1
        customer_ids = [30878, 2647871, 1283744,
                        2488120, 317050, 1904905, 1989766, 14756]
        predicted = netflix_eval(movie_id, customer_ids)
        expected = {30878: 3.7, 2647871: 3.2, 1283744: 4.0, 2488120:
                    4.7, 317050: 4.9, 1904905: 4.0, 1989766: 4.0, 14756: 4.0}
        self.assertEqual(predicted, expected)

    def test_eval_1(self):
        """
        Movie id: 10
        customer: 1952305 rating: 3
        customer: 1531863 rating: 3
        """
        movie_id = 10
        customer_ids = [1952305, 1531863]
        predicted = netflix_eval(movie_id, customer_ids)
        expected = {1952305: 3.0, 1531863: 3.0}
        self.assertEqual(predicted, expected)

    def test_eval_2(self):
        """
        Movie id: 1000
        customer: 2326571 rating: 3
        customer: 977808 rating: 3
        customer: 1010534 rating: 2
        customer: 1861759 rating: 5
        customer: 79755 rating: 5
        customer: 98259 rating: 5
        customer: 1960212 rating: 2
        """
        movie_id = 1000
        customer_ids = [2326571, 977808, 1010534, 1861759, 79755, 1960212]
        predicted = netflix_eval(movie_id, customer_ids)
        expected = {2326571: 3.6, 977808: 2.4, 1010534:
                    2.0, 1861759: 5.1, 79755: 3.9, 1960212: 2.0}
        self.assertEqual(predicted, expected)

    def test_solve_0(self):
        """
        two movies, multiple users per movie
        """
        string = "1:\n30878\n14756\n10:\n1952305\n1531863"
        writer = StringIO()
        reader = StringIO(string)
        netflix_solve(reader, writer)
        result = writer.getvalue()
        last_line = ""
        counter = 0
        result = result.split("\n")
        for line in result:
            last_line = line
            counter += 1
        actual = last_line.replace("RMSE: ", "").replace("\n", "")
        comparison = float(actual) < 1.0
        self.assertEqual(counter, len(string.split("\n")) + 1)
        self.assertTrue(comparison)

    def test_solve_1(self):
        """
        one movie, multiple users
        """
        string = "1:\n30878\n14756"
        writer = StringIO()
        reader = StringIO(string)
        netflix_solve(reader, writer)
        result = writer.getvalue()
        last_line = ""
        counter = 0
        result = result.split("\n")
        for line in result:
            last_line = line
            counter += 1
        actual = last_line.replace("RMSE: ", "").replace("\n", "")
        comparison = float(actual) < 1.0
        self.assertEqual(counter, len(string.split("\n")) + 1)
        self.assertTrue(comparison)

    def test_solve_2(self):
        """
        More movies, multiple users per movie
        """
        string = "1:\n30878\n14756\n10:\n1952305\n1531863\n1000:\n2326571\n977808"
        writer = StringIO()
        reader = StringIO(string)
        netflix_solve(reader, writer)
        result = writer.getvalue()
        last_line = ""
        counter = 0
        result = result.split("\n")
        for line in result:
            last_line = line
            counter += 1
        actual = last_line.replace("RMSE: ", "").replace("\n", "")
        comparison = float(actual) < 1.0
        self.assertEqual(counter, len(string.split("\n")) + 1)
        self.assertTrue(comparison)

    def test_calc_rmse_0(self):
        """ Test with one movie and multiple users """
        big_dict = {1: {30878: 3, 14756: 3}}
        actual = calc_rmse(big_dict)
        expected = (2 / 2) ** (1 / 2)
        self.assertEqual(actual, expected)

    def test_calc_rmse_1(self):
        """ Test with one movie and more users """
        big_dict = {1: {2647871: 3, 1283744: 3, 2488120: 3}}
        actual = calc_rmse(big_dict)
        expected = (5 / 3) ** (1 / 2)
        self.assertEqual(actual, expected)

    def test_calc_rmse_2(self):
        """ Test with multiple movies and multiple users """
        big_dict = {
            1000: {2326571: 3, 977808: 3, 1010534: 3, 1861759: 3}, 1: {30878: 3, 14756: 3}}
        actual = calc_rmse(big_dict)
        expected = (7 / 6) ** (1 / 2)
        self.assertEqual(actual, expected)

    def test_calc_rmse_3(self):
        """ Test with multiple movies and multiple users """
        big_dict = {
            1000: {
                2553920: 3.3, 2326571: 3.3, 1900790: 3.3, 1959111: 3.4, 79755: 3.5, 977808: 3.2,
                2623506: 3.3, 98259: 3.4, 1960212: 3.3, 1580442: 3.0, 100291: 3.3, 708895: 3.3,
                2368043: 3.3, 2409123: 3.1, 1010534: 3.1, 906984: 3.5, 537705: 3.7, 1196779: 3.5,
                433455: 3.6, 929584: 3.6, 506737: 3.3, 97460: 3.6, 2251189: 3.3, 2411446: 3.4,
                1002296: 3.6, 809597: 3.4, 1861759: 3.8},
            1: {548064: 3.5, 1406595: 3.5, 1989766: 3.4, 1904905: 3.6, 2529547: 3.6, 470861: 3.8,
                2488120: 3.9, 1149588: 3.5, 1394012: 3.3, 30878: 3.5, 1774623: 3.5, 1283744: 3.5,
                2380848: 4.0, 712610: 3.7, 14756: 3.5, 1772839: 3.7, 1027056: 3.6, 2603381: 3.6,
                1059319: 3.3, 1682104: 3.6, 317050: 3.5, 2625019: 3.2, 2647871: 3.4},
            10: {1952305: 3.2, 1531863: 3.2}}
        actual = calc_rmse(big_dict)
        expected = (50.97 / 52) ** (1 / 2)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
