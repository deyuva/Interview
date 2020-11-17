# Mat is a 2d array size of N * M containing 'X' or '.' and at each point.
# the array contains rows and collumns of X's which are callsed submarines.
# a sub marine can be a 1 * n sub row or a N * 1 sub collums.
# we no that there is no intercection between any submarine and there is a space of at least 1 '.' at each point.

# find the number of subs in a given matrix.


# SOLUTION 1 algorithem - 

# 1 - initilize a 2D bool matrix size of N * M - grid

# 2 - initilize constants ROW and COL to represents their lenghts

# 3 - iterate over the all the rows

      for each row iterate all its colums
        
          if found a '.'
            continue
          
          if found a 'x'
            count += 1
            
              if next cell to the right is an X 
                go right until reached the end or a '.'
              
              else next cell to the right is a '.' or boundry reached
                go down until reached the end or an '.'
                mark those squres as visited at the grid.
                
# SOLUTION 1 algorithem - 

def find_subs(mat, rows, cols):
    
    grid = {}
    count = 1
    i = 0
    j = 0
    k = 0
    
    for i in range(rows):
        for j in range(cols):
            k = i + 1
            
            if mat[i][j] == '.' or grid[i][j] == 1:
                continue
            
            elif mat[i][j] == 'x'
            
                count += 1
                
                while(j + 1) < cols and mat[i][j + 1] =='x'       # try going right, if found 'xx' raise flag
                    flag = 1
                    j += 1
                    
                if flag == 0:                                     # if flag is not raised found only 'x' should try do down
                    while (k + i) < rows and mat[i + k][j] == 'x'
                        grid[((i + k), j)] == 1
                    k += 1
                
             
            


