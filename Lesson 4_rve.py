import re
import string
def matrix(m, n):
    col = []
    for m in xrange(3):
        row = []
        for n in xrange(3):
            row.append(0)
        col.append(m)
        return col
    print col
