def nQueen(n):
    
    def is_safe(r,c):
        for i in range(len(queen_positions)-1):
            if r == queen_positions[i][0] or abs(r-queen_positions[i][0]) == abs(c-queen_positions[i][1]):
                return False
        return True
    
    def place_queen(col):
        if col == n :
            return True
        row = 0
        while(row<n):
            queen_positions.append([row,col])
            if is_safe(row,col) and place_queen(col+1):
                return True
            queen_positions.pop()
            row = row + 1
        return False
    
    
    
    queen_positions = list()
    if place_queen(0):
        return queen_positions
    else:
        return False
    
    
    
    
    
    
print(nQueen(8))
