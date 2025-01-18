from typing import List

def create_square(key: str) -> List[List[str]]:
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

def find_char(char: str, square: List[List[str]]) -> tuple[int, int]:
    for i in range(5):
        for j in range(5):
            if square[i][j] == char:
                return (i,j)
            
def decrypt(ciphertext: str, square: List[List[str]]) -> str:
    bigraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    result = []
    
    for b in bigraphs:
        r1, c1 = find_char(b[0], square)
        r2, c2 = find_char(b[1], square)

        if r1 == r2:
            result.append(square[r1][(c1 - 1) % 5])
            result.append(square[r2][(c2 - 1) % 5])

        elif c1 == c2:
            result.append(square[(r1 - 1) % 5][c1])
            result.append(square[(r2 - 1) % 5][c2])

        else:
            result.append(square[r1][c2])
            result.append(square[r2][c1])

    result = [c for c in result if c != 'X']
    return "".join(result)

if __name__ == "__main__":
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    square = create_square(key)
    print(decrypt(ciphertext, square))
