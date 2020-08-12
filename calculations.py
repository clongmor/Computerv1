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

def reduce_poly(eqn):
    eqn_halves = eqn.split("=")
    l_side = eqn_halves[0]
    r_side = eqn_halves[1]
    r_components = re.split("\+|-", r_side)
    l_components = re.split("\+|-", l_side)

    l_vars = []
    r_vars = []
    for var in r_components:
        item = var
        r_vars.append(item.split("*"))
    for var2 in l_components:
        item = var2
        l_vars.append(item.split("*"))

    reduced_form = []
    new_list = []
    length_l = len(l_vars)
    length_r = len(r_vars)
    i = 0
    j = 0
    while j < length_r:
        r_vars[j][0] = r_vars[j][0].strip()
        r_vars[j][1] = r_vars[j][1].strip()
        j = j + 1
    while i < length_l:
        l_vars[i][0] = l_vars[i][0].strip()
        l_vars[i][1] = l_vars[i][1].strip()
        i = i + 1
    i = 0
    j = 0
    print(r_vars)
    print(l_vars)
    while j < length_r:
        while i <= length_l:
            if i == length_l:
                new_list.append(r_vars[j][0])
                new_list.append(r_vars[j][1])
                reduced_form.append(new_list)
                new_list = []
            elif r_vars[j][1] == l_vars[i][1]:
                new_list.append(str(int(l_vars[i][0]) - int(r_vars[j][0])))
                new_list.append(r_vars[j][1])
                reduced_form.append(new_list)
                new_list = []
                i = length_l
            i = i + 1
        j = j + 1
    
    print(reduced_form)
    return (0)

# def discriminant_poly(eqn):
#     #some stuff

# def solve_poly(eqn):
#     #some stuff