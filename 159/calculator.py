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
    num1, operator, num2 = calculation.split(' ')

    num1 = float(num1)
    num2 = float(num2)

    if (num2 == 0 and operator == '/') or operator not in ['+', '-', '/', '*']:
        raise ValueError

    return eval(f'{num1} {operator} {num2}')



print(simple_calculator('-5 * -11'))
