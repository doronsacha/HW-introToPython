from sys import stdin


def read_inp():
    matrix = []
    search_word = ''
    for line in stdin:
        line = line.strip()
        if ' ' not in line:
            search_word = line
            break

        matrix.append(line.split(' '))

    assert len(matrix) >= 2, 'matrix must be at least 2X2'

    first_row_len = len(matrix[0])
    assert all(len(row) == first_row_len for row in matrix), 'matrix must be square'

    assert search_word, "must provide a search word with no spaces"

    return matrix, search_word


if __name__ == '__main__':
    mat, w = read_inp()

    print('search in matrix:')
    for row in mat:
        for c in row:
            print(c, end=' ')
        print()
    print()

    print('search for word')
    print(w)
