import operator

CALCULATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
}


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    num1, sign, num2 = calculation.split(' ')

    try:
        return CALCULATIONS[sign](float(num1), float(num2))
    except (ValueError, KeyError, ZeroDivisionError) as ex:
        print(ex)
        raise ValueError
