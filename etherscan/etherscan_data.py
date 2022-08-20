import requests

class Etherscan_scan():

    KEYS_E = "UMAGCB1RZJRTJDGS4B4K58TYAV29G94KJ9" 
    KEYS_DB = "5b952b4639198bc01ac2d695232c58cfbac15ce7"

    def __init__(self, address):
        self.address = address

    def balance_eth(self):
        url = f"https://api.etherscan.io/api?module=account&action=balance&address={self.address}&tag=latest&apikey={Etherscan_scan.KEYS_E}"
        r = requests.get(url = url)
        data = r.json()
        eth_value = int(data["result"])/1000000000000000000
        return eth_value


c1 = Etherscan_scan("0x2cA2B328a6394A5f4DfB06cA22B14f2882d49b85")
print(c1.balance_eth())
        