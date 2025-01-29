class Player:
    def __init__(self, type, board):
        self.type = type
        self.board = board

    def make_move(self,index):
        self.board.put(self.type,index)
        self.board.change_board()
        return self.board.check_win(self.type)
    
    def AI_move(self):
        self.board.change_board()
        return self.board.check_win(self.type)


