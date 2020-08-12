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