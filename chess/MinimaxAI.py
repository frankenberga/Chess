import chess

class MinimaxAI():
    def __init__(self, depth):
        self.depth = depth

    #depth limited search
    def depth_limited_minimax(self, board, max_depth):
        num_calls = 0
        curr_depth = 0
        next_move = None
        infinity = float('inf')
        best_score = -infinity
        for move in list(board.legal_moves):
            board.push(move) #do the move
            score = self.min_value(board, curr_depth + 1, max_depth)
            num_calls += 1
            if (score > best_score): #if the value of that  move equals the max_value
                next_move = move   #set next_move to be that move
                best_score = score   #set best_score to be that higher score
            board.pop() #pop the move off, return to original state
        print("Minimax AI recommending move ", str(next_move))
        print ("Number of calls to minimax", num_calls)
        print ("best score", best_score)
        return next_move #return that next move

    #with iterative deepening
    def choose_move(self, board):
        best_move = None
        max_depth = 1
        while max_depth <= self.depth:
            best_move = self.depth_limited_minimax(board, max_depth) 
            max_depth += 1
        return best_move #return that next move

    #this method recursively gets the minimax value (with min_value method)
    def max_value(self, board, curr_depth, max_depth):
        if self.cutoff_test(board, curr_depth, max_depth):
            return self.utility(board)
        max_val = -float('inf')
        for move in list(board.legal_moves):
            #the recursive minimax step where we alternate calling the max_value method and min_value method
            board.push(move)
            next_depth = curr_depth + 1
            max_val = max(max_val, self.min_value(board, next_depth, max_depth))
            board.pop()
        return max_val

    #this method recursively gets the minimax value (with max_value method)
    def min_value(self, board, curr_depth, max_depth):
        if self.cutoff_test(board, curr_depth, max_depth):
            return self.utility(board)
        min_val = float('inf')
        for move in list(board.legal_moves):
            #the recursive minimax step where we alternate calling the max_value method and min_value method
            board.push(move)
            next_depth = curr_depth + 1
            min_val = min(min_val, self.max_value(board, next_depth, max_depth))
            board.pop()
        return min_val

    #this method is the cutoff test for when to stop recursing
    def cutoff_test(self, board, curr_depth, max_depth):
        if (board.is_game_over()): #if the board is in one of the terminal cases return true
            return True
        elif (max_depth == curr_depth): #otherwise if the depth is at max depth return true
            return True
    
    #this function gets the utility of the board
    def utility(self, board):
        value = 0
        if (board.is_game_over()):
            if (board.is_checkmate()):
                if (board.turn == True):
                    value = 1000
                elif (board.turn == False):
                    value = -1000
        else:
            value = self.evaluation(board)
        return value
    
    #material heuristic function
    def evaluation(self, board):
        state_string = board.fen()
        state_list = state_string.split("/")
        white_val = 0
        black_val = 0

        for element in state_list:
            element = list(element)
            if ' ' in element:
                element = element[:8]
            for x in element:   #adding up all of the white pawns values
                if (x == 'P'):
                    white_val += 1  
                elif (x == 'N' or x == 'B'): #adding up all of the white pieces values
                    white_val += 3
                elif (x == 'R'):
                    white_val += 5
                elif (x == 'Q'):
                    white_val += 9 
                elif (x == 'p'): #adding up all of the black pawns values
                    black_val += 1
                elif (x == 'n' or x == 'b'): #adding up all of the black pieces values
                    black_val += 3
                elif (x == 'r'):
                    black_val += 5
                elif (x == 'q'):
                    black_val += 9 
        return (white_val - black_val) #returning the material heuristic value
      