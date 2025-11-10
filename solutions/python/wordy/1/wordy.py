OPERATIONS = {"plus": "+",
              "minus": "-",
              "multiplied by": "*",
              "divided by": "/"}

QUESTION_MARKS = ["What ", "is ", "?"]

def answer(question: str) -> int:
    """ Answer to a mathematical question.
 
    :param question: str - the mathematical question to answer.
    :return: str - the answer.
    :raise ValueError: when an unknow operation is asked or
                       when there's a syntax error.
    """
    for question_mark in QUESTION_MARKS:
        question = question.replace(question_mark, "")

    for key, value in OPERATIONS.items():
        question = question.replace(key, value)

    question = question.split(" ")
    question.insert(0, "(")
    question.insert(4, ")")

    q = [x.isalpha() for x in question if x not in ("What", "is")]
    if any(q):
        raise ValueError("unknown operation")

    try:
        return eval(" ".join(question))
    except:
        raise ValueError("syntax error")
