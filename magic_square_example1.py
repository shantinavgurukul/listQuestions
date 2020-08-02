magicSquare=[
    [3 -4 1],
    [-2 0 2],
    [-1 4-3]
]
col=0
row=0
diagonalR=0
diagonalL=0
i=0
while(i<len(magicSquare)):
    j=0
    while(j<len(magicSquare)):
        col=col+magicSquare[i][j]
        row=row+magicSquare[j][i]
        j=j+1
    diagonalR=diagonalR+magicSquare[i][i]
    diagonalL=diagonalL+magicSquare[i][len(magicSquare)-1]
    i=i+1
print(col,row,diagonalL,diagonalR)