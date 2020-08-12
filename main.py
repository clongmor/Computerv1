#pulls together all the modules to run the equations and input error checks
import sys
import calculations

args = sys.argv

def main(args):
    if len(args) > 1: #there is actually an input
        for argument in args[1:]:
            #need to check input of equations to be valid
            deg_arg = calculations.degree_poly(argument) #find the degree of the polynomial
            red_arg = calculations.reduce_poly(argument) #reduce/simplify the polynomial equation
            # answer = []
            # if deg_arg <= 2:
            #     disc = discriminant_poly(red_arg) #find the discriminant of the polynomial
            #     answer = solve_poly(red_arg) #use the simplified form of the equation to solve for the answer(s).
            # print "Reduced form: ", red_arg, "\n"
            # print "Polynomial degree: ", deg_arg, "\n"
            # if not answer:
            #     print "The Polynomial degree is strictly greater than 2, I can't solve.\n"
            # elif answer[0] is None:
            #     print "Equation Unsolvable\n" 
            # elif answer[0] and not answer[1]:
            #     print "The soloution is:\n", answer[0], "\n"
            # elif answer[1] and disc > 0: #need to adjust this based on the discriminant
            #     print "Discriminant is strictly positive, the two soloutions are:\n", answer[0], "\n", answer[1], "\n"
            # elif answer[1] and disc == 0:
            #     print "Discriminant is equal to zero with two identical roots, the soloution is:\n", answer[1], "\n"
            # elif answer[1] and disc < 0: #need to factor in imaginary numbers somehow? or just don't handle
            #     print "Discriminant is strictly negative, no real soloutions, the two imaginary soloutions are:\n", answer[0], "\n", answer[1], "\n"
            # else:
            #     print "General Error\n"
            print (deg_arg)
            print (red_arg)
main(args)
print ("The programme is now ending")