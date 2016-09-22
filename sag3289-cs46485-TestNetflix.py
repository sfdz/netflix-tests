#!/usr/bin/env python3
# pylint: disable=missing-docstring,line-too-long,too-many-public-methods

# tests

# -----------
# TestNetflix
# -----------
from io import StringIO
from unittest import main, TestCase

from Netflix import rmse, estimate_ratings, get_actual_ratings, parse_movies, run_netflix, mean, square, sqrt

ACTUAL_RATINGS = {('10', '1544919'): 2, ('10063', '1544919'): 3, ('10066', '1544919'): 2, ('10624', '1544919'): 4,
                  ('10', '1712360'): 3, ('10063', '1712360'): 3, ('10066', '1712360'): 4, ('10624', '1712360'): 2,
                  ('10', '964645'): 3, ('10063', '964645'): 4, ('10066', '964645'): 4, ('10624', '964645'): 2,
                  ('10', '608114'): 4, ('10063', '608114'): 5, ('10066', '608114'): 5, ('10624', '608114'): 4,
                  ('10', '1943448'): 5, ('10063', '1943448'): 3, ('10066', '1943448'): 4, ('10624', '1943448'): 4}

CUST_AVG = {'1544919': 2.72, '1712360': 3.14,
            '964645': 3.35, '608114': 4.53, '1943448': 4.08}

MOVIE_AVG = {'10': 3.18, '10063': 3.83, '10624': 3.13, '10066': 2.9}

CUST_YEAR_AVG = {
    1544919: {2001: 0.7664583242842625, 1998: 0.6830243841064676, 1974: -1.8497341459515727},
    1712360: {2001: 0.7664583242842625, 1998: 0.6830243841064676, 1974: -0.8497341459515727},
    964645: {2001: 0.7664583242842625, 1998: 0.6830243841064676, 1974: -0.8497341459515727},
    608114: {2001: 0.7664583242842625, 1998: 0.6830243841064676, 1974: -0.8497341459515727},
    1943448: {2001: 2.7664583242842625, 1998: 0.6830243841064676, 1974: -0.8497341459515727}}

MOVIE_YEARS = {10: 2001, 10063: 1998, 10066: 1974, 10624: 1998}

# 10, 10063, 10066, 10624

        # movie = ['10066:', '1544919', '1712360', '964645', '608114',
        # '1943448']

        # movie = ['10624:', '1064957', '1647722', '87033',
        #          '2120115', '1352826', '1300733', '1118187', '41422']

        # movie = ['10:', '1952305', '1531863']

        # movie = ['10063:', '2646124', '1059193', '2498639', '2232100', '846288', '1891279',
        #          '326040', '2220804', '1147138', '477002', '278598', '1085817', '1989258', '1227162']

   # 2097731: {1984: -1.6617618314467917, 1985: 0.46648275343186274, 1986: -0.3941397077134502,
   # 1987: -0.8166043457547307, 1988: -0.5569605112498258, 1989: -0.35365041528849633,
   # 1990: -1.8183789


