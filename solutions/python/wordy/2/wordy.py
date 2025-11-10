from operator import add, mul, sub
from operator import floordiv as div

OPERATIONS = {"plus": add, "minus": sub, "multiplied": mul, "divided": div}

def answer(question: str) -> int:
    """ Answer to a mathematical question.
 
    :param question: str - the mathematical question to answer.
    :return: str - the answer.
    :raise ValueError: when an unknow operation is asked or
                       when there's a syntax error.
    """
    return calculate(clean(question))

def clean(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")

    return (question.removeprefix("What is")
            .removesuffix("?")
            .replace("by", "")
            .strip()).split()
    
def calculate(equation):
    if len(equation) == 1:
        return int(equation[0])
    else:
        try:
            x_value, operation, y_value, *rest = equation
            equation = [OPERATIONS[operation](int(x_value), 
                        int(y_value)), *rest]
        except:
            raise ValueError("syntax error")
            
        return calculate(equation)
