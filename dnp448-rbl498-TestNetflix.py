
from io import StringIO
from unittest import main, TestCase

from Netflix import is_movie, get_user_id, calculate_new_rating


# -----------
# TestCollatz
# -----------

class TestNetflix (TestCase) :

    # ----
    # eval
    # ----
    def test_get_user_id_1(self):
        val = '1417435'
        self.assertEqual(get_user_id(val), 1417435)

    def test_get_user_id_2(self):
        val = '2647871'
        self.assertEqual(get_user_id(val), 2647871)

    def test_get_user_id_3(self):
        val = '1283744'
        self.assertEqual(get_user_id(val), 1283744)

    # --------
    # is_movie
    # --------
    def test_is_movie_1(self):
        val = "1:"
        self.assertEqual(is_movie(val), True)

    def test_is_movie_2(self):
        val = "10183:"
        self.assertEqual(is_movie(val), True)
        
    def test_is_movie_3(self):
        val = "10186:"
        self.assertEqual(is_movie(val), True)

    # ---------------------
    # calculate_new_rating
    # ---------------------
    def test_calculate_new_rating(self):
        userID = 442546
        movieID = 10036
        avg_movie_rating = 3.8279652351738243
        rating = 3.603939158683152
        self.assertEqual(calculate_new_rating(userID, movieID,avg_movie_rating), rating)

    def test_calculate_new_rating_2(self):
        userID = 387679
        movieID = 10036
        avg_movie_rating = 3.8279652351738243
        rating = 5.101470786859496
        self.assertEqual(calculate_new_rating(userID, movieID,avg_movie_rating), rating)

    def test_calculate_new_rating_3(self):
        userID = 76156
        movieID = 10036
        avg_movie_rating = 3.8279652351738243
        rating = 3.7259611482951973
        self.assertEqual(calculate_new_rating(userID, movieID,avg_movie_rating), rating)


  


# ----
# main
# ----
            
if __name__ == "__main__":
    main()