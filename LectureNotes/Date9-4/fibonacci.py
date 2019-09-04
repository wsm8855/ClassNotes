"""
    Fibonacci pigeons.
    Basically god mode

    fib(0) = 0
    fib(1) = 1
    fib(2) = 1
    fib(3) = 2
    fib(4) = 3
    fib(5) = 5
    fib(6) = 8

    An example of GENERAL RECURSION.
    (fib could be done as tail or iteration, but requires an accumulator.

    fib(n) = {
                n = 0: 0  } Base cases
                n = 1: 1  }
                n > 1: fib(n-1) + fib(n-2)
            }

    Very inefficient. This is fib(5)
    5
    4
    3
    2
    1
    0
    1
    2
    1
    0
    3
    2
    1
    0
    1
    (24 background computations. nice tree diagram in his notes.)
    5

    The function is not remembering numbers. this means it is recalculating the same number many times.
    Recursion written this way sucks, but recursion itself doesn't suck. Just have to write it right.
"""


def fib(n):
    print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)  # This is what makes it general recursion.


def main():
    print(fib(5))


if __name__ == '__main__':
    main()