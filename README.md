

can run in python 3.

Basic Polynomial calculator (only calculates up to degree of 2) python3 main.py "example equation here" "can put another equation here if you like too"

takes in as many strings as you like to try and calculate and returns the degree of equation, the reduced form of the equation, and the answer(s) if they can be calculated.

It requires a certain format input with little flexibility.

    only variable allowed is "X", case sensitive"
    format of each term can be either "+/- integer/float/fraction * X^power" or "+/- X^power" or "+/- number". the programme will fill it the gaps to create the first format if either of the last two formats are given. spaces between number, signs, * and X^power are non-negotiable.
    equation needs to be equal to something e.g. = 0 or = 2 * X^2

