import random
import math
import GameBoard

class MinMax:

    def __init__(self, player, opponent):
        # Keeps Track of Player and Opponent Symbols
        self.player = player
        self.opponent = opponent

    # Mix Max Algorithm with alpha beta pruning
    def getMove(self, board):
        move = self.Maximize(board, float('-inf'), float('inf'))
        return move[0]
    
    # Checks for a winner or a tie
    def isWinnerOrTie(self, board):
        return len(board.getAvailableSpots()) == 0 or board.checkWin(self.player) or board.checkWin(self.opponent)

    # Heuristic Function    
    def evaluate(self, board):
        # Player Win
        if board.checkWin(self.player):
            return 10

        # Computer Win
        if board.checkWin(self.opponent):
            return -10

        # Tie or No Winner
        return 0
    
    # Simulates Computer Placing a piece
    def Minimize(self, board, alpha, beta):

        # If we reach a terminal node
        if self.isWinnerOrTie(board):
            return (None, self.evaluate(board))

        # By default set the min child to none and the eval to + infinity
        minChild, minUtility = None, float('inf')
        
        # Clone the board and simulate a move
        for spot in board.getAvailableSpots():
            clone = board.clone()

            # Try placing opponent piece here
            clone.placePiece(spot, self.opponent)

            # Take only the utility
            utility = self.Maximize(clone, alpha, beta)[1]
            
            # Find smallest algo
            if utility < minUtility:
                minMove, minUtility = spot, utility

            # Alpha Pruning
            if minUtility <= alpha:
                break

            # Update Beta
            if minUtility < beta:
                beta = minUtility

        return (minMove, minUtility)

    # Simulates Player Move
    def Maximize(self, board, alpha, beta):
        # A terminal node when we run of moves
        if self.isWinnerOrTie(board):
            return (None, self.evaluate(board))

        # By default set the max Move to none and the eval to - infinity
        maxMove, maxUtility = None, float('-inf')
        
        # Clone the board and simulate a move
        for spot in board.getAvailableSpots():
            
            clone = board.clone()

            # Simulate making this move
            clone.placePiece(spot, self.player)

            # Take only the utility
            utility = self.Minimize(clone, alpha, beta)[1]
            
            # Find smallest algo
            if utility > maxUtility:
                maxMove, maxUtility = spot, utility

            # Beta pruning 
            if maxUtility >= beta:
                break

            # Update Alpha
            if maxUtility > alpha:
                alpha = maxUtility

        return (maxMove, maxUtility)


