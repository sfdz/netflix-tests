""" User test harness for Netflix.py """
#!/usr/bin/env python3

# -------
# imports
# -------

import sys
import pickle

from Netflix import Netflix

# ----
# main
# ----

if __name__ == "__main__":
    
    __cache__ = [[0], [0], [0]]

    # open files
    __file1__ = open(
        "/u/downing/cs/netflix-cs373/jic539_cust_avg.p", 'rb')
    __file2__ = open(
        "/u/downing/cs/netflix-cs373/jic539_movie_avg.p", 'rb')
    __file3__ = open(
        "/u/downing/cs/netflix-cs373/cat3238-actual.p", 'rb')

    # save caches locally
    __cache__[0] = pickle.load(__file1__)
    __cache__[1] = pickle.load(__file2__)
    __cache__[2] = pickle.load(__file3__)

    # close files
    __file1__.close()
    __file2__.close()
    __file3__.close()

    __netflix__ = Netflix()
    __netflix__.netflix_solve(sys.stdin, sys.stdout, __cache__)
