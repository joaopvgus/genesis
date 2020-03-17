from random import randint

class Player:
    
    __id = 1
    
    def __init__(self):
        self.__id = Player.__id
        self.__hand = []
        self.__points = 0
    
    def get_id(self):
        return self.__id
    
    def get_hand(self):
        return self.__hand
    
    def set_hand(self, hand):
        self.__hand = hand
    
    def get_points(self):
        return self.__points
    
    def set_points(self, points):
        self.__points = points
        
    def increment_points(self):
        self.__points += 1
    
    def add_piece(self, piece):
        self.__hand.append(piece)

class Game:
    
    def __init__(self):
        self.__player1 = Player()
        self.__player2 = Player()
        self.__table = []
        self.__pieces = [[0,0]]
        
    def get_player1(self):
        return self.__player1
    
    def get_player2(self):
        return self.__player2
    
    def get_pieces(self):
        return self.__pieces
        
    def generate_pieces(self):
        for a in range(7):
            for b in range(7):
                verifier = True
                for piece in self.__pieces:
                    if [a,b] == piece or [b,a] == piece:
                        verifier = False
                if verifier == True:
                    temp = []
                    temp.append(a)
                    temp.append(b)
                    self.__pieces.append(temp)
                    
    def sort_pieces(self):
        for i in range(7):
            piece_coord = randint(0, len(self.__pieces) - 1)
            self.__player1.add_piece(self.__pieces[piece_coord])
            self.__pieces.pop(piece_coord)
            piece_coord = randint(0, len(self.__pieces) - 1)
            self.__player2.add_piece(self.__pieces[piece_coord])
            self.__pieces.pop(piece_coord)
    
game = Game()
game.generate_pieces()
game.sort_pieces()
print('hand 1: ', game.get_player1().get_hand())
print('hand 2: ', game.get_player2().get_hand())
print('resting pieces: ', game.get_pieces())