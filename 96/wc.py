def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        content = f.read()
        lines_len = len(content.splitlines())
        words_len = len(content.split())
        chars_len = len(content)
        return f'{lines_len}\t{words_len}\t{chars_len} {file_}'
    # try:
    #     f = open(file_)
    #     lines = f.read()
    #     breaks_len = lines.count('\n')
    #     lines = lines.splitlines()
    #     lines_len = len(lines)
    #     words_len = 0
    #     chars_len = 0

    #     for line in lines:
    #         if line:
    #             words_len += len(line.split())
    #         chars_len += len(line)
    #     if lines_len > 1:
    #         chars_len += breaks_len
    #     return '\t{}\t{}\t{} {}'.format(lines_len, words_len, chars_len, file_)
    # except OSError as error:
    #     print('Could not open the file', error)

if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))

# wc 96/sample.txt
# python 96/wc.py 96/sample.txt
