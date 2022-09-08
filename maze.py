# maze module:
# - a maze is a rectangle; 
# - has entrance and exit are placed on opposite side of maze;
# - has a wall arround;
# - every cell has number(started at top left corner) and value equal it's content:
# 0 - outside space
# 1 - wall
# 2 - pass

''' return test constant maze as list '''
def getConstMaze():
    maze = [    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
                [2, 2, 1, 2, 2, 2, 1, 1, 2, 2],
                [1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 2, 2, 2, 2, 2, 2, 1, 1],
                [1, 2, 1, 1, 1, 1, 1, 2, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  ]

    return maze


''' print maze '''
def printMaze(maze):
   
    # define symbols for printing
    arround = "~"
    wall = "@"
    way = "."

    # for printing both types of maze with/without arround space 
    if (type(maze[0][0]) == int):
        for line in maze:
            for cell in line:
                if cell == 1:
                    print(wall, end='')
                if cell == 2:
                    print(way, end='')
            print("")
    else:
       for line in maze:
            for cell in line:
                if cell[1] == 0:
                    print(arround, end='')
                if cell[1] == 1:
                    print(wall, end='')
                if cell[1] == 2:
                    print(way, end='')
            print("") 


''' create list wint maze and arround space.
Each cell has unique number and value depends of content '''
def getArroundSpace(maze):
    # get maze's length and width
    space_len = len(maze[1]) + 2
    space_width = len(maze) + 2
    # start numerations from left top corner
    
    full_maze = []  # list for maze with arround
    cell_number = 0 # number of cell
    line = []       # buffer for one line of maze
  
    for l in range(space_width):
        for c in range(space_len):
            # for first and last line
            if ( (l == 0) or (l == (space_width - 1)) ):
                line.append([cell_number, 0])
            else:
                if ( (c == 0) or (c == (space_len - 1)) ):
                    line.append([cell_number, 0])
                else:
                    line.append([cell_number, maze[l-1][c-1]])   
            cell_number = cell_number + 1
        full_maze.append(line)
        line = []

    return full_maze        


