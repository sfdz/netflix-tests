
"""
TestNetflix.py
    Tests Netflix.py for correct functionality
    Unit Testing
"""

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt
# pylint: disable=too-many-public-methods

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import read_probe, eval_probe, print_probe, solve_probe
from Netflix import get_predicted_rating, calculate_rmse, print_rmse


class TestNetflix(TestCase):

    """
    Unit tests for Netflix.py
    """

    def test_read_probe_1(self):
        """
        test read given a line with a movie_id
        """
        line = "2034:\n"
        i, j = read_probe(line)
        self.assertEqual(i, 2034)
        self.assertEqual(j, True)

    def test_read_probe_2(self):
        """
        test read given a line with a customer_id
        """
        line = "1417435\n"
        i, j = read_probe(line)
        self.assertEqual(i, 1417435)
        self.assertEqual(j, False)

    def test_read_probe_3(self):
        """
        test read given a line with a customer_id
        """
        line = "2312054\n"
        i, j = read_probe(line)
        self.assertEqual(i, 2312054)
        self.assertEqual(j, False)

    def test_eval_probe_1(self):
        """
        test eval given a movie_id, customer_id, and list of values
        minimum predicted rating should be 1
        """
        movie = 2034
        customer = 348443
        caches = [{movie: {customer: 3}},
                  {customer: {2000: -2.5}}, {movie: -.5}, {movie: 2000}, 3]
        values = []
        predicted_rating, values = eval_probe(movie, customer, values, caches)
        self.assertEqual(predicted_rating, 1.0)
        self.assertEqual(len(values), 1)
        self.assertEqual(values[0], 4.0)

    def test_eval_probe_2(self):
        """
        test eval given a movie_id, customer_id, and list of values
        """
        movie = 11536
        customer = 157473
        caches = [{movie: {customer: 3}}, {
            customer: {1995: .4}}, {movie: -.2}, {movie: 1995}, 3]
        values = []
        predicted_rating, values = eval_probe(movie, customer, values, caches)
        self.assertEqual(predicted_rating, 3.2)
        self.assertEqual(len(values), 1)
        self.assertEqual(values[0], 0.04000000000000007)

    def test_eval_probe_3(self):
        """
        test eval given a movie_id, customer_id, and list of values
        maximum predicted rating should be 5
        """
        movie = 11533
        customer = 223257
        caches = [{movie: {customer: 2}},
                  {customer: {2001: 1.5}}, {movie: 1.5}, {movie: 2001}, 3]
        values = []
        predicted_rating, values = eval_probe(movie, customer, values, caches)
        self.assertEqual(predicted_rating, 5.0)
        self.assertEqual(len(values), 1)
        self.assertEqual(values[0], 9.0)

    def test_print_probe_1(self):
        """
        test print for a customer_id
        """
        writer = StringIO()
        customer_id = 704465
        print_probe(customer_id, writer)
        self.assertEqual(writer.getvalue(), "704465\n")

    def test_print_probe_2(self):
        """
        test print for movie_id
        """
        writer = StringIO()
        movie_id = "12021:"
        print_probe(movie_id, writer)
        self.assertEqual(writer.getvalue(), "12021:\n")

    def test_print_probe_3(self):
        """
        test print for movie_id
        """
        writer = StringIO()
        movie_id = "742:"
        print_probe(movie_id, writer)
        self.assertEqual(writer.getvalue(), "742:\n")

    def test_print_rmse_1(self):
        """
        test print for rounded up rmse to 2 decimal places
        """
        writer = StringIO()
        rmse = 0.799535646
        print_rmse(rmse, writer)
        self.assertEqual(writer.getvalue(), "RMSE: 0.80\n")

    def test_print_rmse_2(self):
        """
        test print for rounded up rmse to 2 decimal places
        """
        writer = StringIO()
        rmse = 0.80
        print_rmse(rmse, writer)
        self.assertEqual(writer.getvalue(), "RMSE: 0.80\n")

    def test_print_rmse_3(self):
        """
        test print for rounded up rmse to 2 decimal places
        """
        writer = StringIO()
        rmse = 0.8001
        print_rmse(rmse, writer)
        self.assertEqual(writer.getvalue(), "RMSE: 0.80\n")

    def test_solve_probe_1(self):
        """
        test predicted_rating for 3 customers and rmse
        """
        reader = StringIO("7421:\n1459122\n859476\n823164")
        writer = StringIO()
        caches = [{7421: {1459122: 2, 859476: 3, 823164: 3}},
                  {1459122: {1995: 0.4}, 859476: {1995: 0.5},
                   823164: {1995: 0.2}},
                  {7421: -.2},
                  {7421: 1995},
                  3]
        solve_probe(reader, writer, caches)
        self.assertEqual(
            writer.getvalue(), "7421:\n3.2\n3.3\n3.0\nRMSE: 0.71\n")

    def test_solve_probe_2(self):
        """
        test predicted_rating for 3 customers and rmse
        """
        reader = StringIO("680:\n1118974\n145640\n907840")
        writer = StringIO()
        caches = [{680: {1118974: 4, 145640: 2, 907840: 5}},
                  {1118974: {1995: 0.2}, 145640:
                   {1995: 0.1}, 907840: {1995: 0.5}},
                  {680: -0.6},
                  {680: 1995},
                  3]
        solve_probe(reader, writer, caches)
        self.assertEqual(
            writer.getvalue(), "680:\n2.6\n2.5\n2.9\nRMSE: 1.49\n")

    def test_solve_probe_3(self):
        """
        test predicted_rating for 5 customers and rmse
        """
        reader = StringIO("4563:\n1676257\n1107756\n185124\n1840435")
        writer = StringIO()
        caches = [{4563: {1676257: 1, 1107756: 3, 185124: 2, 1840435: 3}},
                  {1676257: {2006: 0.3}, 1107756: {2006: 1.0},
                   185124: {2006: 0.9}, 1840435: {2006: 0.6}},
                  {4563: 0.8},
                  {4563: 2006},
                  2]
        solve_probe(reader, writer, caches)
        self.assertEqual(
            writer.getvalue(), "4563:\n3.1\n3.8\n3.7\n3.4\nRMSE: 1.42\n")

    def test_get_predicted_rating_1(self):
        """
        test predicted_rating given weighted movie average
        and weighted customer average
        """
        movie_average = -0.4
        customer_average = 1
        total_average = 3
        predicted_rating = get_predicted_rating(
            movie_average, customer_average, total_average)
        self.assertEqual(predicted_rating, 3.6)

    def test_get_predicted_rating_2(self):
        """
        test predicted_rating given weighted movie average
        and weighted customer average
        """
        movie_average = 1.0
        customer_average = -0.5
        total_average = 2
        predicted_rating = get_predicted_rating(
            movie_average, customer_average, total_average)
        self.assertEqual(predicted_rating, 2.5)

    def test_get_predicted_rating_3(self):
        """
        test predicted_rating given weighted movie average
        and weighted customer average
        """
        movie_average = 0.2
        customer_average = 2.3
        total_average = 1
        predicted_rating = get_predicted_rating(
            movie_average, customer_average, total_average)
        self.assertEqual(predicted_rating, 3.5)

    def test_calculate_rmse_1(self):
        """
        test calculate rmse given array of (predicted - actual)**2
        """
        values = [0.1365096276428999,
                  0.2248974339188119, 0.0, 1.0785035366365043]
        rmse = calculate_rmse(values)
        self.assertEqual(rmse, 0.5999813743355322)

    def test_calculate_rmse_2(self):
        """
        test calculate rmse given array of (predicted - actual)**2
        """
        values = [0.6637788008032236, 0.4687879615111395,
                  0.0, 2.2970110060604143, 0.4419325366215253]
        rmse = calculate_rmse(values)
        self.assertEqual(rmse, 0.8799443510809423)

    def test_calculate_rmse_3(self):
        """
        test calculate rmse given array of (predicted - actual)**2
        """
        values = [1.8019814874492273]
        rmse = calculate_rmse(values)
        self.assertEqual(rmse, 1.3423790401556586)


if __name__ == "__main__":
    main()
