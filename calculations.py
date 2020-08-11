import re

def degree_poly(eqn):
    exponents_list = []
    variables_list = re.findall("X{1}\^{1}[0-9]{1}", eqn)
    if not variables_list:
        return (0)

    for var in variables_list:
        digit = (re.search(r"\d", var)).group()
        exponents_list.append(digit)
    
    highest_exp = 0
    for exp in exponents_list:
        if int(exp) > highest_exp:
            highest_exp = int(exp)
    
    return (highest_exp)

# def reduce_poly(eqn):
#     #some stuff

# def discriminant_poly(eqn):
#     #some stuff

# def solve_poly(eqn):
#     #some stuff