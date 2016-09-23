'''
    This module provides unit tests for functions in Netflix.
'''
#!/usr/bin/env python3

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_solve, netflix_eval, netflix_print, netflix_cache_load

# -----------
# TestNetflix
# -----------

class TestNetflix(TestCase):
    '''
        TestNetflix serves as our class to hold unit test methods
        to test functions in Netflix.
    '''

    def test_read(self):
        '''
            Test the netflix_read() function, which takes a line
            of input and parses to an int
        '''
        string_input = "55543\n"
        result = netflix_read(string_input)
        self.assertEqual(result, 55543)

    def test_read_2(self):
        '''
            Test the netflix_read() function, which takes a line
            of input and parses to an int
        '''
        string_input = "101\n"
        result = netflix_read(string_input)
        self.assertEqual(result, 101)

    def test_read_3(self):
        '''
            Test the netflix_read() function, which takes a line
            of input and parses to an int
        '''
        string_input = "1337::::\n"
        result = netflix_read(string_input)
        self.assertEqual(result, 1337)

    def test_read_4(self):
        '''
            Test the netflix_read() function, which takes a line
            of input and parses to an int
        '''
        string_input = "100000"
        result = netflix_read(string_input)
        self.assertEqual(result, 100000)

    def test_eval_1(self):
        '''
            Test the netflix_eval() function with movie ID 1
            and customer IDs 1, 2 and 3.
        '''
        netflix_eval_result = netflix_eval(40, [1543642, 1575381], netflix_cache_load())
        self.assertEqual(len(netflix_eval_result), 2)

    def test_eval_2(self):
        '''
            Test the netflix_eval() function with movie ID 2
            and customer IDs 4, 5 and 6.
        '''
        netflix_eval_result = netflix_eval(10005, [2087887, 1917538, 2520477], netflix_cache_load())
        self.assertEqual(len(netflix_eval_result), 3)

    def test_eval_3(self):
        '''
            Test the netflix_eval() function with movie ID 3
            and customer ID 5.
        '''
        netflix_eval_result = netflix_eval(1001, [1050889, 239718], netflix_cache_load())
        self.assertEqual(len(netflix_eval_result), 2)

    def test_eval_4(self):
        '''
            Test the netflix_eval() function with movie ID 4 and
            customer ID 6.
        '''
        netflix_eval_result = netflix_eval(4, [6], netflix_cache_load())
        self.assertEqual(len(netflix_eval_result), 1)

    def test_eval_5(self):
        '''
            Test the netflix_eval() function with movie ID 10 and
            customer ID 9.
        '''
        netflix_eval_result = netflix_eval(4000, [657811], netflix_cache_load())
        self.assertEqual(len(netflix_eval_result), 1)

    def test_eval_6(self):
        '''
            Test the netflix_eval() function with movie ID 12
            and customer IDs 20 and 30.
        '''
        netflix_eval_result = netflix_eval(4001, [1284991, 1388095], netflix_cache_load())
        self.assertEqual(len(netflix_eval_result), 2)

    def test_print(self):
        '''
            Testing the netflix_print() function by passing a StringIO
            object to write to instead of standard out.
        '''
        write_io = StringIO()
        netflix_print(write_io, 1, [10, 20])
        self.assertEqual(write_io.getvalue(), "1:\n10\n20\n")

    def test_print_2(self):
        '''
            Testing the netflix_print() function by passing a StringIO
            object to write to instead of standard out.
        '''
        write_io = StringIO()
        netflix_print(write_io, 10, [1, 20])
        self.assertEqual(write_io.getvalue(), "10:\n1\n20\n")

    def test_print_3(self):
        '''
            Testing the netflix_print() function by passing a StringIO
            object to write to instead of standard out.
        '''
        write_io = StringIO()
        netflix_print(write_io, 20, [1])
        self.assertEqual(write_io.getvalue(), "20:\n1\n")

    def test_print_4(self):
        '''
            Testing the netflix_print() function by passing a StringIO
            object to write to instead of standard out.
        '''
        write_io = StringIO()
        netflix_print(write_io, 21, [1, 5])
        self.assertEqual(write_io.getvalue(), "21:\n1\n5\n")

    def test_solve(self):
        '''
            Testing the netflix_solve() function
        '''
        read_io = StringIO("1:\n317050\n1772839")
        write_io = StringIO()
        netflix_solve(read_io, write_io)
        self.assertEqual(write_io.getvalue(), "1:\n4.9\n5.0\nRMSE: 0.05")

    def test_solve_2(self):
        '''
            Testing the netflix_solve() function
        '''
        read_io = StringIO("10000:\n200206")
        write_io = StringIO()
        netflix_solve(read_io, write_io)
        self.assertEqual(write_io.getvalue(), "10000:\n5.0\nRMSE: 0.0")

    def test_solve_3(self):
        '''
            Testing the netflix_solve() function
        '''
        read_io = StringIO("10:\n1531863")
        write_io = StringIO()
        netflix_solve(read_io, write_io)
        self.assertEqual(write_io.getvalue(), "10:\n3.0\nRMSE: 0.02")

# ----
# main
# ----

if __name__ == "__main__":
    main()
