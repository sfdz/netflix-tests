""" Test Netflix.py """

from unittest import main, TestCase
from io import StringIO
from Netflix import Netflix, netflix_print


class TestNetflix(TestCase):

    """ Class for testing Collatz """

    # ----
    # init
    # ----

    def test_netflix_init_1(self):
        """ Ensure that Netflix creation is correct"""
        netflix = Netflix()

        self.assertEqual(netflix.__base_avg__, 3.7)
        self.assertEqual(netflix.__index__, 0)
        self.assertEqual(netflix.__rmse__, 0)

    # ----
    # eval
    # ----

    def test_netflix_eval_1(self):
        """ Ensure eval functionality is correct """

        w_value = StringIO()
        evaluate = Netflix()

        evaluate.__customer__ = {"1": 3, "2": 3, "3": 3, "4": 4}
        evaluate.__movie__ = {"1": 3.8}
        evaluate.__actual__ = [[0], [0, 3, 3, 3, 3]]

        evaluate.__cur_movie__ = ["1", 0]
        evaluate.__cid__ += ["1", "2", "3", "4"]

        evaluate.netflix_eval(w_value)
        self.assertEqual(evaluate.__ratings__, [3.1, 3.1, 3.1, 4.1])

    def test_netflix_eval_2(self):
        """ tests eval for different movie input """
        w_value = StringIO()
        evaluate = Netflix()

        evaluate.__customer__ = {"1": 5.0}
        evaluate.__movie__ = {"10": 5.0}
        evaluate.__actual__ = [[0], [0], [0], [0], [0], [0], [0], [0],
                               [0], [0], [0, 5.0]]

        evaluate.__cur_movie__ = ["10"]
        evaluate.__cid__ = ["1"]
        evaluate.__ratings__ = []

        evaluate.netflix_eval(w_value)
        self.assertEqual(evaluate.__ratings__, [5.0])

    # -----
    # print
    # -----

    def test_netflix_print_1(self):
        """ Ensure print functionality is correct for integer input"""
        w_value = StringIO()
        netflix_print(w_value, 1)
        self.assertEqual(w_value.getvalue(), "1\n")

    def test_netflix_print_2(self):
        """ Ensure print functionality is correct for string input"""
        w_value = StringIO()
        netflix_print(w_value, "1")
        self.assertEqual(w_value.getvalue(), "1\n")

    # -----
    # solve
    # -----

    def test_netflix_solve_1(self):
        """ Ensure solve functionality is correct """
        netflix = Netflix()

        # reset cid and ratings
        netflix.__cid__ = []
        netflix.__ratings__ = []

        caches = [
            {"1": 3.0},
            {"1": 3.0},
            [[0], [0, 3]]
        ]

        # input/output
        r_value = StringIO("1:\n1\n")
        w_value = StringIO()

        netflix.netflix_solve(r_value, w_value, caches)

        # test output
        self.assertEqual(
            w_value.getvalue(),
            "1:\n2.3\nRMSE: 0.49\n")

    def test_netflix_solve_2(self):
        """ tests solve for two movies """
        netflix = Netflix()

        # reset cid and ratings
        netflix.__cid__ = []
        netflix.__ratings__ = []

        caches = [
            {"1": 3.0, "2": 2.0},
            {"1": 3.0, "2": 4.0},
            [[0], [0, 3], [0, 0, 3.0]]
        ]

        # input/output
        r_value = StringIO("1:\n1\n2:\n2\n")
        w_value = StringIO()

        netflix.netflix_solve(r_value, w_value, caches)

        # test output
        self.assertEqual(
            w_value.getvalue(),
            "1:\n2.3\n2:\n2.3\nRMSE: 0.57\n")

    def test_netflix_solve_3(self):
        """ tests solve for many movies"""
        netflix = Netflix()

        # reset cid and ratings
        netflix.__cid__ = []
        netflix.__ratings__ = []

        caches = [
            {"1": 3.0, "2": 2.0, "3": 4.0},
            {"1": 3.0, "2": 4.0, "3": 5.0},
            [[0], [0, 3], [0, 0, 3.0], [0, 0, 0, 4.5]]
        ]

        # input/output
        r_value = StringIO("1:\n1\n2:\n2\n3:\n3\n")
        w_value = StringIO()

        netflix.netflix_solve(r_value, w_value, caches)

        # test output
        self.assertEqual(
            w_value.getvalue(),
            "1:\n2.3\n2:\n2.3\n3:\n5.0\nRMSE: 0.55\n")

    def test_netflix_solve_4(self):
        """ Tests rmse for small input """
        netflix = Netflix()

        # reset cid and ratings
        netflix.__cid__ = []
        netflix.__ratings__ = []

        caches = [
            {"1": 0.0},
            {"1": 0.0},
            [[0], [0, 0.0]]
        ]

        # input/output
        r_value = StringIO("1:\n1\n")
        w_value = StringIO()

        netflix.netflix_solve(r_value, w_value, caches)

        # test output
        self.assertEqual(
            w_value.getvalue(),
            "1:\n0.0\nRMSE: 0.00\n")

    def test_netflix_solve_5(self):
        """ tests solve for zero cust ids """
        netflix = Netflix()

        # reset cid and ratings
        netflix.__cid__ = []
        netflix.__ratings__ = []

        # input/output
        r_value = StringIO("1:")
        w_value = StringIO()

        caches = [
            {"1": 0.0},
            {"1": 0.0},
            [[0], [0, 0.0]]
        ]

        netflix.netflix_solve(r_value, w_value, caches)

        # test output
        self.assertEqual(
            w_value.getvalue(),
            "1:\nRMSE: 0.00\n")

    def test_netflix_solve_6(self):
        """ tests solve for repeating movies """
        netflix = Netflix()

        # reset cid and ratings
        netflix.__cid__ = []
        netflix.__ratings__ = []

        # input/output
        r_value = StringIO("1:\n1\n1:\n1\n1:\n1")
        w_value = StringIO()

        caches = [
            {"1": 4.0},
            {"1": 4.0},
            [[0], [0, 4.0]]
        ]

        netflix.netflix_solve(r_value, w_value, caches)

        # test output
        self.assertEqual(
            w_value.getvalue(),
            "1:\n4.3\n1:\n4.3\n1:\n4.3\nRMSE: 0.26\n")

    def test_netflix_solve_7(self):
        """ tests solve for one empty movie and a movie with one cid """
        netflix = Netflix()

        # reset cid and ratings
        netflix.__cid__ = []
        netflix.__ratings__ = []

        # input/output
        r_value = StringIO("1:\n2:\n1\n")
        w_value = StringIO()

        caches = [
            {"1": 3.0},
            {"1": 3.0, "2": 3.0},
            [[0], [0, 0.0], [0, 3.0]]
        ]

        netflix.netflix_solve(r_value, w_value, caches)

        # test output
        self.assertEqual(
            w_value.getvalue(),
            "2:\n2.3\nRMSE: 0.49\n")

    def test_netflix_solve_8(self):
        """ tests solve for many customers """
        netflix = Netflix()

        # reset cid and ratings
        netflix.__cid__ = []
        netflix.__ratings__ = []

        # input/output
        r_value = StringIO("1:\n1\n2\n3\n4\n5\n6\n7\n8\n9\n")
        w_value = StringIO()

        caches = [
            {"1": 3.0, "2": 4.0, "3": 2.0, "4": 5.0, "5": 3.0,
             "6": 1.0, "7": 3.0, "8": 4.0, "9": 3.0},
            {"1": 3.0},
            [[0], [0, 3.0, 4.0, 2.0, 5.0, 3.0, 1.0,
                   3.0, 4.0, 3.0]]
        ]

        netflix.netflix_solve(r_value, w_value, caches)

        # test output
        self.assertEqual(
            w_value.getvalue(),
            "1:\n2.3\n3.3\n1.3\n4.3\n2.3\n0.3\n2.3\n3.3\n2.3\nRMSE: 0.66\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
