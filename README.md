

can run in python 3.

Basic Polynomial calculator (only calculates up to degree of 2) to run:

python computor.py "example equation here" "can put another equation here if you like too"
e.g. python copmutor.py " 3 * X^0 + 2.3 * X^1 - 1 * X^2 = 0"

takes in as many string arguments as you like to try and calculate and returns the degree of equation, the reduced form of the equation, and the answer(s) if they can be calculated.
e.g. python computor.py " 3 * X^0 + 2 * X^1 = X^1"
New Calculation

Reduced form: 3 * X^0 + 1 * X^1 = 0
Polynomial degree: 1
The soloution is:
 -3.0

It requires a certain format input with little flexibility:

    - only variable allowed is "X", case sensitive
    - coefficients of X can be integers, floats or fractions (written as 2/3).
    format of each term can be either "+/- integer/float/fraction * X^power" or "+/- X^power" or "+/- number". 
       the programme will fill it the gaps to create the first format if either of the last two formats are given.
    e.g. - 2 + X = 0 will become - 2 * X^0 + 1 * X^1 = 0
    
       
    spaces between number, signs, * and X^power are non-negotiable. e.g. 2*X^1 will not work since there are no spaces
    equation needs to be equal to something e.g. 2 * X^0 = 0 or 1 = 2 * X^2

