def get_ordinal_suffix(number:int) -> str:
    """Receives a number int and returns it appended with its ordinal suffix,
       so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.

       Rules:
       https://en.wikipedia.org/wiki/Ordinal_indicator#English
       - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
       - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
       - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
       - As an exception to the above rules, all the "teen" numbers ending with
         11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
         pronounced one hundred [and] twelfth)
       - th is used for all other numbers (e.g. 9th, pronounced ninth).
       """
    str_num = str(number)

    if any(str_num.endswith(teen_num) for teen_num in ['11', '12', '13']):
        return str_num + 'th'
    elif str_num.endswith('1'):
        return str_num + 'st'
    elif str_num.endswith('2'):
        return str_num + 'nd'
    elif str_num.endswith('3'):
        return str_num + 'rd'

    return str_num + 'th'


print(get_ordinal_suffix(9))

