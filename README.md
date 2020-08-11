Think about complex solutions when the degree is worth 2. ;)
•The language is up to you.
•That said, you are not allowed any mathematic function/library (beside additionsand multiplications of real numbers) that you did not implement yourself.
•If you are working in a compilable language (C/C++ for ex) you will submit a Makefile with all the usual rules

Write a program that solves a polynomial equation of degree less than or equal to 2. Youwill need to display at least:
•The reduced form of the equation.
•The degree of the equation.
•Its solution(s), as well as the sign of the discriminant when it makes sense.

$>./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131
$>./computor "5 * X^0 + 4 * X^1 = 4 * X^0"
Reduced form: 1 * X^0 + 4 * X^1 = 0
Polynomial degree: 1
The solution is:-0.25
./computor "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
Polynomial degree: 3
The polynomial degree is stricly greater than 2, I can't solve.

It will always be considered that the input is well formatted, ie.  all terms are of the forma∗x^p. The powers are well ordered and all present. Attention, this does not necessarily mean that the equation is solvable! In this case, your program must detect itand indicate it. Think also of the coefficients that are null, negative, not integers...

There may be special cases that you need to manage. For example, for the following equation 42∗X^0= 42∗X^0, all the real numbers are solution...

discriminant > 0 = 2 distinct real roots
discriminant = 0 = 1 double root
discriminant < 0 = no real roots