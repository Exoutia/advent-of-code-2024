with open("./in.txt", "r") as f:
    rows = f.read().splitlines()

    row_len = len(rows)
    col_len = len(rows[0])

    def count(row, col):
        if rows[row][col] != "A":
            return 0
        
        ul = rows[row-1][col-1]
        ur = rows[row-1][col+1]
        dl = rows[row+1][col-1]
        dr = rows[row+1][col+1]
        return sorted([ul, ur, dl, dr]) == ['M', 'M', 'S', 'S'] and ul != dr

    print(sum(count(r, c) for r in range(1, row_len-1) for c in range(1, col_len-1)))
