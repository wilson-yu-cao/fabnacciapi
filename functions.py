# Fibonacci number
from os import truncate


def F(n):
    assert n>=0, 'assert n>=0'
    seq = []

    if n == 0:
        seq = [0]
    elif n == 1:
        seq = [0,1]
    elif n > 1 :
        seq = [0,1]
        for i in range(2, n+1):
            seq.append(seq[i-2] + seq[i-1])

    return seq

# Fibonacci number with global cache
# This is only for dev or demo purpose. Such global cache
# may cause unexpected behavior when Flask handles requests using multiple threads. 
# For production, use a memory cache solution.
fib_cache=[]
def F_with_cache(n, page, size):
    assert n>=0, 'assert n>=0'
    assert page>=1, 'assert page>=1'
    assert size>=1, 'assert size>=1'

    global fib_cache

    if len(fib_cache) <= n:
        fib_cache = [str(element) for element in F(n)]
 
    fib_split=fib_cache[:n+1]
    ret=fib_split[(page-1)*size:page*size]
 
    return ret