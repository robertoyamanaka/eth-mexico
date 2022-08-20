from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import json 

class Cmc_data():


    def __init__ (self):
        self.cmc = CoinMarketCapAPI("f13a5b69-a336-4a1f-ba41-b35d6ff62f24")
        self.json_data = {}
    
    def info_data(self, coin):
        try:
            r = self.cmc.cryptocurrency_info(symbol=coin)
            self.json_data.update(r.data)

            return r.data
        except CoinMarketCapAPIError as e:
            print(e)
            return None

    def get_extract_dats(self):
        raw_tokens = ["AVAX","QI","BTC","CSPR","CFG","CERE","CLV","ATOM","ETH","FTM","JOE","MINA","CAKE","PLGR","DOT","QUICK","BOO","TARA","RUNE","VEGA","XRP","SOL","DOGE","TRX","FLOW","EOS","AAVE","HNT","FTM","GRT","NEO","CEL","CRV","NEXO","TWT","CLV","GST","SAND","LRC","PLA","CHR","STG","XYO","ANT","ENJ","MVL","PMON","RFOX"]
        for x in raw_tokens:
            self.info_data(x)
    
    def export_data(self,name):
        self.get_extract_dats()

        with open(name, 'w') as outfile:
            json.dump(self.json_data, outfile)