def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    brackets = "()[]{}<>"

    opposite_brackets = {
        "(" : ")",
        "[" : "]",
        "{": "}",
        "<" : ">",
    }

    balance_check = []

    for char in phrase:
        if char in brackets:
            if not balance_check:

                if char in ")]}>":
                    return False
            
            if char in "([{<":
                balance_check.append(char)
            
            if char in ")]}>":
                last_bracket = balance_check.pop()
                if char != opposite_brackets[last_bracket]:
                    return False
    
    return len(balance_check) == 0
