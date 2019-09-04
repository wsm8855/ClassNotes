"""
        Great exam question: can we write this math definition in python? Euclid's GCD algorithm.
        gcd(a,b) = {
                        b = 0: a                    BASE CASE
                        b > 0: gcd(b, a mod b)        RECURSIVE CASE
                    }

        Trace example
        gcd(96, 14) = gcd(14, 96%14)
                    = gcd(14, 12)
                    = gcd(12, 14%12)
                    = gcd(2, 12%2)
                    = gcd(2,0)
                    = 2
"""
"""
    Modulus overview.
    11 % 5 = 1 bc 11/5 = 2 R.1
    12 % 8 = 4 bc 12 / 8 = 1 R.4
    for x, y.
    f x % y. return will be within (0, y-1)
"""


def gcd(a, b):
    if b == 0:
        return a  # worse place to forget a return statement in recursive programming.
    else:
        return gcd(b, (a % b))


def main():
    print(gcd(96, 14))
    print(gcd(11, 5))


"""
    What is this name == main stuff?
    * Proper way to construct main function.
    remember the import command? This makes sure that if this program is run directly, the main runs. If the program
    is imported as a module, the main won't run.
    For example, turtle has a main function, but we don't want to run its main. Usually the mains have test code.
    It's called an "if guard".

"""
if __name__ == '__main__':
    main()
