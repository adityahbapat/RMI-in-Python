# saved as Server.py
import Pyro4
import random
import os

stocks = [
    [0,"Jet Airways",1000,10],
    [1,"Maruti Suzuki",3586,30],
    [2,"Pooja Ent.",423,7]
    ]

@Pyro4.expose
class Kerberos(object):
    def get_stocks(self):
        return stocks

       
    def buy(self, sid, qty):
        stocks[sid][3] = stocks[sid][3] - qty
        return stocks
    
    def sell(self, sid, qty):
        stocks[sid][3] = stocks[sid][3] + qty
        return stocks
    
    def listdir(self):
    	return os.listdir('./Server/')


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(Kerberos)   # register the greeting maker as a Pyro object
ns.register("example.kerb", uri)   # register the object with a name in the name server

print("Hi. Kerberos is now active.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls