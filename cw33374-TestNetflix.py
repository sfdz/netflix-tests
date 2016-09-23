"""Unit tests for the methods defined in Netflix.py"""

# -------
# imports
# -------

from unittest import main, TestCase
from io import StringIO
import Netflix

# -----------
# TestNetflix
# -----------


class ConstantPredictor:  # pylint: disable=too-few-public-methods

    """ This predictor always returns the same value for all user/movies """

    def __init__(self, rating):
        """ Constructs a ConstantPredictor

        Params:
            rating: the constant to return for all predictions

        """
        self.rating = rating

    def predict(self, _user, _movie):
        """ Predicts the rating for a user """
        return self.rating


def answers():
    """ Generates some sample answers """
    test_answers = {}
    test_answers[1] = {}
    test_answers[1][1] = 4
    test_answers[2] = {}
    test_answers[2][1] = 5
    test_answers[2][2] = 4
    return test_answers


class TestNetflix(TestCase):

    """Provide unit tests for each method in Netflix.py"""

    def test_answer_cache(self):
        """ Tests that the AnswerCache returns the actual ratings"""
        cache = Netflix.AnswerCache(answers())

        self.assertEqual(cache.predict(1, 1), 4)
        self.assertEqual(cache.predict(1, 2), 5)
        self.assertEqual(cache.predict(2, 2), 4)

    def test_answer_cache_invalid_movie(self):
        """ Tests handling invalid movie """
        cache = Netflix.AnswerCache(answers())

        with self.assertRaises(KeyError):
            cache.predict(1, 3)

    def test_answer_cache_invalid_user(self):
        """ Tests handling invalid user """
        cache = Netflix.AnswerCache(answers())

        with self.assertRaises(KeyError):
            cache.predict(5, 1)

    def test_run_constant_predictor(self):
        """ Tests the input and output formats of run()"""
        reader = StringIO("1:\n1\n2\n3\n")
        writer = StringIO()
        predictor = ConstantPredictor(1)
        answer = ConstantPredictor(2)
        Netflix.run(reader, writer, predictor, answer)
        self.assertEqual(writer.getvalue(), "1:\n1.0\n1.0\n1.0\nRMSE: 1.00\n")

    def test_run_math_predictor(self):
        """ Tests run() using the MathPredictor """
        reader = StringIO("1:\n1\n2\n3\n")
        writer = StringIO()
        predictor = Netflix.MathPredictor(
            {1: 2.5}, {1: 1.0}, {1: 0, 2: 1, 3: -1})
        answer = ConstantPredictor(3)

        Netflix.run(reader, writer, predictor, answer)
        self.assertEqual(writer.getvalue(), "1:\n2.5\n3.5\n1.5\nRMSE: 0.96\n")

    def test_math_predictor_1(self):
        """ Tests that the MathPredictor does the correct math """
        predictor = Netflix.MathPredictor(
            {1: 2.5}, {1: 1.0}, {1: 0, 2: 1, 3: -1})
        self.assertEqual(predictor.predict(1, 1), 2.5)

    def test_math_predictor_2(self):
        """ Tests that the MathPredictor does the correct math with adjustments """
        predictor = Netflix.MathPredictor(
            {1: 2.5}, {1: 1.0}, {1: 0, 2: 1, 3: -1})
        self.assertEqual(predictor.predict(2, 1), 3.5)

    def test_math_predictor_no_user(self):
        """ Tests handling invalid user """
        predictor = Netflix.MathPredictor(
            {1: 2.5}, {1: 1.0}, {1: 0, 2: 1, 3: -1})

        with self.assertRaises(KeyError):
            predictor.predict(4, 1)

    def test_math_predictor_no_movie(self):
        """ Tests handling invalid movie """
        predictor = Netflix.MathPredictor(
            {1: 2.5}, {1: 1.0}, {1: 0, 2: 1, 3: -1})

        with self.assertRaises(KeyError):
            predictor.predict(1, 2)

# ----
# main
# ----

if __name__ == "__main__":
    main()
