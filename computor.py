#pulls together all the modules to run the equations and input error checks
import sys
import calculations
import helper

args = sys.argv

def main(args):
    if len(args) > 1: #there is actually an input
        for argument in args[1:]:
            print ("New Calculation\n")
            check = helper.error_checks(argument)
            if check == -1:
                continue
            #need to check input of equations to be valid
            deg_arg = calculations.degree_poly(argument)
            if deg_arg == -1:
                continue #find the degree of the polynomial
            red_arg = calculations.reduce_poly(argument)
            if red_arg == -1:
                continue
            answer = []
            if deg_arg <= 2:
                terms = calculations.discriminant_poly(red_arg) #find the discriminant of the polynomial
                if terms == -1:
                    continue
                disc = terms["discriminant"]
                answer = calculations.solve_poly(terms) #use the simplified form of the equation to solve for the answer(s).
            print ("Reduced form:", red_arg)
            print ("Polynomial degree:", deg_arg)
            if not answer:
                print ("The Polynomial degree is strictly greater than 2, I can't solve.")
            elif answer[0] is None:
                print ("Equation Unsolvable")
            elif answer[0] == answer[1]:
                print ("The soloution is:\n", answer[0])
            elif answer[1] and disc > 0: #need to adjust this based on the discriminant
                print ("Discriminant is strictly positive, the two soloutions are:\n", answer[0], "\n", answer[1])
            elif answer[1] and disc == 0:
                print ("Discriminant is equal to zero with two identical roots, the soloution is:\n", answer[1])
            elif answer[1] and disc < 0: #need to factor in imaginary numbers somehow? or just don't handle
                print ("Discriminant is strictly negative, no real soloutions, the two imaginary soloutions are:\n", answer[0], "\n", answer[1])
            else:
                print ("General Error")
main(args)