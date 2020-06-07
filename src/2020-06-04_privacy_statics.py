import random

class Account:
    __balance=0
    __number=''
    __name=''

    def __init__(self, name):
        self.__name = name
        self.__number = 'N'+str(random.randint(1000,1999))

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
       self.__balance=value

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

class Bank:
    __accounts=[]

    @staticmethod
    def __printAccount(account):
        print('Account number: ', account.name)
        print('Account number: ', account.number)
        print('Account current balance: ', account.balance)
        print()

    @classmethod
    def printAccount(cls, number):
        for acc in cls.__accounts:
            if(acc.number == number):
                Bank.__printAccount(acc)

    @classmethod
    def removeAccount(cls, number, name, balance):
        index=0
        for acc in cls.__accounts:
            if(acc.number == number and
                acc.name == name and
                acc.balance == balance):
                del cls.__accounts[index]
                cls.__accounts.remove(index)
                print('Account deleted')
            index = index + 1

    @classmethod
    def createAccount(cls, name):
        for acc in cls.__accounts:
            if(acc.name == name):
                print('Account exist')
                return

        account = Account(name)
        cls.__accounts.append(account)
        print('Account created')
        Bank.__printAccount(account)

    @classmethod
    def changeBalance(cls, number, value):
        for acc in cls.__accounts:
            if(acc.number == number):
                acc.balance = acc.balance+value
                Bank.__printAccount(acc)

if __name__ == '__main__':
    while True:
        operation = input('Action: exit (E), create new account (C), print account data (P), change balance (B), remove account (R): ')
        if operation == 'E':
            break
        if operation == 'C':
            name = input('Give a name: ')
            Bank.createAccount(name)
        if operation == 'P':
            number = input('Give a number: ')
            Bank.printAccount(number)
        if operation == 'B':
            number = input('Give a number: ')
            try:
                balance = float(input('Give a value to add or substract: '))
                Bank.changeBalance(number, balance)
            except ValueError:
                print('Given value is not a number')
        if operation == 'R':
            number = input('Give a number: ')
            name = input('Give a name: ')
            try:
                b = input('Give a current balance: ')
                balance=0
                if b != '0':
                    balance = float(b)
                Bank.removeAccount(number, name, balance)
            except ValueError:
                print('Given balance is not a number')
            

    
