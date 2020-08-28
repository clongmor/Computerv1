def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_negative(string):
    if string[0] == "-" and is_number(string[1:]):
        return True
    else:
        return False

def to_negative(string):
    if string.isdigit():
        return (int(string) * -1)
    elif is_number(string):
        return (float(string) * -1)
    else:
        print("error not a number")
        exit(0)

def to_number(string):
    if string.isdigit():
        int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            exit(0)

def quadratic_formula(a, b, c):
    print(a, b, c)
    if a == 0 and b == 0 and c == 0:
        answer1 = "X ∈ R"
        answer2 = answer1
    elif a == 0 and b == 0:
        answer1 = "no possible solution"
        answer2 = answer1
    elif a == 0:
        answer1 = str((c * -1)/b)
        answer2 = answer1
    else:
        answer1 = str((-b + (b*b - 4*a*c)**0.5)/(2*a))
        answer2 = str((-b - (b*b - 4*a*c)**0.5)/(2*a))

    print(answer1, answer2)
    answers = [answer1, answer2]
    return (answers)

def error_checks(string):
    if string == "":
        print("invalid input, try again.")
    if "=" not in string:
        print ("cannot calculate solution if not equal to sign.")
    
    
    