import requests


SUBGRAPHS = {
    "premia-mainnet": "https://gateway.thegraph.com/api/{}/subgraphs/id/3nXfK3RbFrj6mhkGdoKRowEEti2WvmUdxmz73tben6Mb",
    "livepeer": "https://gateway.thegraph.com/api/{}/subgraphs/id/FDD65maya4xVfPnCjSgDRBz6UBWKAcmGtgY6BmUueJCg",
    "lido": "https://gateway.thegraph.com/api/{}/subgraphs/id/HXfMc1jPHfFQoccWd7VMv66km75FoxVHDMvsJj5vG5vf",
    "rai-mainnet": "https://gateway.thegraph.com/api/{}/subgraphs/id/D4kczV9c2KTC5GArH2M54gs5mGZaigBpsiR7rCwgHqBX",
    "audius-mainnet": "https://gateway.thegraph.com/api/{}/subgraphs/id/CptFsHp6zar7kdfGYbVAqMeF1wNA1pJs6GaaJvPgeCfu",
    "connext-network": "https://gateway.thegraph.com/api/{}/subgraphs/id/DfD1tZSmDtjCGC2LeYEQbVzj9j8kNqKAQEsYL27Vg6Sw",
    "sushi-mainnet": "https://gateway.thegraph.com/api/{}/subgraphs/id/D7azkFFPFT5H8i32ApXLr34UQyBfxDAfKoCEK4M832M6",
    "uma-mainnet": "https://gateway.thegraph.com/api/{}/subgraphs/id/41LCrgtCNBQyDiVVyZEuPxbvkBH9BxxLU3nEZst77V8o",
    "pooltogether": "https://gateway.thegraph.com/api/{}/subgraphs/id/6v8a77TMhCrSECtSdTAAitCnrqg7cqHuYSDfwoFLhDe2",
    "mstable-protocol": "https://gateway.thegraph.com/api/{}/subgraphs/id/HTmE4KFztgBCbs2fdM7ai3jV32nufPs4xqXqfnLU3WRU",
    "synth-mainnet": "https://gateway.thegraph.com/api/{}/subgraphs/id/H87NmTfhtQRmUVzwWzZDZ6SzqvSnJe4CqDSY1pE1bhVS",
    "dodoex-v2": "https://gateway.thegraph.com/api/{}/subgraphs/id/GxV9XL6Wnjz75z919NPNdrLhEkqDR99PweUY3oh7Lh94",
    "hop-protocol-mainnet": "https://gateway.thegraph.com/api/{}/subgraphs/id/Cjv3tykF4wnd6m9TRmQV7weiLjizDnhyt6x2tTJB42Cy",
    "uniswap-v2": "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2",
    "doodle-bucket-auction": "https://gateway.thegraph.com/api/{}/subgraphs/id/zgYQMZnyfRtH4vyvTZE6TLtkPLfCpDreg6rPHzWrJm2",
    "polkabridge-amm": "https://gateway.thegraph.com/api/{}/subgraphs/id/4CUsiX9vBdi7FUwn28JEqzjuCumMrEzvBtctHQZmGiEt",
}


class SubGraph:
    def __init__(self, subgraph_name, api_key):
        self.subgraph_name = subgraph_name
        self.subgraph_url = SUBGRAPHS[subgraph_name]
        self.api_key = api_key

    def run_query(self, query):
        # endpoint where you are making the request
        request = requests.post(
            self.subgraph_url.format(self.api_key),
            json={"query": query},
        )
        if request.status_code < 400:
            return request.json()
        else:
            raise Exception(f"Query failed, {request.status_code}")
