from constants import * 

def read_maze(file):
    with open(file) as f:
        maze = []
        line = f.readline()
        #y = 0
        while line:
            array_line = []
            # x = 0
            for c in line:
                array_line.append(c)
                # x += 1
                #TODO: check limit maze with x
            maze.append(array_line)
            line = f.readline()
            #y +=1
            #TODO: check limit maze with y
        return maze

#  ## # #X#   #S#

["#"]

x = 1

["#", " "]

x = 2

["#", " ", " "]

x = 

array_line = ["#", " ", " ", ..., "#", "S", "#"]

maze = [["#", " ", " ", ..., "#", "S", "#"]]

y = 1 

x = 0

[]

...

x = N


0123
6789

7892

maze = read_maze('./assets/level.txt')
"""
print(maze)
print(maze[1][1])
print(maze[1][0])
print(maze[2][3])
"""
for i in maze:
  for j in i:
    print(j, end='')
  print()

  



