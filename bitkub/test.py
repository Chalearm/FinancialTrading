import json
import pandas as pd
from bitkub import bitkub
def printPrice(bk,name):
	price = bk.getprice(name)
	print(name+' : '+"{:,.4f}".format(price))
	
#API info
API_HOST = 'https://api.bitkub.com'
API_KEY = '7eaf2193a7e4f29051c492eab996adc1'
API_SECRET = b'8e0f553a18d9194865c1cdee35645982'
bk =bitkub(API_HOST=API_HOST,
     	   API_KEY=API_KEY,
           API_SECRET=API_SECRET)
printPrice(bk,'THB_BTC')
printPrice(bk,'THB_ETH')
printPrice(bk,'THB_XRP')
printPrice(bk,'THB_IOST')
printPrice(bk,'THB_INF')
printPrice(bk,'THB_SIX')
printPrice(bk,'THB_DOGE')

print('My Wallet :')
myWallets = bk.wallets()
myBalances = bk.balances()
pd.set_option('display.max_columns',None)
pd.set_option('display.expand_frame_repr',False)
pd.set_option('max_colwidth',-1)
df = pd.DataFrame(myWallets)
df2 = pd.DataFrame(myBalances['result'])
del df['error']
print(df)
print(df2)
product = 'THB_XRP'
zone = 8.5 
amount = 10 
#order = bk.createbuy(name=product,amount=float(amount),rate=float(zone),ordertype='limit')
