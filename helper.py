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

def quadratic_formula(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    answer1 = (-b + (b*b - 4*a*c)**0.5)/(2*a)
    answer2 = (-b - (b*b - 4*a*c)**0.5)/(2*a)
    try:
        answer1 = int(answer1)
        answer1 = str(answer1)
    except:
        answer1 = str(answer1)
    
    try:
        answer2 = int(answer2)
        answer2 = str(answer2)
    except:
        answer2 = str(answer2)
    
    answers = [answer1, answer2]
    return (answers)