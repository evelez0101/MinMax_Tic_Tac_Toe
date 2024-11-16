class board:
    def __init__(self):
        # initalize matrix
        self.matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def __str__(self):
        string = "\n----+---+----\n"
        
        for row in self.matrix:
            string += "| "
            for col in row:
                string += col
                string += " | "
            
            string += "\n----+---+----\n"

        return string

    def check_win(self, player):
        
        # Check rows and cols
        for idx in range(len(self.matrix)):
            # check row 
            if (self.matrix[idx][0] == player and 
                self.matrix[idx][1] == player and 
                self.matrix[idx][2] == player):
                    return True

            # check col
            if (self.matrix[0][idx] == player and 
                self.matrix[1][idx] == player and 
                self.matrix[2][idx] == player):
                    return True

        # Check Diagonal 1
        if (self.matrix[0][0] == player and 
            self.matrix[1][1] == player and 
            self.matrix[2][2] == player):
                return True
        
        # Check Diagonal 2
        if (self.matrix[2][0] == player and 
            self.matrix[1][1] == player and 
            self.matrix[0][2] == player):
                return True

        return False

    def validate_move(self, location, player_piece):
        row,col = location

        # Check for valid row
        if row >= len(self.matrix) or row < 0:
            return False

        # check for valid col
        if col >= len(self.matrix[0]) or col < 0:
            return False
        
        # if space isn't empty
        if self.matrix[row][col] != " ":
            return False
        
        return True

    def place_piece(self, location, player_piece):
        row,col = location
        self.matrix[row][col] = player_piece
    
    def getAvailableSpots(self):
        li_available_spots = []

        # Traverse the grid
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                # Add open spots to a grid as a tuple
                if self.matrix[row][col] == " ":
                    li_available_spots.append( (row,col) )

        return li_available_spots