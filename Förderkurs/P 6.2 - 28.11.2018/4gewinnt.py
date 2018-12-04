col1 =  [1,1,1,1,1,1,1,1,1]
col2 =  [1,0,0,0,0,0,0,0,0]
col3 =  [1,0,0,0,0,0,0,0,0]
col4 =  [1,0,0,0,0,0,0,0,0]
col5 =  [1,0,0,0,0,0,0,0,0]
col6 =  [1,0,0,0,0,0,0,0,0]
col7 =  [1,0,0,0,0,0,0,0,0]
col8 =  [1,0,0,0,0,0,0,0,0]
col9 =  [1,0,0,0,0,0,0,0,0]
col10 = [1,0,0,0,0,0,0,0,0]

matrix = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10]

#selected_col = matrix[4]
#selected_col[0] = 1

# i = 0
# j = 0
for i in range(9):
     for j in range(10):
          print(matrix[j][i], end="")
     print("")


