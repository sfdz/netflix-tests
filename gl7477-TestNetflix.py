""" Guande Lyu & Lei Lin """
#!/usr/bin/envalpython3

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase
from Netflix import netflix_caching, netflix_read, netflix_eval
from Netflix import netflix_print, sqrt_diff, netflix_rmse, netflix_solve


# -----------
# TestNetflix
# -----------

class TestNetflix(TestCase): #pylint: disable=R0904

    """ test netflix """

    # ----
    # netflix_caching
    # ----

    def test_netflix_caching_1(self):
        """ test test_netflix_caching_1 """
        avg_cust_rating = {}
        avg_movie_rating = {}
        actual_rating = {}
        actual_rating, avg_cust_rating, avg_movie_rating = netflix_caching(
            actual_rating, avg_cust_rating, avg_movie_rating)
        self.assertEqual(actual_rating[2043][1417435], 3)
        self.assertEqual(actual_rating[2043][2312054], 1)
        self.assertEqual(actual_rating[2043][462685], 4)
        self.assertEqual(avg_cust_rating['386454'], 4.78)
        self.assertEqual(avg_cust_rating['670698'], 3.69)
        self.assertEqual(avg_cust_rating['1924134'], 3.4)
        self.assertEqual(avg_movie_rating['1000'], 3.28)
        self.assertEqual(avg_movie_rating['1001'], 3.31)
        self.assertEqual(avg_movie_rating['1002'], 3.44)

    # -----
    # netflix_read
    # -----

    def test_netflix_read_1(self):
        """ netflix_read_1 """
        input_dic = {}
        store_rating = {}
        reader = StringIO("2043:\n555555\n666666\n777777\n")
        netflix_read(reader, input_dic, store_rating)
        self.assertEqual(input_dic, {2043: [555555, 666666, 777777]})

    def test_netflix_read_2(self):
        """ netflix_read_2 """
        input_dic = {}
        store_rating = {}
        reader = StringIO(
            "2043:\n555555\n666666\n777777\n2044:\n888888\n9999999\n")
        netflix_read(reader, input_dic, store_rating)
        self.assertEqual(store_rating, {2043: [], 2044: []})

    def test_netflix_read_3(self):
        """ netflix_read_3 """
        input_dic = {}
        store_rating = {}
        reader = StringIO("2043:\n2044:\n2045:\n1111111")
        netflix_read(reader, input_dic, store_rating)
        self.assertEqual(input_dic, {2045: [1111111]})

    def test_netflix_read_4(self):
        """ netflix_read_4 """
        input_dic = {}
        store_rating = {}
        reader = StringIO("2042:\n2043:\n000001\n2044:\n2045:\n1111111")
        netflix_read(reader, input_dic, store_rating)
        self.assertEqual(store_rating, {2043: [], 2045: []})

    # ----
    # netflix_eval
    # ----

    def test_sqrt_netflix_eval_1(self):
        """ test netflix_eval_1 """
        input_dic = {2043: [1417435, 2312054, 462685]}
        store_rating = {2043: []}
        avg_cust_rating = {"1417435": 1.0, "2312054": 3.0, "462685": 5.0}
        avg_movie_rating = {"2043": 3.5}
        netflix_eval(input_dic, store_rating,
                     avg_cust_rating, avg_movie_rating)
        self.assertEqual(store_rating, {2043: [1.6, 3.1, 4.5]})

    def test_sqrt_netflix_eval_2(self):
        """ test netflix_eval_2 """
        input_dic = {1: [1000]}
        store_rating = {1: []}
        avg_cust_rating = {"1000": 1.0, "1002": 3.0, "1003": 5.0}
        avg_movie_rating = {"1": 1.0}
        netflix_eval(input_dic, store_rating,
                     avg_cust_rating, avg_movie_rating)
        self.assertEqual(store_rating, {1: [1.0]})

    def test_sqrt_netflix_eval_3(self):
        """ test netflix_eval_3 """
        input_dic = {1: [100, 101], 2: [100]}
        store_rating = {1: [], 2: []}
        avg_cust_rating = {"100": 1.0, "101": 5.0}
        avg_movie_rating = {"1": 1.0, "2": 5.0}
        netflix_eval(input_dic, store_rating,
                     avg_cust_rating, avg_movie_rating)
        self.assertEqual(store_rating, {1: [1.0, 2.8], 2: [2.7]})

        # -----
    # netflix_print
    # -----

    def test_netflix_print_1(self):
        """ netflix_print_1 """
        input_dic = {1: {2001}, 2: {2002}, 3: {2003}}
        store_rating = {1: {3.5}, 2: {3.6}, 3: {3.7}}
        writer = StringIO()
        netflix_print(writer, input_dic, store_rating)
        self.assertEqual(
            writer.getvalue(), "1:\n2001 3.5\n2:\n2002 3.6\n3:\n2003 3.7\n")

    def test_netflix_print_2(self):
        """ netflix_print_2 """
        input_dic = {1: {1000, 1001, 1002, 1003}}
        store_rating = {1: {3.4, 3.5, 3.6, 3.7}}
        writer = StringIO()
        netflix_print(writer, input_dic, store_rating)
        self.assertEqual(
            writer.getvalue(), "1:\n1000 3.6\n1001 3.5\n1002 3.7\n1003 3.4\n")

    def test_netflix_print_3(self):
        """ netflix_print_3 """
        input_dic = {1: {1001, 1002, 1003, 1004, 1005}}
        store_rating = {1: {3.5, 3.6}}
        writer = StringIO()
        netflix_print(writer, input_dic, store_rating)
        self.assertEqual(writer.getvalue(), "1:\n1001 3.5\n1002 3.6\n")

    # ----
    # sqrt_diff
    # ----

    def test_sqrt_diff_1(self):
        """ test sqrt_diff_1 """
        self.assertEqual(sqrt_diff(18, 9), 81)

    def test_sqrt_diff_2(self):
        """ test sqrt_diff_2"""
        self.assertEqual(sqrt_diff(1, 1), 0)

    def test_sqrt_diff_3(self):
        """ test sqrt_diff_3 """
        self.assertEqual(sqrt_diff(1, 3), 4)

    def test_sqrt_diff_4(self):
        """ test sqrt_diff_4 """
        self.assertEqual(sqrt_diff(-1, 3), 16)

    # ----
    # netflix_rmse
    # ----
    def test_netflix_rmse_1(self):
        """ test_netflix_rmse_1 """
        input_dic = {1: {2001}, 2: {2002}, 3: {2003}}
        store_rating = {1: {3.5}, 2: {3.6}, 3: {3.7}}
        actual_rating = {1: {2001: 4.0}, 2: {2002: 3.6}, 3: {2003: 3.6}}
        self.assertEqual(
            netflix_rmse(input_dic, store_rating, actual_rating), 0.2943920288775949)

    def test_netflix_rmse_2(self):
        """ test_netflix_rmse_2 """
        input_dic = {1: {2001}, 2: {2002}}
        store_rating = {1: {3.5}, 2: {3.6}}
        actual_rating = {1: {2001: 1.0}, 2: {2002: 5.0}}
        self.assertEqual(
            netflix_rmse(input_dic, store_rating, actual_rating), 2.026079958935481)

    def test_netflix_rmse_3(self):
        """ test_netflix_rmse_3 """
        input_dic = {1: {2001, 2002, 2003}}
        store_rating = {1: {3.5, 3.6, 3.7}}
        actual_rating = {1: {2001: 2.0, 2002: 4.0, 2003: 4.0}}
        self.assertEqual(
            netflix_rmse(input_dic, store_rating, actual_rating), 0.9831920802501751)

    # ----
    # netflix_solve
    # ----

    def test_netflix_solve_1(self):
        """ test_netflix_solve_1 """
        reader = StringIO("2043:\n1417435")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "2043:\n1417435 3.6\nRMSE: 0.60")

    def test_netflix_solve_2(self):
        """ test_netflix_solve_2 """
        reader = StringIO("2043:\n1417435\n2312054")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "2043:\n1417435 3.6\n2312054 4.3\nRMSE: 2.37")

    def test_netflix_solve_3(self):
        """ test_netflix_solve_3 """
        reader = StringIO("2043:\n1417435\n2312054\n462685")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "2043:\n1417435 3.6\n2312054 4.3\n462685 3.8\nRMSE: 1.94")

    def test_netflix_solve_4(self):
        """ test_netflix_solve_4 """
        reader = StringIO("2043:\n1417435\n1:\n30878")
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1:\n30878 3.7\n2043:\n1417435 3.6\nRMSE: 0.47")

# ----
# main
# ----
if __name__ == "__main__":
    main()
