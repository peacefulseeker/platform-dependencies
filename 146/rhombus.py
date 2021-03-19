STAR = '*'

def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          * width - 4, row 1
         ***, with - 2, row 2
        *****, width
         ***, width - 2, row 4
          *, width - 4, row 5
    """
    def _print_row(stars_count):
        return f"{STAR * stars_count : ^{width}}"

    stars_count = 1
    for row in range(1, width + 1):
        # the most middle:
        if (width // 2 + 1) == row:
            yield(_print_row(stars_count))
            stars_count -= 2
        elif row > width / 2:
            yield(_print_row(stars_count))
            stars_count -= 2
        else:
            yield(_print_row(stars_count))
            stars_count += 2

gen = gen_rhombus(5)
for row in gen:
    print(row)