class TestNetflix(TestCase):

    # ----
    # rmse
    # ----

    def test_rmse_1(self):
        real_list = [['10:', 3, 3, 3, 4]]
        estimate_list = [['10:', 2, 2, 2, 3]]
        rmse_result = rmse(real_list, estimate_list)
        self.assertEqual(rmse_result, '1.00')

    def test_rsme_2(self):
        real_list = [['1:', 1, 1, 1, 1, 1], ['2:', 2, 2], ['3:', 3, 3, 3]]
        estimate_list = [['1:', 2, 1, 3, 2, 5], ['2:', 2, 2], ['3:', 3, 3, 2]]
        rmse_result = rmse(real_list, estimate_list)
        self.assertEqual(rmse_result, '1.52')

    def test_rsme_3(self):
        real_list = [['6:', 1, 1, 2, 5, 3], ['7:', 5, 1], ['601:', 3, 4, 3]]
        estimate_list = [['1:', 2, 1, 3, 2, 5],
                         ['7:', 2, 2], ['601:', 3, 3, 2]]
        rmse_result = rmse(real_list, estimate_list)
        self.assertEqual(rmse_result, '1.64')

    # -----
    # mean
    # -----

    def test_mean_1(self):
        numbers = [1, 5, 3, 2, 4, 3, 3]
        self.assertEqual(mean(numbers), 3)

    def test_mean_2(self):
        numbers = [4, 4, 4, 4]
        self.assertEqual(mean(numbers), 4)

    def test_mean_3(self):
        numbers = [5, 1, 5, 4, 3, 2, 5, 5, 3, 5]
        self.assertEqual(mean(numbers), 3.8)

    # ------
    # square
    # ------

    def test_square_1(self):
        numbers = [1, 2, 3, 4, 5, 6]
        self.assertEqual(square(numbers), [1, 4, 9, 16, 25, 36])

    def test_square_2(self):
        numbers = [10, 100, 1000]
        self.assertEqual(square(numbers), [100, 10000, 1000000])

    def test_square_3(self):
        numbers = [1, 1, 1, 2, 5]
        self.assertEqual(square(numbers), [1, 1, 1, 4, 25])

    # -----
    # sqrt
    # -----
    def test_sqrt_1(self):
        result = sqrt(4)
        self.assertEqual(result, 2)

    def test_sqrt_2(self):
        result = sqrt(1015)
        self.assertEqual(result, 31.85906464414798)

    def test_sqrt_3(self):
        result = sqrt(7)
        self.assertEqual(result, 2.6457513110645907)

    # ----------------
    # estimate_ratings
    # ----------------
