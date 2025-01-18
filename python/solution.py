def create_square(key: str):
    square = [['']*5 for i in range(5)]

    i, j = 0, 0
    inserted = set()
    #                       J = I
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c in inserted:
            continue
        square[i][j] = c
        inserted.add(c)
        j += 1
        if j % 5 == 0:
            j = 0
            i += 1

    return square

if __name__ == "__main__":

    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    print(create_square(key))