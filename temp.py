file = open('system.txt', 'r')

itens = file.readlines()[1].split(' ')
print(itens)