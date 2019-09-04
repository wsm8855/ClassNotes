"""
    Recursive trees!
    First without recursion, then with recursion because we don't hate ourselves that much yet.

    Step 1: make draw_tree_1
    step 2: draw_tree_2
        - draw a green main branch.
        - uses draw_tree_1 to draw sub-branches
    Step 3: draw_tree_3
        - draw a purple main branch
        - draw_tree_2 to draw subbranches

    Recursive translation:
    This is our recursive case.
    def draw_tree_3(length):     ////  1. draw_tree_rec(length, depth)

        //////////////////////
        BASE CASE
        if depth == 0:
            pass
        else:
            (stuff below)
        //////////////////////

        turtle.color('purple')
        turtle.forward(length)
        turtle.left(45)
        draw_tree_2(length/2) ///// draw_tree_rec(length/2)
        turtle.right(90)
        draw_tree_2(length/2) ///// draw_tree_rec(length/2)
        turtle.left(45)
        turtle.color('purple')
        turtle.backward(length)

    1. Need one more argument, depth.
    2. Need base case.
    Nice!

    One more layer of complexity.
    Let's calculate the total amount of 'wood' in this tree.
    'Fruitfull function' Recursivelly compute total wood (length) used.

    made some changes to the structure.
    How would a recursive boss do this?
    different from fib, turtle has state
"""

import turtle


def init():
    turtle.left(90) # turtle north
    turtle.pensize(3)
    turtle.speed(100)


def draw_tree_1(length):
    turtle.forward(length)
    turtle.backward(length)


def draw_tree_2(length):
    turtle.forward(length)
    turtle.left(45)
    draw_tree_1(length/2)
    turtle.right(90)
    draw_tree_1(length/2)
    turtle.left(45)
    turtle.backward(length)


def draw_tree_3(length):
    turtle.forward(length)
    turtle.left(45)
    draw_tree_2(length/2)
    turtle.right(90)
    draw_tree_2(length/2)
    turtle.left(45)
    turtle.backward(length)


COLORS = ('orange', 'green', 'purple', 'pink', 'blue', 'red')


def draw_tree_rec(length, depth):
    wood = 0
    if depth != 0:
        turtle.color(COLORS[depth % len(COLORS)])
        turtle.forward(length)
        wood += length
        turtle.left(45)
        wood += draw_tree_rec(length / 2, depth - 1)
        turtle.right(90)
        wood += draw_tree_rec(length / 2, depth - 1)
        turtle.left(45)
        turtle.color(COLORS[depth % len(COLORS)])
        turtle.backward(length)
    return wood


def main():
    init()
    print(draw_tree_rec(200, 7))
    turtle.mainloop()


if __name__ == '__main__':
    main()