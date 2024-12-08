def find_xmas(row: int, col: int, mat: list[str]) -> int:
    ans = 0
    
    def in_bound(row: int, col: int) -> bool:
        return 0 <= row < rows_len and 0 <= col < cols_len

    list_xmas = list('xmas'.upper())
    
        
    # horizontal:
    if in_bound(row, col) and in_bound(row, col+4):
        if mat[row][col:col+4] == list_xmas:
            # print(row, col)
            ans += 1

    # reverse horizontal:
    if in_bound(row, col) and in_bound(row, col-3) and in_bound(row, col+1):
        # print(mat[row][col-3:col+1][::-1])
        if mat[row][col-3:col+1][::-1] == list_xmas:
            # print(mat[row])
            # print(row, col)
            ans += 1

    # vertical:
    if in_bound(row, col) and in_bound(row+4, col):
        # print(list(zip(*mat[row:row+4]))[col] == tuple('XMAS'))
        
        if (list(zip(*mat[row:row+4]))[col] == tuple('XMAS')):
            # print(mat[row:row+4])
            # print(row, col)
            ans += 1

    # reverse vertical:
    if in_bound(row, col) and in_bound(row-3, col) and in_bound(row+1, col):
        print(list(zip(*mat[row-3:row+1]))[col] == tuple('XMAS'))
        print(list(zip(*mat[row-3:row+1][::-1]))[col])
        
        if (list(zip(*mat[row:row+4]))[col] == tuple('XMAS')):
            # print(mat[row:row+4])
            # print(row, col)
            ans += 1
    return ans
    

    




with open('./in-my.txt', 'r') as f:
    rows_of_letters = [list(i) for i in f.readlines()]
    rows_len = len(rows_of_letters)
    cols_len = len(rows_of_letters[0])
    
    count = 0

    for i, row in enumerate(rows_of_letters):
        for j, letter in enumerate(row):
            if letter == 'X':
                # print(i, j)
                count += find_xmas(i, j, rows_of_letters)

    print(count)
            
