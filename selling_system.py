import os

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    def get_username(self):
        return self.__username
    
    def set_username(self, username):
        self.__username = username
        
    def get_password(self):
        return self.__username
    
    def set_password(self, password):
        self.__password = password
        
class Seller:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
        
class Sale:
    def __init__(self, seller, groups_list):
        self.__seller = seller
        self.__groups_list = groups_list
        
    def get_seller(self):
        return self.__seller
    
    def set_seller(self, seller):
        self.__seller = seller
        
    def get_itens_groups(self):
        return self.groups_list
    
    def set_itens_groups(self, itens_groups):
        self.__itens = itens_groups
        
    def get_total(self):
        total = 0
        for group in self.groups_list:
            total += (group.get_quantity() * group.get_item().get_price())
        return total
    
    def get_sale(self):
        to_be_printed = 'Seller: ' + self.__seller + '   '
        for group in self.__groups_list:
            to_be_printed += group.get_quantity() + '   ' + group.get_item().get_name() + '   ' + str(group.get_item().get_price()) + '   ' + str(group.get_total()) + '\n'
        return to_be_printed

class Item:
    
    def __init__(self,_id, name, price):
        self.__id = _id
        self.__name = name
        self.__price = price        

    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
        
class Group:
    def __init__(self, quantity, item):
        self.__quantity = quantity
        self.__item = item
        
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, quantity):
        self.__quantity = quantity
        
    def get_item(self):
        return self.__item
    
    def set_item(self, item):
        self.__item = item
        
    def get_total(self):
        return float(self.__quantity) * float(self.__item.get_price())
        
class Store:
    def __init__(self):
        admin = User('admin', 'admin')
        self.__users_list = [admin]
        self.__sellers_list = []
        self.__itens_list = []
        self.__sales_list = []
        self.__id = 0
        
    def get_itens_list(self):
        return self.__itens_list    
    
    def get_sales_list(self):
        return self.__sales_list
    
    #only for test purposes, must be deleted further
    def get_sellers_list(self):
        return self.__sellers_list
        
    def login(self, name, password):
        for i in self.__users_list:
            if (i.get_username() == name and i.get_password() == password):
                return False
        return True
    
    def add_seller(self, name):
        if len(self.__sellers_list) > 0:
            for seller in self.__sellers_list:
                if name != seller.get_name():
                    new_seller = Seller(name)
                    self.__sellers_list.append(new_seller)
                    return True
        else:
            new_seller = Seller(name)
            self.__sellers_list.append(new_seller)
            return True
    
    def add_item(self, name, price):
        if len(self.__itens_list) > 0:
            for item in self.__itens_list:
                new_item = Item(self.__id, name, price)
                self.__itens_list.append(new_item)
                self.__id += 1
                return True
        else:
            new_item = Item(self.__id, name, price)
            self.__itens_list.append(new_item)
            self.__id += 1
            return True
    
    def add_sale(self, seller, groups_list):
        new_sale = Sale(seller, groups_list)
        self.__sales_list.append(new_sale)

class main:
    
    def __init__(self):
        self.__store = Store()
    
    def login(self):
        login_finish = True
        while login_finish:
            user = input('Insert the user:\n')
            password = input('Insert the password:\n')
            login_finish = self.__store.login(user, password)
            if(login_finish == True):
                os.system('clear')
                print('Invalid credentials')
                self.login()
                
    def set_sale(self, seller_name, groups_list):
        item_name = input('Insert the items name or id:\n')
        for item in self.__store.get_itens_list():
            if item_name == item.get_id() or item_name == item.get_name():
                quantity = input('Insert the quantity: ')
                new_group = Group(quantity, item)
                groups_list.append(new_group)
                recursion = input('Do you wish to insert a new item to the sale? \n1 - Yes \n2 - No\n')
                if recursion == '1':
                    self.set_sale(seller_name, groups_list)
        self.__store.add_sale(seller_name, groups_list)
    
    def menu(self):
        # the following four lines are only for test purposes and must be deleted further
        os.system('clear')
        print('sales = ', self.__store.get_sales_list())
        print('itens = ', self.__store.get_itens_list())
        print('sellers = ', self.__store.get_sellers_list())
        # os.system('clear')
        print('Logged in\n')
        choice = input('''Type the number referent to your choice:
1 - Make a sale
2 - Add a new item
3 - Add a new seller
4 - View sales
5 - Shut down\n\n''')
        if choice == '5':
            return False
        if choice == '4':
            for sale in self.__store.get_sales_list():
                print(sale.get_sale())
            verify = input('Type any button to go back go menu')
            return True
        if choice == '3':
            seller_name = input('Insert a name:\n')
            self.__store.add_seller(seller_name)
            return True
        if choice == '2':
            item_name = input('Insert the items name:\n')
            price = float(input('Insert the price of the item:\n'))
            self.__store.add_item(item_name, price)
            return True
        if choice == '1':
            groups_list = []
            seller_name = input('Insert the seller: ')
            self.set_sale(seller_name, groups_list)
            return True

main = main()
main.login()
loop = True
while loop:
    loop = main.menu()