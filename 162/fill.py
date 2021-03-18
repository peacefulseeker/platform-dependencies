HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    val_length = len(str(value))
    fill_char_length = column_length - val_length
    return f'{fill_char * fill_char_length}{value}'
