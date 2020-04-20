dict_x = {'1': 3, '2': 6, '3': 9, '4': 12, '5': 15, '6': 18, '7': 21, '8': 24, '9': 27, '10': 30, '11': 33, '12': 36, '13': 39, '14': 42}
dict_y = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14}

class Player:
    def __init__(self, _id):
        self.__id = _id
        self.__counter = 5
        self.__boats = 5
        self.__map = ['0  1  2  3  4  5  6  7  8  9  10 11 12 13 14',
                      'A  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'B  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'C  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'D  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'E  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'F  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'G  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'H  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'I  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'J  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'K  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'L  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'M  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~',
                      'N  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~']
    
    def add_boat(self):
        print(self.printed_map('me'))
        print('Player {}: Insert your boats location'.format(self.__id))
        cords = input('Type the alfabetical coordinate followed by the number coordinate: ')
        if (cords != '' and cords[0] in 'ABCDEFGHIJKLMN' and cords[1] in '123456789'):
            listed = list(self.__map[dict_y[cords[0]]])
            if (len(cords) == 2) and (cords[1] in '123456789' and cords[0] in 'ABCDEFGHIJKLMN') and (self.get_map()[dict_y[cords[0]]][dict_x[cords[1]]] == '~'):
                listed[dict_x[cords[1]]] = 'O'
            elif (len(cords) == 3) and (cords[1:3] == '10' or cords[1:3] == '11'  or cords[1:3] == '12'  or cords[1:3] == '13'  or cords[1:3] == '14') and cords[0] in 'ABCDEFGHIJKLMN' and (self.get_map()[dict_y[cords[0]]][dict_x[cords[1]]] == '~'):
                listed[dict_x[cords[1:3]]] = 'O'    
            self.__map[dict_y[cords[0]]] = ''.join(listed)
            self.__counter -= 1
        else:
            print('invalid coordinates')
        return self.__counter
    
    def get_boats(self):
        return self.__boats
    
    def decrement_boats(self):
        self.__boats -= 1
        
    def get_map(self):
        return self.__map
    
    def set_map_line(self, line_number, new_line):
        self.__map[line_number] = new_line
    
    def printed_map(self, viewer):
        printed = ''
        if viewer == 'me':
            for line in self.__map:
                printed += line + '\n'
            return printed
        elif viewer == 'enemy':
            printed = self.__map[0] + '\n'
            for line in range(1,15):
                listed = list(self.__map[line])
                for character in range(len(listed)):
                    if listed[character] == 'O':
                        printed += '~'
                    else:
                        printed += listed[character]
                printed += '\n'
            return printed

    def attack(self, enemy):
        print('Your boats: {}\nYour enemys boats: {}'.format(self.get_boats(), enemy.get_boats()) + '\n')
        print('Your map:\n')
        print(self.printed_map('me'))
        print('Your enemys map:\n')
        print(enemy.printed_map('enemy'))
        cords = input('Type the alfabetical coordinate followed by the number coordinate: ')
        
        if (cords != '' and len(cords) < 4 and len(cords) > 1 and cords[0] in 'ABCDEFGHIJKLMN'):
            if (len(cords) == 2 or len(cords) == 3) and ((cords[1] in '123456789' or ( cords[1:3] == '10' or cords[1:3] == '11'  or cords[1:3] == '12'  or cords[1:3] == '13'  or cords[1:3] == '14')) and cords[0] in 'ABCDEFGHIJKLMN'):
                if len(cords) == 2:
                    x_cor = cords[1]
                else:
                    x_cor = cords[1:3]
                
                y_cor = cords[0]
                listed = list(enemy.get_map()[dict_y[y_cor]])
                if listed[dict_x[x_cor]] == 'O':
                    listed[dict_x[x_cor]] = 'X'
                    enemy.decrement_boats()
                    print('You\'ve got one!')
                elif listed[dict_x[x_cor]] == '~' or listed[dict_x[x_cor]] == '#':
                    listed[dict_x[x_cor]] = '#'
                    print('You\'ve lost that one...')
                
                new_line = ''.join(listed)
                enemy.set_map_line(dict_y[y_cor], new_line)
        else:
            print('invalid coordinates')
            self.attack(enemy)
                
    def get_counter(self):
        return self.__counter

class main():
    def __init__(self):
        self.__player1 = Player('1')
        self.__player2 = Player('2')
    
    def set_boats(self):
        counter1 = 0
        counter2 = 0
        while self.__player1.add_boat() > 0: pass
        while self.__player2.add_boat() > 0: pass
    
    def rounds(self):
        check = True
        while check:
            print('hacked:\n', self.__player1.get_map())
            self.__player1.attack(self.__player2)
            if self.__player2.get_boats() == 0:
                print('Player 1 won!')
                break
            else:
                self.__player2.attack(self.__player1)
                if self.__player1.get_boats() == 0:
                    print('Player 2 won!')
                    break
                
    def get_player1(self):
        return self.__player1
    
    
    def get_player2(self):
        return self.__player2
                
main = main()
main.set_boats()
main.rounds()