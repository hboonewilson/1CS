# fib() is basic recursive Fibonacci, while fib2() uses caching.
# 
# Try fib(37), maybe fib(38).  On most computers fib(38) will be pretty slow.
# fib(50) won't finish while you wait ...
# The problem is unnecessary recomputation.
# To compute fib(8) the code computes fib(6) and fib(7) but in computing
# fib(7) if totally "ignores" the fact that we just computed it and
# recomputes it again from scratch. This "recomputing" happens A LOT and
# yield super inefficent exponential time code.
#
# Now try fib2(50). It should return nearly instantly. It is still
# recursive; it just doesn't do unnecessary recomputation. It "caches"
# values received from recursive calls so that if needed again, they
# can simply be looked up rather than recomputed. 
#
import time
def fib(n):
    result = 0
    if (n == 1) or (n == 2):
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


fibCache = [0,1,1]

def fib2(n):
    # before doing lots work check cache to see if we already know answer
    if n < len(fibCache):
        return fibCache[n]

    # identical to fib code above
    result = 0
    if (n == 1) or (n == 2):
        result = 1
    else:
        result = fib2(n-1) + fib2(n-2)

    #add new result to cache
    fibCache.append(result)
    
    return result
