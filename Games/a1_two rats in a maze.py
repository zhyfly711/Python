# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat(object):
    """ A rat caught in a maze. """

    def __init__(self, ratName, row, column): #initiate the rat
        self.ratName = ratName
        self.row = row
        self.colunm = column
        self.num_sprouts_eaten = 0
        
    def set_location(self, row, column):
        self.row = row
        self.column = column
    
    def eat_sprout(self):
        self.num_sprouts_eaten += 1
    
    def __str__(self):
        return self.ratName + ' at ' + '(' + self.row + ', ' + self.column + ')' + ' ate '  + self.num_sprouts_eaten + ' sprouts.'

          
        
class Maze(object):
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        sprouts = 0
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if j == '@':
                    sprouts += 1
        
        self.num_sprouts_left = sprouts
        
    def is_wall(self, row, column):
        return self.maze[row][column] == '#'
        
    def get_character(self, row, column):
        if row == self.rat_1.row and column == self.rat_1.column:
            return self.rat_1
        elif row == self.rat_2.row and column == self.rat_2.column:
            return self.rat_2
        else:
            return self.maze[row][column]
    
    def move(self, rat, verticalMove, horizontalMove):
        new_row = rat.row + verticalMove
        new_column = rat.column + horizontalMove
        
        if self.is_wall(new_row, new_column):
            return False
        elif self.get_charactor(new_row, new_column) == SPROUT:
            rat.eat_sprout()
            self.maze[new_row][new_column] = HALL
            self.num_sprouts_left -= 1
        
        rat.row += verticalMove
        rat.column += horizontalMove
        return True
    
            
    def __str__(self):
        result = ""
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if (self.rat_1.row, self.rat_1.col) == (i, j):
                    result += self.rat_1.symbol
                elif (self.rat_2.row, self.rat_2.col) == (i, j):
                    result += self.rat_2.symbol
                else:
                    result += self.maze[i][j]
            result += "\n"

        result += self.rat_1.__str__() + "\n"
        result += self.rat_2.__str__()

        return result
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        