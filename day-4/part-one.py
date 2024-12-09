with open("./in.txt", "r") as f:
    rows = f.read().splitlines()

    row_len = len(rows)
    col_len = len(rows[0])

    def count(row, col):
        if rows[row][col] != "X":
            return 0
        return sum(
            [
                col > 2 and rows[row][col - 3 : col + 1] == "SAMX",  # left
                col < row_len - 3 and rows[row][col : col + 4] == "XMAS",  # right
                row > 2 and "".join(rows[row - i][col] for i in range(4)) == "XMAS",  # up
                row < col_len - 3 and "".join(rows[row + i][col] for i in range(4)) == "XMAS",  # down
                row > 2 and col > 2 and "".join(rows[row - i][col - i] for i in range(4)) == "XMAS",  # left-up
                row > 2 and col < row_len - 3 and "".join(rows[row - i][col + i] for i in range(4)) == "XMAS",  # right-up
                row < col_len - 3 and col > 2 and "".join(rows[row + i][col - i] for i in range(4)) == "XMAS",  # left-down
                row < col_len - 3 and col < row_len - 3 and "".join(rows[row + i][col + i] for i in range(4)) == "XMAS",  # right-down
            ]
        )

    print(sum(count(r, c) for r in range(row_len) for c in range(col_len)))
