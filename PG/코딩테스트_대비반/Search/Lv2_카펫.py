def solution(brown, red):
    carpet = brown + red

    for factorize_num in range(3, int(carpet/2)):
        if carpet % factorize_num == 0:
            row = carpet // factorize_num
            col = carpet // row
            if 2 * (row + (col - 2)) == brown:
                return [row, col]
