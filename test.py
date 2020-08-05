import pickle
from wallet import *


w1 = Wallet.generate_wallet()
w2 = Wallet.generate_wallet()
f = open('address.txt', 'w')
f.write(w1.address)
f.write('\n')
f.write(w2.address)
f.close()
ws = {}
ws[w1.address] = w1
ws[w2.address] = w2
f = open('wallet.dat', 'wb')
pickle.dump(ws, f)
f.close()