#  cust_avg_cache,
                     # movie_avg_cache, cust_year_avg_cache,
                     # movie_years_cache):
    def test_estimate_ratings_1(self):
        movie = ['10066:', '1544919', '1712360', '964645', '608114', '1943448']
        self.assertEqual(
            estimate_ratings(
                movie, CUST_AVG, MOVIE_AVG, CUST_YEAR_AVG, MOVIE_YEARS),
            ['10066:', 1.0, 2.2, 2.3, 2.9, 2.7])

    def test_estimate_ratings_2(self):
        movie = ['10063:', '1544919', '1712360', '964645', '608114']
        self.assertEqual(
            estimate_ratings(
                movie, CUST_AVG, MOVIE_AVG, CUST_YEAR_AVG, MOVIE_YEARS),
            ['10063:', 3.9, 4.1, 4.3, 4.9])

    def test_estimate_ratings_3(self):
        movie = ['10:', '1712360', '1544919']
        self.assertEqual(
            estimate_ratings(
                movie, CUST_AVG, MOVIE_AVG, CUST_YEAR_AVG, MOVIE_YEARS),
            ['10:', 3.9, 3.7])

    def test_estimate_ratings_4(self):
        movie = ['10624:', '1544919', '964645', '1712360', '1943448', '608114']
        self.assertEqual(
            estimate_ratings(
                movie, CUST_AVG, MOVIE_AVG, CUST_YEAR_AVG, MOVIE_YEARS),
            ['10624:', 3.6, 3.9, 3.8, 4.3, 4.6])
    # ------------------
    # get_actual_ratings
    # ------------------

    def test_get_actual_ratings_1(self):
        movie_list = [
            ['10624:', '1544919', '964645', '1712360', '1943448', '608114']]
        ratings = get_actual_ratings(movie_list, ACTUAL_RATINGS)
        self.assertEqual(
            ratings, [['10624:', 4, 2, 2, 4, 4]])

    def test_get_actual_ratings_2(self):
        movie_list = [
            ['10624:', '1544919', '964645', '1712360', '608114'],
            ['10066:', '964645', '1712360', '1943448', '608114'],
            ['10063:', '1544919', '1943448', '608114']]
        ratings = get_actual_ratings(movie_list, ACTUAL_RATINGS)
        self.assertEqual(
            ratings, [['10624:', 4, 2, 2, 4], ['10066:', 4, 4, 4, 5], ['10063:', 3, 3, 5]])

    def test_get_actual_ratings_3(self):
        movie_list = [
            ['10624:', '1544919', '964645', '1712360', '1943448', '608114'],
            ['10063:', '1544919', '964645', '1712360', '1943448', '608114'],
            ['10066:', '1544919', '964645', '1712360', '1943448', '608114'],
            ['10:', '1544919', '964645', '1712360', '1943448', '608114']]
        ratings = get_actual_ratings(movie_list, ACTUAL_RATINGS)
        self.assertEqual(
            ratings, [['10624:', 4, 2, 2, 4, 4], ['10063:', 3, 4, 3, 3, 5], ['10066:', 2, 4, 4, 4, 5], ['10:', 2, 3, 3, 5, 4]])
    # ------------
    # parse_movies
    # ------------

    def test_parse_movies_1(self):
        reader = StringIO("1:\n100\n200\n300\n2:\n500\n600\n")
        parse_list = parse_movies(reader)
        self.assertEqual(
            parse_list, [['1:', '100', '200', '300'], ['2:', '500', '600']])

    def test_parse_movies_2(self):
        reader = StringIO(
            "5:\n1000\n999\n\n299\n\n10:\n7\n52\n25:\n20\n10000\n250\n")
        parse_list = parse_movies(reader)
        self.assertEqual(parse_list, [['5:', '1000', '999', '299'], [
            '10:', '7', '52'], ['25:', '20', '10000', '250']])

    def test_parse_movie_3(self):
        reader = StringIO("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        parse_list = parse_movies(reader)
        self.assertEqual(parse_list, [])

    # ------------
    # run_netflix
    # ------------

    def test_run_netflix_1(self):
        reader = StringIO(
            "10624:\n1544919\n964645\n1712360\n1943448\n608114\n")
        writer = StringIO()
        run_netflix(reader, writer, ACTUAL_RATINGS,
                    CUST_AVG, MOVIE_AVG, CUST_YEAR_AVG, MOVIE_YEARS)
        self.assertEqual(
            writer.getvalue(), "10624:\n3.6\n3.9\n3.8\n4.3\n4.6\nRMSE: 1.22\n")

    def test_run_netflix_2(self):
        reader = StringIO(
            "10624:\n1544919\n964645\n1712360\n608114\n10066:\n964645\n1712360\n1943448\n608114\n10063:\n1544919\n1943448\n608114\n")
        writer = StringIO()
        run_netflix(reader, writer, ACTUAL_RATINGS,
                    CUST_AVG, MOVIE_AVG, CUST_YEAR_AVG, MOVIE_YEARS)
        self.assertEqual(
            writer.getvalue(), "10624:\n3.6\n3.9\n3.8\n4.6\n10066:\n2.3\n2.2\n2.7\n2.9\n10063:\n3.9\n4.6\n4.9\nRMSE: 1.45\n")

    def test_run_netflix_3(self):
        reader = StringIO(
            "10624:\n1544919\n964645\n1712360\n1943448\n608114\n10063:\n1544919\n964645\n1712360\n1943448\n608114\n10066:\n1544919\n964645\n1712360\n1943448\n608114\n10:\n1544919\n964645\n1712360\n1943448\n608114\n")
        writer = StringIO()
        run_netflix(reader, writer, ACTUAL_RATINGS,
                    CUST_AVG, MOVIE_AVG, CUST_YEAR_AVG, MOVIE_YEARS)
        self.assertEqual(
            writer.getvalue(), "10624:\n3.6\n3.9\n3.8\n4.3\n4.6\n10063:\n3.9\n4.3\n4.1\n4.6\n4.9\n10066:\n1.0\n2.3\n2.2\n2.7\n2.9\n10:\n3.7\n4.0\n3.9\n5.0\n4.7\nRMSE: 1.24\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()
