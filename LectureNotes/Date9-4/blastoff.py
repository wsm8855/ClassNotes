"""
    Tail Recursion.
"""


def blastoff_iter():
    for i in range(5, 0, -1):
        print(i)
    print("Blast off!")


def blastoff_rec(i):  # Tail recursion
    """ Last thing you do is call yourself recursively, and there is no return, it's tail recursion
    if there are any instructions after that last recursive call, it's not tail recursive.
    Tail recursion can easily be converted to iteration.
    def TAIL RECURSION. last thing is to call itself recursively."""
    if i < 1:
        print("Blast off!")
    else:
        print(i)
        blastoff_rec(i-1)


def main():
    # blastoff_iter()
    blastoff_rec(5)


if __name__ == '__main__':
    main()