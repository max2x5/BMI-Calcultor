def match_age(age, bmi):
    if age < 25:
        result = under25(bmi)
    elif age < 35:
        result = under35(bmi)
    elif age < 45:
        result = under45(bmi)
    elif age < 55:
        result = under55(bmi)
    else:
        result = six5upper(bmi)

    return result


def under25(bmi):
    if bmi < 20:
        return("Underweight")

    elif bmi <= 25:
        return("Normal weight")

    elif bmi <= 30:
        return("Overweight")

    elif bmi <= 40:
        return("Adiposity")

    else:
        return("Severe adiposity")


def under35(bmi):
    if bmi < 21:
        return("Underweight")

    elif bmi <= 26:
        return("Normal weight")

    elif bmi <= 31:
        return("Overweight")

    elif bmi <= 41:
        return("Adiposity")

    else:
        return("Severe adiposity")


def under45(bmi):
    if bmi < 22:
        return("Underweight")

    elif bmi <= 27:
        return("Normal weight")

    elif bmi <= 32:
        return("Overweight")

    elif bmi <= 42:
        return("Adiposity")

    else:
        return("Severe adiposity")


def under55(bmi):
    if bmi < 23:
        return("Underweight")

    elif bmi <= 28:
        return("Normal weight")

    elif bmi <= 33:
        return("Overweight")

    elif bmi <= 43:
        return("Adiposity")

    else:
        return("Severe adiposity")


def under65(bmi):

    if bmi < 24:
        return("Underweight")

    elif bmi <= 29:
        return("Normal weight")

    elif bmi <= 34:
        return("Overweight")

    elif bmi <= 44:
        return("Adiposity")

    else:
        return("Severe adiposity")

def six5upper(bmi):

    if bmi < 25:
        return("Underweight")

    elif bmi <= 30:
        return("Normal weight")

    elif bmi <= 35:
        return("Overweight")

    elif bmi <= 45:
        return("Adiposity")

    else:
        return("Severe adiposity")