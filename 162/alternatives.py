def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    res = f"{value:>{column_length}}".replace(" ", fill_char)
    return res


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    return str(value).rjust(column_length).replace(' ', fill_char)
