# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# column=0
# row=0
# diagonalRight=0
# diagonalLeft=0
# i=0
# sum=0
# while(i<len(magic_square)):
#     j=0
#     while(j<len(magic_square)):
#         column=column+magic_square[i][j]
#         row=row+magic_square[j][i]
#         j=j+1
#     diagonalRight=diagonalRight+magic_square[i][i]
#     diagonalLeft=diagonalLeft+magic_square[i][len(magic_square)[i]][len(magic_square)-i]
#     i=i+1
# print(diagonalRight)









# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# column=0
# row=0
# diagonalRight=0
# diagonalLeft=0
# i=0
# while(i<len(magic_square)):
#     j=0
#     while(j<len(magic_square)):
#         column=column+magic_square[i][j]
#         row=row+magic_square[j][i]
#         j=j+1
#     diagonalRight=diagonalRight+magic_square[i][i]
#     diagonalLeft=diagonalLeft+magic_square[i][len(magic_square)-(i+1)]
#     i=i+1
# print("column is =",column,"row is=",row,"diagonalleft is=",diagonalLeft,"dialonalright is=",diagonalRight)





