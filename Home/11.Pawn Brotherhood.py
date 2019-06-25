def safe_pawns(pawns: set) -> int:
    columns = ' abcdefgh '
    rows = ' 12345678 '
    safe = 0    
    for paw in pawns:
        check = 0
        col_num = columns.find(paw[0])
        row_num = rows.find(paw[1])
        for i in pawns:            
                if ((i[0] == columns[col_num-1] or i[0] == columns[col_num+1])
                        and i[1] == rows[row_num-1]):
                    check+=1                    
        if check>=1:
            safe+=1
    return safe

if __name__ == '__main__':
    print(safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
