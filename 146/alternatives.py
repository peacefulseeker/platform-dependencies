STAR = '*'


def _print_row(i, width):
    return f'{STAR*i: ^{width}}'

# ORIGINAL
def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    # upper half
    for i in range(1, width+1, 2):
        yield _print_row(i, width)
    # lower half ('width-2' to not repeat middle row)
    for i in range(width-2, 0, -2):
        yield _print_row(i, width)




from itertools import chain

STAR = '*'
# CLEVER
def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    star_range = chain(range(1, width, 2), range(width, 0, -2))
    yield from (f"{STAR * i:^{width}}" for i in star_range)



STAR = '*'

# MOST ELEGANT
def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    for index in range(width):
        stars = width - abs((index - width // 2) * 2)
        yield (STAR * stars).center(width)
