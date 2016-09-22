#!/usr/bin/env python3


"""Tests harness for Netflix"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_solve, netflix_rmse, netflix_predict, get_actual, get_mov, get_cus


# -----------
# TestNetflix
# -----------


class TestNetflix(TestCase):

    """Test harness"""

    # ------------
    # netflix_rmse
    # ------------

    def test_rmse_1(self):
        """First RMSE test"""
        count = 1
        sum_sq_diff = 4
        self.assertEqual(netflix_rmse(count, sum_sq_diff), 2.00000)

    def test_rmse_2(self):
        """Second RMSE test"""
        count = 7
        sum_sq_diff = 17
        self.assertEqual(netflix_rmse(count, sum_sq_diff), 1.55839)

    def test_rmse_3(self):
        """Third RMSE test"""
        count = 8
        sum_sq_diff = 1
        self.assertEqual(netflix_rmse(count, sum_sq_diff), 0.35355)

    # ----------
    # get_actual
    # ----------
    def test_get_actual_1(self):
        """Fetch actual rating 3"""
        key_mov = "2043"
        key_cus = "1417435"
        self.assertEqual(get_actual(key_mov, key_cus), 3)

    def test_get_actual_2(self):
        """Check assert safety"""
        key_mov = "0"
        key_cus = "1417435"
        try:
            self.assertEqual(get_actual(key_mov, key_cus), 0)
        except AssertionError:
            pass
        else:
            raise ValueError("Getter tried fetching non-positive integer")

    def test_get_actual_3(self):
        """Return 0 if not in cache"""
        key_mov = "999999999999"
        key_cus = "999999999999"
        self.assertEqual(get_actual(key_mov, key_cus), 0)

    def test_get_actual_4(self):
        """Check assert safety"""
        key_cus = "0"
        key_mov = "2043"
        try:
            self.assertEqual(get_actual(key_mov, key_cus), 0)
        except AssertionError:
            pass
        else:
            raise ValueError("Getter tried fetching non-positive integer")

    # -------
    # get_mov
    # -------
    def test_get_mov_1(self):
        """Fetch movie avg for movie ID 2043"""
        key_mov = "2043"
        self.assertEqual(get_mov(key_mov), 3.77)

    def test_get_mov_2(self):
        """Return 0 if movie does not exist"""
        key_mov = "99999999"
        self.assertEqual(get_mov(key_mov), 0)

    def test_get_mov_3(self):
        """Another general test"""
        key_mov = "13"
        self.assertEqual(get_mov(key_mov), 4.55)

    # -------
    # get_cus
    # -------
    def test_get_cus_1(self):
        """Fetch customer avg"""
        key_cus = "1417435"
        self.assertEqual(get_cus(key_cus), 3.5)

    def test_get_cus_2(self):
        """Fetch 0 if customer does not exist"""
        key_cus = "99999999"
        self.assertEqual(get_cus(key_cus), 0)

    def test_get_cus_3(self):
        """Fetch customer avg"""
        key_cus = "2312054"
        self.assertEqual(get_cus(key_cus), 4.45)

    # ---------------
    # netflix_predict
    # ---------------
    def test_predict_1(self):
        """Our prediction based on movie and customer"""
        key_mov = "2043"
        key_cus = "1417435"
        self.assertEqual(netflix_predict(key_mov, key_cus), 3.57)

    def test_predict_2(self):
        """Giving None movie and customer to force a return of 0"""
        key_mov = "999999999"
        key_cus = "999999999"
        self.assertEqual(netflix_predict(key_mov, key_cus), 0)

    def test_predict_3(self):
        """Simply another test"""
        key_mov = "888"
        key_cus = "2312054"
        self.assertEqual(netflix_predict(key_mov, key_cus), 3.36)

    # -------------
    # netflix_solve
    # -------------
    def test_solve_1(self):
        """Example"""
        str_in = StringIO(
            "13:\n615010\n1860468\n2131832\n")
        str_out = StringIO()
        netflix_solve(str_in, str_out)
        self.assertEqual(
            str_out.getvalue(), "13:\n4.9\n4.7\n5.0\nRMSE: 0.22")

    def test_solve_2(self):
        """Sample run throughs"""
        str_in = StringIO("10:\n1952305\n1531863\n1000:\n2326571\n977808")
        str_out = StringIO()
        netflix_solve(str_in, str_out)
        self.assertEqual(
            str_out.getvalue(), "10:\n2.9\n2.6\n1000:\n3.2\n2.9\nRMSE: 0.22")

    def test_solve_3(self):
        """Test 3"""
        str_in = StringIO("1:\n30878\n2647871\n1283744")
        str_out = StringIO()
        netflix_solve(str_in, str_out)
        self.assertEqual(
            str_out.getvalue(), "1:\n3.7\n3.3\n3.6\nRMSE: 0.57")


# ----
# main
# ----

if __name__ == "__main__":
    main()
