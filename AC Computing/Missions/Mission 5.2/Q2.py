manchester_grid = [['M', 'A', 'N', 'C', 'H'], ['E', 'S', 'T', 'R', 'B'], ['D', 'F', 'G', 'I', 'K'], ['L', 'O', 'P', 'Q', 'U'], ['V', 'W', 'X', 'Y', 'Z']]
juventus_grid = [['I', 'U', 'V', 'E', 'N'], ['T', 'S', 'A', 'B', 'C'], ['D', 'F', 'G', 'H', 'K'], ['L', 'M', 'O', 'P', 'Q'], ['R', 'W', 'X', 'Y', 'Z']]

def coord(char, grid):
    #Looks through all lines in the grid
    for n in range(5):
        line = grid [n]
        #Looks throgh each charecter in the line
        for k in range(5):
            if char == line[k]:
                return [n,k]
            
def extract(coord, grid):
    return grid[ coord[0] ][ coord[1] ]