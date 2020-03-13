dict_x = {'1': 3, '2': 6, '3': 9, '4': 12, '5': 15, '6': 18, '7': 21, '8': 24, '9': 27, '10': 30, '11': 33, '12': 36, '13': 39, '14': 42}
dict_y = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14}

class Player:
    def __init__(self):
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
    
    def get_boats(self):
        return self.__boats
    
    def decrement_boats(self):
        self.__boats -= 1
        
    def get_map(self):
        return self.__map
    
    def set_map_line(self, line_number, new_line):
        self.__map[line_number] = new_line
    
    def print_map(self, viewer):
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
        print('Your boats: {}\n Your enemys boats: {}'.format(self.get_boats(), enemy.get_boats()) + '\n')
        self.print_map()
        x_cor = input('Type the X coordinate: ')
        y_cor = input('Type the Y coordinate: ')
        if x_cor not in '12345678911121314' or y_cor not in 'ABCDEFGHIJKLMN':
            print('Invalid coordinate')
            self.attack(enemy)
        else:
            listed = list(enemy.get_map()[dict_y[y_cor]])
            if listed[dict_x[x_cor]] == 'O':
                listed[dict_x[x_cor]] = 'X'
                new_line = ''.join(listed)
                enemy.set_map_line(dict_y[y_cor], new_line)
                enemy.decrement_boats()
                print('You\'ve got one! Make another move!')
                self.attack(enemy)
            else:
                listed[dict_x[x_cor]] = '#'
                print('You\'ve lost that one...')

class main():
    def __init__(self):
        self.__player1 = Player()
        self.__player2 = Player()
    
    def rounds(self):
        while self.__player1.get_boats() > 0 and self.__player2.get_boats() > 0:
            