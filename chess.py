# assignment: programming assignment 5
# author: Krishna Dua
# date: 12/07/2023
# file: chess.py is a program that helps people learn how chess pieces move
# input: Information about chess piece and position
# output: Board drawn that moves the chess piece and shows its possible movements.

class Board:
    def __init__(self):
        self.board = {}
        self.empty()

    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col + row] = ' '

    def set(self, pos, label):
        if pos in self.board.keys():
            self.board[pos] = label

    def get_keys(self):
        return self.board.keys()

    def draw(self):
        print('   a   b   c   d   e   f   g   h')
        print(' +---+---+---+---+---+---+---+---+')
        for row in '87654321':
            column_row = row + '|'
            for col in 'abcdefgh':
                column_row += ' ' + self.board[col + row] + ' |'
            print(column_row + row)
            print(' +---+---+---+---+---+---+---+---+')
        print('   a   b   c   d   e   f   g   h')

    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col + row] = ' '

class Chess_Piece:
    def __init__(self, board, pos, color='white'):
        self.pos = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
    def get_index(self, pos):
        return 'abcdefgh'.index(pos[0]), '12345678'.index(pos[1])
    def get_rank(self, index):
        if 0 <= index < 8:
            return '12345678'[index]
    def get_file(self, index):
        if 0 <= index < 8:
            return 'abcdefgh'[index]
    def get_name(self):
        pass
    def moves(self, board):
        pass
class Rook(Chess_Piece):
    def get_name(self):
        return 'R'

    def moves(self, board):
        for key in board.get_keys():
            row, col = self.get_index(key)
            if row == self.pos[0] and col == self.pos[1]:
                continue
            elif row == self.pos[0]:
                board.set(key, 'x')
            elif col == self.pos[1]:
                board.set(key, 'x')

class Bishop(Chess_Piece):
    def get_name(self):
        return 'B'

    def moves(self, board):
        for key in board.get_keys():
            row, col = self.get_index(key)
            if row == self.pos[0] and col == self.pos[1]:
                continue
            elif abs(row - self.pos[0]) == abs(col - self.pos[1]):
                board.set(key, 'x')

class Queen(Chess_Piece):
    def get_name(self):
        return 'Q'

    def moves(self, board):
        for key in board.get_keys():
            row, col = self.get_index(key)
            if row == self.pos[0] and col == self.pos[1]:
                continue
            elif row == self.pos[0] or col == self.pos[1] or abs(row - self.pos[0]) == abs(col - self.pos[1]):
                board.set(key, 'x')

class King(Chess_Piece):
    def get_name(self):
        return 'K'

    def moves(self, board):
        for key in board.get_keys():
            row, col = self.get_index(key)
            if abs(row - self.pos[0]) <= 1 and abs(col - self.pos[1]) <= 1 and (row, col) != self.pos:
                board.set(key, 'x')

class Knight(Chess_Piece):
    def get_name(self):
        return 'N'

    def moves(self, board):
        for key in board.get_keys():
            row, col = self.get_index(key)
            if (abs(row - self.pos[0]) == 2 and abs(col - self.pos[1]) == 1) or (abs(row - self.pos[0]) == 1 and abs(col - self.pos[1]) == 2):
                board.set(key, 'x')

if __name__ == '__main__':
    print('Welcome to the Chess Game!')
    board = Board()
    board.draw()
    while True:
        answer = input('Enter a chess piece and its position or type X to exit:\n')
        if answer.upper() == 'X':
            print('Goodbye!')
            break
        if len(answer) != 3:
            continue
        elif answer[0].upper() in 'KQNBR' and answer[1] in 'abcdefgh' and answer[2] in '12345678':
            piece_type = answer[0].upper()
            piece_pos = answer[1:]
            piece = None
            if piece_type == 'R':
                piece = Rook(board, piece_pos)
            elif piece_type == 'B':
                piece = Bishop(board, piece_pos)
            elif piece_type == 'Q':
                piece = Queen(board, piece_pos)
            elif piece_type == 'K':
                piece = King(board, piece_pos)
            elif piece_type == 'N':
                piece = Knight(board, piece_pos)
            piece.moves(board)
        else:
            continue

        board.draw()
        board.empty()
