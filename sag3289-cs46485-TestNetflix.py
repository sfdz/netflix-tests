#!/usr/bin/env python3
# pylint: disable=missing-docstring,line-too-long,too-many-public-methods

# tests

# -----------
# TestNetflix
# -----------
from io import StringIO
from unittest import main, TestCase

from Netflix import rmse, estimate_ratings, get_actual_ratings, parse_movies, run_netflix, mean, square, sqrt


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

    def test_estimate_ratings_1(self):
        movie = ['10066:', '1544919', '1712360', '964645', '608114', '1943448']
        self.assertEqual(estimate_ratings(movie), ['10066:', 2.7, 3.4, 3.3, 3.2, 2.4])

    def test_estimate_ratings_2(self):
        movie = ['10624:', '1064957', '1647722', '87033',
                 '2120115', '1352826', '1300733', '1118187', '41422']
        self.assertEqual(estimate_ratings(movie), ['10624:', 3.4, 3.3, 2.6, 4.7, 4.5, 2.7, 2.7, 3.6])

    def test_estimate_ratings_3(self):
        movie = ['10:', '1952305', '1531863']
        self.assertEqual(estimate_ratings(movie), ['10:', 3.1, 3.0])

    def test_estimate_ratings_4(self):
        movie = ['10063:', '2646124', '1059193', '2498639', '2232100', '846288', '1891279', '326040', '2220804', '1147138', '477002', '278598', '1085817', '1989258', '1227162']
        self.assertEqual(estimate_ratings(movie), ['10063:', 3.0, 2.0, 2.9, 3.6, 5.0, 3.2, 4.4, 5.0, 1.0, 3.5, 4.8, 5.0, 4.8, 3.8])
    # ------------------
    # get_actual_ratings
    # ------------------

    def test_get_actual_ratings_1(self):
        movie_list = [
            ['10028:', '1986255', '1312610', '1527666', '1606775', '1649392',
             '1522640', '440956'], ['10029:', '2293890', '1141552', '1823836', '2551226']]
        ratings = get_actual_ratings(movie_list)
        self.assertEqual(
            ratings, [['10028:', 4, 3, 4, 5, 5, 3, 5], ['10029:', 3, 5, 3, 3]])

    def test_get_actual_ratings_2(self):
        movie_list = [
            ['10066:', '1544919', '1712360', '964645', '608114', '1943448'],
            ['10067:', '1747200', '212759', '1678519', '1025440', '2400195', '2331378', '1715415'],
            ['10068:', '2169183', '1200359', '1477194', '1861603', '1516386', '2217808'],
            ['10069:', '2140139', '1555169', '562543'], ['1007:', '95090', '468346', '84508', '2202141', '2383688'],
            ['10070:', '1611581', '2116105', '2126134']]
        ratings = get_actual_ratings(movie_list)
        self.assertEqual(ratings, [['10066:', 2, 3, 3, 3, 2], ['10067:', 5, 4, 5, 5, 4, 3, 2], [
            '10068:', 3, 4, 3, 5, 5, 4], ['10069:', 3, 3, 2], ['1007:', 4, 2, 4, 3, 4], ['10070:', 4, 2, 1]])

    def test_get_actual_ratings_3(self):
        movie_list = [
            ['10622:', '60296', '764750', '640454', '134864', '1727651', '1847231', '1676093', '161104', '1997103',
             '1721636', '2556140', '943534', '667346', '1001185', '1136939', '2493493', '250302', '2417914', '1850241',
             '1767265', '2531021', '1000576', '684078', '1653368', '1000419', '1171012', '1539212', '77708', '1667893',
             '5710', '493480', '1455720', '472736', '2315012',
             '1872701', '129310', '1710311', '1625249', '2060307', '286680', '2263821', '1805566', '917694', '1143746',
             '2292818', '1002660', '1641947', '548665', '1166373', '1755214', '1150680', '2160484', '1540741', '2184628',
             '1440026', '99720', '214850', '2278024', '1105767', '1634235'],
            ['10624:', '1064957', '1647722', '87033',
             '2120115', '1352826', '1300733', '1118187', '41422']]
        ratings = get_actual_ratings(movie_list)
        self.assertEqual(
            ratings, [
                ['10622:', 3, 3, 1, 4, 5, 3, 4, 4, 2, 3, 3, 4, 3, 5, 5, 3, 3, 2, 3, 3, 5, 2, 4, 4, 5, 5, 4, 2, 2, 5,
                 5, 4, 3, 2, 4, 4, 4, 5, 4, 4, 3, 4, 3, 4, 4, 3, 3, 5, 3, 3, 5, 4, 2, 3, 4, 4, 5, 5, 4, 2], ['10624:', 2, 3, 3, 4, 4, 3, 3, 3]])
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
        reader = StringIO("1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n14756\n1027056\n1149588\n1394012\n1406595\n2529547\n1682104\n2625019\n2603381\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n10:\n1952305\n1531863\n")
        writer = StringIO()
        run_netflix(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1:\n3.7\n3.0\n3.8\n5.0\n4.9\n4.1\n3.8\n3.9\n3.6\n3.6\n2.9\n3.8\n3.9\n4.1\n2.4\n4.3\n4.0\n5.0\n4.3\n5.0\n2.4\n5.0\n3.3\n10:\n3.1\n3.0\nRMSE: 0.70\n")

    def test_run_netflix_2(self):
        reader = StringIO("10069:\n2140139\n1555169\n562543\n1007:\n95090\n468346\n84508\n2202141\n2383688\n10070:\n1611581\n2116105\n2126134\n")
        writer = StringIO()
        run_netflix(reader, writer)
        self.assertEqual(
            writer.getvalue(), "10069:\n3.8\n2.8\n2.6\n1007:\n4.1\n3.3\n4.7\n3.1\n4.1\n10070:\n3.6\n2.0\n1.9\nRMSE: 0.62\n")

    def test_run_netflix_3(self):
        reader = StringIO("1021:\n1157667\n2618351\n1435902\n1331\n1780588\n964825\n620832\n1645064\n894553\n1676997\n1632247\n868733\n1429332\n754567\n2303740\n302344\n1108131\n2131301\n510712\n2289237\n990036\n2633644\n2543516\n379005\n2170900\n1587712\n481433\n2632868\n1305371\n1343436\n2447225\n353669\n1183731\n366775\n2427961\n229634\n1694254\n474566\n2528435\n972040\n1688898\n1082864\n2278872\n571455\n581616\n607220\n2442028\n1174108\n1610929\n927271\n509331\n373838\n1151836\n1019775\n697818\n2487578\n148404\n1838848\n1122480\n2031549\n1677426\n1437925\n1184761\n920617\n1463238\n188630\n1482840\n1909324\n309719\n10210:\n2282309\n114388\n")
        writer = StringIO()
        run_netflix(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1021:\n1.7\n3.4\n1.9\n3.4\n4.0\n4.3\n4.3\n3.7\n3.5\n3.7\n3.1\n4.1\n4.1\n3.2\n3.4\n3.8\n3.9\n4.3\n3.5\n3.5\n3.2\n4.5\n3.4\n4.8\n3.6\n4.3\n3.1\n2.3\n4.7\n3.4\n2.2\n4.9\n4.6\n3.9\n3.5\n3.1\n3.4\n4.0\n3.9\n2.6\n2.4\n3.7\n5.0\n3.4\n3.3\n3.5\n3.8\n4.1\n4.4\n3.3\n3.8\n3.4\n3.9\n5.0\n3.5\n5.0\n3.4\n5.0\n3.5\n2.7\n3.3\n3.8\n2.9\n4.5\n5.0\n3.7\n2.7\n3.3\n5.0\n10210:\n1.7\n1.8\nRMSE: 0.66\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
