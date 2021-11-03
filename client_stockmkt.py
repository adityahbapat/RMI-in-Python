# saved as client.py

import Pyro4
from datetime import datetime
kerberos = Pyro4.Proxy("PYRONAME:example.kerb") # use name server

class Customer:
  def __init__(self, name):
    self.name = name
    #Company,Price,Quantity,Datetime
    self.list_stocks = [
    ["Jet Airways",1000,0,datetime.now()],
    ["Maruti Suzuki",3586,0,datetime.now()],
    ["Pooja Ent.",423,0,datetime.now()]
]
#Start of the client code---------------------------------------
print("Welcome to StockPred. Please enter your details")

name = input("Enter name : ")
username = input("Enter username : ")
# gender = input("Enter gender(M/F) : ")
person = Customer(name)


#object lookup uri shortcut
#name = input("What is your name? ").strip()
#print(kerberos.get_fortune(name))
#a,b = input("Enter price at shares are bought and selling price of shares
#").split(' ')
#print(kerberos.get_profit(a,b))
stocks=kerberos.get_stocks()

print("id \t| Stocks \t\t| Price \t| Quantity Available ")
for i in range(len(person.list_stocks)):
    print(str(stocks[i][0]) + "\t|" + stocks[i][1] +" \t\t| " + str(stocks[i][2])  +" \t\t| " + str(stocks[i][3]))
print("\n")

while(True):
    n = int(input("1: View DashBoard \n2: Buy Stocks \n3: Sell Stocks \n4: Market \n5: Exit \n>> "))
    print("\n")
    if(n==1):
        print("id \t| Company \t| Price \t| Quantity \t| Date")

        for i in range(len(person.list_stocks)):
            print(str(i) + "\t|" + person.list_stocks[i][0] +" \t| " + str(person.list_stocks[i][1])  +" \t\t| " + str(person.list_stocks[i][2])  +" \t\t| " + str(person.list_stocks[i][3]))
        print("\n")

    elif(n == 2):
        stocks=kerberos.get_stocks()
        sid = int(input("Enter the id of the stock you want to buy:"))
        qty = int(input("Enter the Quantity:"))
        qty_av = stocks[sid][3]
        print("Quantity Available:" + str(qty_av))
        if(qty > qty_av):
            print("Sorry! Cannot buy the Stock")
        else:
            person.list_stocks[sid][2] = person.list_stocks[sid][2] + qty
            stocks[sid][3] = stocks[sid][3] - qty
            print(str(qty) + " Stocks bought of Company " + person.list_stocks[sid][0] + " at price:" + str(person.list_stocks[sid][1]))
            kerberos.buy(sid,qty)
            stocks=kerberos.get_stocks()
            print("\n")
    elif(n == 3):
        stocks=kerberos.get_stocks()
        sid2 = int(input("Enter the id of the stock you want to sell:"))
        qty_av_2 = person.list_stocks[sid2][2]
        print("Quantity Available with you:" + str(qty_av_2))
        qty2 = int(input("Enter the Quantity:"))
        if(qty2 > qty_av_2):
            print("Sorry! Cannot sell the Stock")
        else:
            person.list_stocks[sid2][2] = person.list_stocks[sid2][2] - qty2
            stocks[sid2][3] = stocks[sid2][3] + qty2
            print(str(qty2) + " Stocks sold of Company " + person.list_stocks[sid2][0] + " at price:" + str(person.list_stocks[sid2][1]))
            kerberos.sell(sid2,qty2)
            stocks=kerberos.get_stocks()
            print("\n")
    elif(n == 4):
        stocks=kerberos.get_stocks()
        print("id \t| Stocks \t\t| Price \t| Quantity Available |")
        for i in range(len(person.list_stocks)):
            print(str(stocks[i][0]) + "\t|" + stocks[i][1] +" \t\t| " + str(stocks[i][2])  +" \t\t| " + str(stocks[i][3]))
        print("\n")
    else:
        break

