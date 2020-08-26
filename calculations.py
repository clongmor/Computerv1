import re
import helper

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

def reduce_poly(eqn):
    eqn_halves = eqn.split("=")
    l_side = eqn_halves[0]
    r_side = eqn_halves[1]
    r_vars = r_side.split()
    l_vars = l_side.split()

    #makes co-efficients negative as needed
    length_l = len(l_vars)
    length_r = len(r_vars)
    i = 0
    j = 0
    while i < length_l - 1:
        if l_vars[i] == "-" and helper.is_number(l_vars[i + 1]):
            l_vars[i + 1] = str(float(l_vars[i + 1]) * -1)
        i = i + 1
    while j < length_r - 1:
        if r_vars[j] == "-" and helper.is_number(r_vars[j + 1]):
            r_vars[j + 1] = str(float(r_vars[j + 1]) * -1)
        j = j + 1
    
    #does the addition/subtraction of like x power co-efficients
    i = 0
    j = 0
    check = 0
    while j < length_r:
        if re.findall("X{1}\^{1}[0-9]{1}", r_vars[j]):
            while i < length_l:
                if r_vars[j] == l_vars[i]:
                    if r_vars[j - 2].isdigit():
                        r_vars[j - 2] = int(r_vars[j - 2])
                    else:
                        r_vars[j - 2] = float(r_vars[j - 2])
                    if l_vars[i - 2].isdigit():
                        l_vars[i - 2] = int(l_vars[i - 2])
                    else:
                        l_vars[i - 2] = float(l_vars[i - 2])
                    l_vars[i - 2] = str(l_vars[i - 2] - r_vars[j - 2])
                    check = 1
                i = i + 1
            if check == 0:
                l_vars.append(r_vars[j - 2])
                l_vars.append(r_vars[j - 1])
                l_vars.append(r_vars[j])
            check = 0
        j = j + 1

    #converts negative numbers back to positive for printing
    i = 0
    length_l = len(l_vars)
    while i < length_l:
        if helper.is_negative(l_vars[i]):
            try:
                l_vars[i] = str(int(l_vars[i]) * -1)
            except ValueError:
                l_vars[i] = str(float(l_vars[i]) * -1)
        i = i + 1  
    
    l_vars.append("=")
    l_vars.append("0")
    reduced_form = " ".join(l_vars)      
    return (reduced_form)

def discriminant_poly(eqn):
    terms = {
        "a" : 0,
        "b" : 0,
        "c" : 0
    }
    eqn_halves = eqn.split("=")
    l_vars= eqn_halves[0].split()

    #makes co-efficients negative as needed
    length_l = len(l_vars)
    i = 0
    while i < length_l - 1:
        if l_vars[i] == "-" and l_vars[i + 1].isdigit():
            l_vars[i + 1] = str(int(l_vars[i + 1]) * -1)
        elif l_vars[i] == "-" and helper.is_number(l_vars[i + 1]):
            l_vars[i + 1] = str(float(l_vars[i + 1]) * -1)
        i = i + 1
    #pulls out the a b and c coefficients of the equation
    i = 0
    while i < length_l:
        if re.match("X{1}\^{1}[0]{1}", l_vars[i]) and l_vars[i - 2].isdigit():
            terms["c"] = int(l_vars[i - 2])
            terms["clet"] = l_vars[i]
        elif re.match("X{1}\^{1}[0]{1}", l_vars[i]) and helper.is_number(l_vars[i - 2]):
            terms["c"] = float(l_vars[i - 2])
            terms["clet"] = l_vars[i]
        elif re.match("X{1}\^{1}[1]{1}", l_vars[i]) and l_vars[i - 2].isdigit():
            terms["b"] = int(l_vars[i - 2])
            terms["blet"] = l_vars[i]
        elif re.match("X{1}\^{1}[1]{1}", l_vars[i]) and helper.is_number(l_vars[i - 2]):
            terms["b"] = float(l_vars[i - 2])
            terms["blet"] = l_vars[i]
        elif re.match("X{1}\^{1}[2]{1}", l_vars[i]) and l_vars[i - 2].isdigit():
            terms["a"] = int(l_vars[i - 2])
            terms["alet"] = l_vars[i]
        elif re.match("X{1}\^{1}[2]{1}", l_vars[i]) and helper.is_number(l_vars[i - 2]):
            terms["a"] = float(l_vars[i - 2])
            terms["alet"] = l_vars[i]
        i = i + 1

    #calculates the discriminant
    disc = terms["b"]**2 - 4*terms["a"]*terms["c"]
    terms["discriminant"] = disc

    return (terms)

def solve_poly(vars_dict):
    answer_list = helper.quadratic_formula(vars_dict["a"], vars_dict["b"], vars_dict["c"])

    return (answer_list)
    #some stuff