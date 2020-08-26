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
    print (a, b, c)
    answer1 = (-b + (b*b - 4*a*c)**0.5)/(2*a)
    answer2 = (-b - (b*b - 4*a*c)**0.5)/(2*a)

    print(answer1, answer2)
    answer1 = str(answer1)
    answer2 = str(answer2)

    print(answer1, answer2)
    answers = [answer1, answer2]
    return (answers)