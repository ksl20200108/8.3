import pickle


fo = open("address.txt", "r")
addrs = []
for line in fo:
    addrs.append(line[:34])
fo.close()
f = open('wallet.dat', 'rb')
wallets = pickle.load(f)
from_wallet = wallets[addrs[0]]
pub_key = from_wallet.private_key
print(pub_key)
