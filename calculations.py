import re
import helper

def degree_poly(eqn):
    exponents_list = []
    var_list1 = re.findall("X{1}\^{1}[0-9]", eqn)
    var_list2 = re.findall("X{1}\s", eqn)
    i = 0
    while i < len(var_list2):
        var_list2[i] = var_list2[i].strip() + "^1"
        i += 1
    variables_list = var_list1 + var_list2
    eqn_halves = eqn.split("=")
    if not variables_list and (eqn_halves[0].strip() != eqn_halves[1].strip()):
        print("no soloution")
        return (-1)

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

    #adds powers to reduced X's
    i = 0
    while i < len(r_vars):
        x = re.search('X$', r_vars[i])
        if x != None:
            r_vars[i] = r_vars[i] + "^1"
        i += 1
    i = 0
    while i < len(l_vars):
        x = re.search('X$', l_vars[i])
        if x != None:
            l_vars[i] = l_vars[i] + "^1"
        i += 1

    #makes co-efficients negative as needed and adds in co-efficients and * where non-existent
    length_l = len(l_vars)
    length_r = len(r_vars)
    i = 0
    j = 0
    if length_l == 1 and re.findall("X{1}\^{1}[0-9]", l_vars[i]):
        l_vars.insert(i, "*")
        l_vars.insert(i, "1")
        length_l += 2
    elif helper.is_number(l_vars[i]) and length_l == 1 and l_vars[i] != "0":
        l_vars.insert(i + 1, "X^0")
        l_vars.insert(i + 1, "*")
        length_l += 2
    while i < length_l - 1:
        if i == 0 and re.findall("X{1}\^{1}[0-9]", l_vars[i]):
            l_vars.insert(i, "*")
            l_vars.insert(i, "1")
            length_l += 2
        elif re.findall("(-?\d+)\/(\d+)", l_vars[i]):
            digits = l_vars[i]. split("/")
            decimal = int(digits[0]) / int(digits[1])
            l_vars[i] = str(decimal)
            if i > 0 and l_vars[i - 1] == "-":
                l_vars[i] = str(helper.to_negative(l_vars[i]))
        elif helper.is_number(l_vars[i]) and l_vars[i + 1] != "*" and l_vars[i] != "0":
            l_vars.insert(i + 1, "X^0")
            l_vars.insert(i + 1, "*")
            length_l += 2
        elif l_vars[i] == "-" and helper.is_number(l_vars[i + 1]):
            l_vars[i + 1] = str(helper.to_negative(l_vars[i + 1]))
        elif l_vars[i] == "-" and re.findall("X{1}\^{1}[0-9]", l_vars[i + 1]):
            l_vars.insert(i + 1, "*")
            l_vars.insert(i + 1, "-1")
            length_l += 2
        elif l_vars[i] == "+" and re.findall("X{1}\^{1}[0-9]", l_vars[i + 1]):
            l_vars.insert(i + 1, "*")
            l_vars.insert(i + 1, "1")
            length_l += 2
        i = i + 1
    if length_r == 1 and re.findall("X{1}\^{1}[0-9]", r_vars[j]):
        r_vars.insert(j, "*")
        r_vars.insert(j, "1")
        length_r += 2
    elif helper.is_number(r_vars[j]) and length_r == 1 and r_vars[j] != "0":
        r_vars.insert(j + 1, "X^0")
        r_vars.insert(j + 1, "*")
        length_r += 2
    while j < length_r - 1:
        if j == 0 and re.findall("X{1}\^{1}[0-9]", r_vars[j]):
            r_vars.insert(j, "*")
            r_vars.insert(j, "1")
            length_r += 2
        elif re.findall("(-?\d+)\/(\d+)", r_vars[j]):
            digits = r_vars[j]. split("/")
            decimal = int(digits[0]) / int(digits[1])
            r_vars[j] = str(decimal)
            if j > 0 and r_vars[j - 1] == "-":
                r_vars[j] = str(helper.to_negative(r_vars[j]))
        elif helper.is_number(r_vars[j]) and r_vars[j + 1] != "*" and r_vars[j] != "0":
            r_vars.insert(j + 1, "X^0")
            r_vars.insert(j + 1, "*")
            length_r += 2
        elif r_vars[j] == "-" and helper.is_number(r_vars[j + 1]):
            r_vars[j + 1] = str(helper.to_negative(r_vars[j + 1]))
        elif r_vars[j] == "-" and re.findall("X{1}\^{1}[0-9]", r_vars[j + 1]):
            r_vars.insert(j + 1, "*")
            r_vars.insert(j + 1, "-1")
            length_r += 2
        elif r_vars[j] == "+" and re.findall("X{1}\^{1}[0-9]", r_vars[j + 1]):
            r_vars.insert(j + 1, "*")
            r_vars.insert(j + 1, "1")
            length_r +=2
        j = j + 1
    
    #checks for similar terms on the left side only an adjusts co-efficients
    j = 0

    while j < length_l:
        if re.findall("X{1}\^{1}[0-9]", l_vars[j]):
            i = 0
            while i < length_l:
                if i == j:
                    i += 1
                    continue
                elif l_vars[j] == l_vars[i]:
                    if l_vars[j - 2].isdigit() and "*" in l_vars[j - 1]:
                        l_vars[j - 2] = int(l_vars[j - 2])
                    elif helper.is_negative(l_vars[j - 2]) and "*" in l_vars[j - 1]:
                        try:
                            l_vars[j - 2] = int(l_vars[j - 2])
                        except ValueError:
                            l_vars[j - 2] = float(l_vars[j - 2])
                    elif helper.is_number(l_vars[j - 2]) and "*" in l_vars[j - 1]:
                        l_vars[j - 2] = float(l_vars[j - 2])
                    elif helper.is_number(l_vars[j - 2]) == False and "*" in l_vars[j - 1]:
                        print("On the left side of the equation, co-efficient of", l_vars[j], "is not a number.")
                        return (-1)
                    if l_vars[i - 2].isdigit() and "*" in l_vars[i - 1]:
                        l_vars[i - 2] = int(l_vars[i - 2])
                    elif helper.is_negative(l_vars[i - 2]) and "*" in l_vars[i - 1]:
                        try:
                            l_vars[i - 2] = int(l_vars[i - 2])
                        except ValueError:
                            l_vars[i - 2] = float(l_vars[i - 2])
                    elif helper.is_number(l_vars[i - 2]) and "*" in l_vars[i - 1]:
                        l_vars[i - 2] = float(l_vars[i - 2])
                    elif helper.is_number(l_vars[i - 2]) == False and "*" in l_vars[i - 1]:
                        print("On the left side of the equation, co-efficient of", l_vars[i], "is not a number.")
                        return (-1)
                    l_vars[j - 2] = str(l_vars[i - 2] + l_vars[j - 2])
                    del l_vars[i - 3:i + 1]
                    length_l -= 4
                i = i + 1
        j = j + 1

    #does the addition/subtraction of like x power co-efficients across both sides of equation
    i = 0
    j = 0
    check = 0

    while j < length_r:
        if re.findall("X{1}\^{1}[0-9]", r_vars[j]):
            while i < length_l:
                if r_vars[j] == l_vars[i]:
                    if r_vars[j - 2].isdigit() and "*" in r_vars[j - 1]:
                        r_vars[j - 2] = int(r_vars[j - 2])
                    elif helper.is_negative(r_vars[j - 2]) and "*" in r_vars[j - 1]:
                        try:
                            r_vars[j - 2] = int(r_vars[j - 2])
                        except ValueError:
                            r_vars[j - 2] = float(r_vars[j - 2])
                    elif helper.is_number(r_vars[j - 2]) and "*" in r_vars[j - 1]:
                        r_vars[j - 2] = float(r_vars[j - 2])
                    elif helper.is_number(r_vars[j - 2]) == False and "*" in r_vars[j - 1]:
                        print("On the right side of the equation, co-efficient of", r_vars[j], "is not a number.")
                        return (-1)
                    if l_vars[i - 2].isdigit() and "*" in l_vars[i - 1]:
                        l_vars[i - 2] = int(l_vars[i - 2])
                    elif helper.is_negative(l_vars[i - 2]) and "*" in l_vars[i - 1]:
                        try:
                            l_vars[i - 2] = int(l_vars[i - 2])
                        except ValueError:
                            l_vars[i - 2] = float(l_vars[i - 2])
                    elif helper.is_number(l_vars[i - 2]) and "*" in l_vars[i - 1]:
                        l_vars[i - 2] = float(l_vars[i - 2])
                    elif helper.is_number(l_vars[i - 2]) == False and "*" in l_vars[i - 1]:
                        print("On the left side of the equation, co-efficient of", l_vars[i], "is not a number.")
                        return (-1)
                    l_vars[i - 2] = str(l_vars[i - 2] - r_vars[j - 2])
                    r_vars[j - 2] = "0"
                    check = 1
                i = i + 1
            if check == 0:
                if r_vars[j - 2][0] == "-":
                    l_vars.append("-")
                else:
                    l_vars.append("+")
                l_vars.append(r_vars[j - 2])
                l_vars.append(r_vars[j - 1])
                l_vars.append(r_vars[j])
            check = 0
        j = j + 1
    #converts negative numbers back to positive for printing
    i = 0
    length_l = len(l_vars)
    while i < length_l:
        if helper.is_negative(l_vars[i]) and (i == 0 or l_vars[i - 1] != "-"):
            try:
                l_vars[i] = str(int(l_vars[i]) * -1)
                l_vars.insert(i, "-")
                length_l += 1
                i += 1
            except ValueError:
                l_vars[i] = str(float(l_vars[i]) * -1)
                l_vars.insert(i, "-")
                length_l += 1
                i += 1
        elif not helper.is_negative(l_vars[i]) and l_vars[i - 1] == "-":
            if not i - 1 == 0:
                l_vars[i - 1] = "+"
            else:
                del l_vars[i - 1]
                length_l -= 1
        i = i + 1  
    
    #removes any terms with co-efficient of zero
    i = 0
    while i < length_l:
        if length_l == 1 and l_vars[i] == "0":
            break
        if (l_vars[i] == "0" or l_vars[i] == "0.0") and l_vars[i + 1] == "*":
            del l_vars[i:i + 3]
            length_l -= 3
        i += 1
    if not l_vars:
        l_vars.append("0")
    
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
    l_vars = eqn_halves[0].split()

    #makes co-efficients negative as needed
    length_l = len(l_vars)
    i = 0
    while i < length_l - 1:
        if l_vars[i] == "-" and helper.is_number(l_vars[i + 1]):
            l_vars[i + 1] = str(helper.to_negative(l_vars[i + 1]))
        i = i + 1
    
    #pulls out the a b and c coefficients of the equation
    i = 0
    while i < length_l:
        if re.match("X{1}\^{1}[0]{1}", l_vars[i]) and (l_vars[i - 2].isdigit() or (l_vars[i - 2][0] == "-" and l_vars[i - 2][1:].isdigit())):
            terms["c"] = int(l_vars[i - 2])
        elif re.match("X{1}\^{1}[0]{1}", l_vars[i]) and helper.is_number(l_vars[i - 2]):
            terms["c"] = float(l_vars[i - 2])
        elif re.match("X{1}\^{1}[1]{1}", l_vars[i]) and (l_vars[i - 2].isdigit() or (l_vars[i - 2][0] == "-" and l_vars[i - 2][1:].isdigit())):
            terms["b"] = int(l_vars[i - 2])
        elif re.match("X{1}\^{1}[1]{1}", l_vars[i]) and helper.is_number(l_vars[i - 2]):
            terms["b"] = float(l_vars[i - 2])
        elif re.match("X{1}\^{1}[2]{1}", l_vars[i]) and (l_vars[i - 2].isdigit() or (l_vars[i - 2][0] == "-" and l_vars[i - 2][1:].isdigit())):
            terms["a"] = int(l_vars[i - 2])
        elif re.match("X{1}\^{1}[2]{1}", l_vars[i]) and helper.is_number(l_vars[i - 2]):
            terms["a"] = float(l_vars[i - 2])
        i = i + 1

    #calculates the discriminant
    disc = terms["b"]**2 - 4*terms["a"]*terms["c"]
    terms["discriminant"] = disc

    return (terms)

def solve_poly(vars_dict):
    answer_list = helper.quadratic_formula(vars_dict["a"], vars_dict["b"], vars_dict["c"])

    return (answer_list)
    #some stuff