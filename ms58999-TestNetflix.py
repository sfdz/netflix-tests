"""
 Netflix project CS373
 TestNetflix.py
 Madeline Stager
"""

#--------
# imports
#--------

import pickle

from io import StringIO

from unittest import main, TestCase

from Netflix import make_predictions, predict_rating, read_input

#-----------
# TestNetlix
#-----------


class TestNetflix(TestCase):

    """Class for unit tests of  Netflix project"""

    # ----------
    # read_input
    # ----------

    def test_read_input_1(self):
        """Test 1 of read_input() tests one movie id and customer id pair"""

        test_string = StringIO("9150:\n1772361\n")
        movie_id, customer_id = read_input(0, test_string)
        self.assertEqual(movie_id, 9150)
        self.assertEqual(customer_id, 1772361)

    def test_read_input_2(self):
        """Test 2 of read_input() tests one customer id useing previously read movie id"""

        test_string = StringIO("599993\n")
        movie_id, customer_id = read_input(9150, test_string)
        self.assertEqual(movie_id, 9150)
        self.assertEqual(customer_id, 599993)

    def test_read_input_3(self):
        """Test 3 of read_input() tests one movie id and customer id pair"""

        test_string = StringIO("12821:\n1876743\n")
        movie_id, customer_id = read_input(9150, test_string)
        self.assertEqual(movie_id, 12821)
        self.assertEqual(customer_id, 1876743)

    def test_read_input_4(self):
        """Test 4 of read_input() the empyt string as input"""

        test_string = StringIO("")
        movie_id, customer_id = read_input(12821, test_string)
        self.assertEqual(movie_id, -1)
        self.assertEqual(customer_id, -1)

# --------------
# predict_rating
# --------------
    def test_predict_rating_1(self):
        """Test 1 of predict_rating() tests for expected rating prediction"""

        # load all caches necessary for testing
        with open('/u/downing/public_html/netflix-cs373/cat3238-years.p', 'rb') as year_cache:
            movie_years = pickle.load(year_cache)
        with open('/u/downing/public_html/netflix-cs373/cat3238-customer.p', 'rb') as cust_cache:
            customer_year_ratings = pickle.load(cust_cache)
        with open('/u/downing/public_html/netflix-cs373/cat3238-movie.p', 'rb') as movie_cache:
            movie_ratings = pickle.load(movie_cache)

        movie_id, customer_id = 9150, 1772361
        rating = predict_rating(
            movie_id, customer_id, movie_years, movie_ratings, customer_year_ratings)
        self.assertEqual(rating, 4.8)

    def test_predict_rating_2(self):
        """Test 2 of predict_rating() tests for expected rating prediction"""

        # load all caches necessary for testing
        with open('/u/downing/public_html/netflix-cs373/cat3238-years.p', 'rb') as year_cache:
            movie_years = pickle.load(year_cache)
        with open('/u/downing/public_html/netflix-cs373/cat3238-customer.p', 'rb') as cust_cache:
            customer_year_ratings = pickle.load(cust_cache)
        with open('/u/downing/public_html/netflix-cs373/cat3238-movie.p', 'rb') as movie_cache:
            movie_ratings = pickle.load(movie_cache)

        movie_id, customer_id = 1, 30878
        rating = predict_rating(
            movie_id, customer_id, movie_years, movie_ratings, customer_year_ratings)
        self.assertEqual(rating, 4.2)

    def test_predict_rating_3(self):
        """Test 3 of predict_rating() tests for another user of previously tested movie"""

        # load all caches necessary for testing
        with open('/u/downing/public_html/netflix-cs373/cat3238-years.p', 'rb') as year_cache:
            movie_years = pickle.load(year_cache)
        with open('/u/downing/public_html/netflix-cs373/cat3238-customer.p', 'rb') as cust_cache:
            customer_year_ratings = pickle.load(cust_cache)
        with open('/u/downing/public_html/netflix-cs373/cat3238-movie.p', 'rb') as movie_cache:
            movie_ratings = pickle.load(movie_cache)

        movie_id, customer_id = 9150, 599993
        rating = predict_rating(
            movie_id, customer_id, movie_years, movie_ratings, customer_year_ratings)
        self.assertEqual(rating, 3.9)

# ----------------
# make_predictions
# ----------------

    def test_make_predictions_1(self):
        """Test 1 of make_predictions() tests three movies with a
            couple customers and test rating are rounded properly if above 5.0"""

        test_string = StringIO(
            "9150:\n1772361\n599993\n12821:\n1876743\n9996:\n66828\n")
        test_output = StringIO()
        make_predictions(test_string, test_output)
        self.assertEqual(
            test_output.getvalue(), "9150:\n4.8\n3.9\n12821:\n2.7\n9996:\n5.0\nRMSE: 1.02\n")

    def test_make_predictions_2(self):
        """Test 2 of make_predictions() tests two movies with a couple customers each"""

        test_string = StringIO(
            "10:\n1952305\n1531863\n10001:\n262828\n2609496\n1474804\n")
        test_output = StringIO()
        make_predictions(test_string, test_output)
        self.assertEqual(
            test_output.getvalue(), "10:\n3.4\n3.4\n10001:\n4.1\n4.9\n3.9\nRMSE: 0.48\n")


if __name__ == "__main__":
    main()
