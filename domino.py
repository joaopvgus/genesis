import os
from random import randint

class Player:
    
    __id = 1
    
    def __init__(self):
        self.__id = Player.__id
        self.__hand = []
        self.__points = 0
        Player.__id += 1
    
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
        
    def remove_piece(self, position):
        self.__hand.pop(position)
    
    @property
    def printed_hand(self):
        text = 'Your hand: ' + (' '.join(str(piece) for piece in self.__hand) + '\n              ')
        text += '      '.join(str(num + 1) for num in range(len(self.__hand)))
        return text

class Game:
    
    def __init__(self):
        self.__player1 = Player()
        self.__player2 = Player()
        self.__player = [self.__player1, self.__player2]
        self.__table = []
        self.__pieces = []
        self.generate_pieces()
        self.sort_pieces()
        
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
    
    def round1(self):
        ver = input('player 1, type any button to continue...')
        print('table: ', end='')
        print(*self.__table)
        print(self.__player1.printed_hand)
        play = input('Choose your piece, Player 1:\n')
        try:
            if int(play) <= len(self.__player1.get_hand()) and int(play)-1 >= 0:
            # if play != '' and play in '123456789' and int(play) <= len(self.__player1.get_hand()):
                self.__table.append(self.__player1.get_hand()[int(play) - 1])
                self.__player1.remove_piece(int(play) - 1)
            else:
                print('invalid option, try again\n')
                self.round1()
        except:
            print('invalid option, try again\n')
            self.round1()
    
    def round(self, player):
        # os.system('clear')
        ver = input('player {}, type any button to continue...'.format(player.get_id()))
        print('table: ', end='')
        print(*self.__table)
        print(player.printed_hand)
        if self.verify_pieces(player) == None:
            piece = input('Choose your piece, Player {}:\n'.format(str(player.get_id())))
            side = input('What side will you play it?\n1 - Left \n2 - Right\n')
            try:
                if (int(piece) <= len(player.get_hand()) and int(piece) > 0) and side != '' and side in '12':
                # if piece != '' and piece in '123456789' and int(piece) <= len(player.get_hand()) and side != '' and side in '12':
                    if self.verify_side(player, piece, side) :
                        player.remove_piece(int(piece) - 1)
                else:
                    verif = input('invalid option, type any button to try again\n')
                    self.round(player)
            except:
                verif = input('invalid option, type any button to try again\n')
                self.round(player)
        else:
            ver = input('There are no more pieces to take, and you can\'t use any of those...')
            
    def verify_pieces(self, player):
        verifier = 0
        for my_piece in player.get_hand():
            if my_piece[0] != self.__table[0][0] and my_piece[1] != self.__table[0][0] and my_piece[0] != self.__table[-1][1] and my_piece[1] != self.__table[-1][1]:
                # a = input('139! this one won\'t do, lets see the next one')
                pass
            else:
                # b = input('141! this one will do, lets see the next one')
                verifier = 1
                
        if verifier == 0:
            # c = input('145! u shall now receive your piece')
            if len(self.__pieces) > 0:
                ver = input('One more piece to you, player {} \nType any button to continue...'.format(str(player.get_id())))
                num = randint(0, len(self.__pieces) - 1)
                player.add_piece(self.__pieces[num])
                self.__pieces.pop(num)
                self.verify_pieces(player)
            else:
                return False
            
    def verify_side(self, player, piece, side):
        if side == '1':
            if player.get_hand()[int(piece) - 1][1] == self.__table[0][0]:
                self.__table.insert(0, player.get_hand()[int(piece) - 1])
                return True
            elif player.get_hand()[int(piece) - 1][0] == self.__table[0][0]:
                temp = player.get_hand()[int(piece) - 1]
                temp.reverse()
                self.__table.insert(0, temp)
                return True
            else:
                ver = input('invalid option, try again')
                self.round(player)
        elif side == '2':
            if player.get_hand()[int(piece) - 1][0] == self.__table[-1][1]:
                self.__table.append(player.get_hand()[int(piece) - 1])
                return True
            elif player.get_hand()[int(piece) - 1][1] == self.__table[-1][1]:
                temp = player.get_hand()[int(piece) - 1]
                temp.reverse()
                self.__table.append(temp)
                return True
            else:
                ver = input('invalid option, try again')
                self.round(player)

    def someone_can_play(self):
        verifier = 0
        for piece in self.__player1.get_hand():
            if piece[0] != self.__table[0][0] and piece[1] != self.__table[0][0] and piece[0] != self.__table[-1][1] and piece[1] != self.__table[-1][1]:
                # a = input('174! this one won\'t do, lets see the next one')
                pass
            else:
                # b = input('177! this one will do, lets see the next one')
                verifier = 1
        
        for piece in self.__player2.get_hand():
            if piece[0] != self.__table[0][0] and piece[1] != self.__table[0][0] and piece[0] != self.__table[-1][1] and piece[1] != self.__table[-1][1]:
                # a = input('174! this one won\'t do, lets see the next one')
                pass
            else:
                # b = input('177! this one will do, lets see the next one')
                verifier = 1
                
        if verifier == 1 : return True
        
    def draw(self):
        
        if self.someone_can_play() : return False
        
        else:
            soma1 = 0
            soma2 = 0
            for piece in self.__player1.get_hand():
                soma1 += piece[0] + piece[1]
            for piece in self.__player2.get_hand():
                soma2 += piece[0] + piece[1]
            if soma1 == soma2 :
                print('It\'s a draw')
            if soma1 > soma2:
                print('Player 1 won')
            else:
                print('Player 2 won')
            return True
        
    def check_for_winner(self):
        if len(self.__player1.get_hand()) == 0:
            print('Player 1 won!')
            return False
        elif len(self.__player2.get_hand()) == 0:
            print('Player 2 won!')
            return False
        elif self.draw() : return False
        else: return True
            
    def loop(self):        
        running = True
        self.round1()
        self.round(self.__player2)
        while self.check_for_winner():
            if self.check_for_winner():
                print('player 2: ', self.__player2.get_hand())
                self.round(self.__player1)
            if self.check_for_winner():
                print('player 1: ', self.__player1.get_hand())
                self.round(self.__player2)
        
game = Game()
game.loop()