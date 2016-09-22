""" Jake Mayo & Alex Irion Fall 2016 Test Harness """
#!/usr/bin/envalpython3

# -------
# imports
# -------
import pickle
import urllib.request
from io import StringIO
from unittest import main, TestCase
from Netflix import rmse, predict_rating, netflix_solve

# -----------
# TestNetflix
# -----------
class TestNetflix(TestCase):
    """ test netflix """

    # # ----
    # # RMSE
    # # ----
    def test_rmse_1(self):
        """ test netflix rmse """
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        self.assertEqual(rmse(list1, list2), 1.00)

    def test_rmse_2(self):
        """ test netflix rmse """
        list1 = [1, 2, 3]
        list2 = [3, 4, 5]
        self.assertEqual(rmse(list1, list2), 2.00)

    def test_rmse_3(self):
        """ test netflix rmse """
        list1 = [4, 5, 1, 4, 5, 3, 2]
        list2 = [3.7, 4.2, 3, 4.2, 2.2, 3.8, 2]
        self.assertEqual(rmse(list1, list2), 1.38)

    def test_rmse_4(self):
        """ test netflix rmse """
        list1 = [1, 2, 3, 5, 5, 5, 1]
        list2 = [3, 4, 5, 3, 3, 3, 4]
        self.assertEqual(rmse(list1, list2), 2.17)

    # # ----
    # # predict_rating
    # # ----
    def test_predict_1(self):
        """ test predict_rating """
        d_path = "http://www.cs.utexas.edu/users/downing/netflix-cs373/"

        cust_avg_url = d_path + "aji272-CustAverage.pickle"
        movie_avg_url = d_path + "aji272-MovieAverage.pickle"
        year_avg_url = d_path + "aji272-YearAverage.pickle"
        actual_probe_url = d_path + "aji272-Actual.pickle"

        customer_ave = pickle.load(urllib.request.urlopen(cust_avg_url))
        movie_ave = pickle.load(urllib.request.urlopen(movie_avg_url))
        year_ave = pickle.load(urllib.request.urlopen(year_avg_url))

        # with open('ActualRatings.p', 'rb') as actual_file:
        #     actual_averages = pickle.load(actual_file)
        actual_averages = pickle.load(urllib.request.urlopen(actual_probe_url))

        self.assertEqual(predict_rating(30878, 1, movie_ave, customer_ave, year_ave, actual_averages), 3.6835999999999998)

    def test_predict_2(self):
        """ test predict_rating """
        d_path = "http://www.cs.utexas.edu/users/downing/netflix-cs373/"

        cust_avg_url = d_path + "aji272-CustAverage.pickle"
        movie_avg_url = d_path + "aji272-MovieAverage.pickle"
        year_avg_url = d_path + "aji272-YearAverage.pickle"
        actual_probe_url = d_path + "aji272-Actual.pickle"

        customer_ave = pickle.load(urllib.request.urlopen(cust_avg_url))
        movie_ave = pickle.load(urllib.request.urlopen(movie_avg_url))
        year_ave = pickle.load(urllib.request.urlopen(year_avg_url))

        # with open('ActualRatings.p', 'rb') as actual_file:
        #     actual_averages = pickle.load(actual_file)
        actual_averages = pickle.load(urllib.request.urlopen(actual_probe_url))


        self.assertEqual(predict_rating(254775, 10005, movie_ave, customer_ave, year_ave, actual_averages), 3.5124999999999997)

    def test_predict_3(self):
        """ test predict_rating """
        d_path = "http://www.cs.utexas.edu/users/downing/netflix-cs373/"

        cust_avg_url = d_path + "aji272-CustAverage.pickle"
        movie_avg_url = d_path + "aji272-MovieAverage.pickle"
        year_avg_url = d_path + "aji272-YearAverage.pickle"
        actual_probe_url = d_path + "aji272-Actual.pickle"

        customer_ave = pickle.load(urllib.request.urlopen(cust_avg_url))
        movie_ave = pickle.load(urllib.request.urlopen(movie_avg_url))
        year_ave = pickle.load(urllib.request.urlopen(year_avg_url))

        # with open('ActualRatings.p', 'rb') as actual_file:
        #     actual_averages = pickle.load(actual_file)
        actual_averages = pickle.load(urllib.request.urlopen(actual_probe_url))

        self.assertEqual(predict_rating(1892654, 10005, movie_ave, customer_ave, year_ave, actual_averages), 3.9747000000000003)

    # # -----
    # # solve
    # # -----
    def test_solve_1(self):
        """ test solve """
        string_in = StringIO("1:\n30878\n2647871\n1283744\n")
        writer = StringIO()
        netflix_solve(string_in, writer)
        self.assertEqual(writer.getvalue(), "1:\n3.7\n3.3\n3.6\nRMSE: 0.57\n")

    def test_solve_2(self):
        """ test solve """
        string_in = StringIO("10006:\n1093333\n1982605\n1534853\n")
        writer = StringIO()
        netflix_solve(string_in, writer)
        self.assertEqual(writer.getvalue(), "10006:\n3.7\n3.1\n3.9\nRMSE: 1.26\n")

    def test_solve_3(self):
        """ test solve """
        string_in = StringIO("10010:\n1462925\n52050\n650466\n")
        writer = StringIO()
        netflix_solve(string_in, writer)
        self.assertEqual(writer.getvalue(), "10010:\n2.2\n2.0\n2.0\nRMSE: 1.33\n")


# ----
# main
# ----
if __name__ == "__main__":
    main()
