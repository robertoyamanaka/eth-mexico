import requests
import sys
import pandas as pd
import numpy as np

from coin_list import COIN_LIST

sys.path.append("../")
from keys.private_keys import LUNAR_CRUSH_BEARER_TOKEN


class LunarCrushData:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {LUNAR_CRUSH_BEARER_TOKEN}"}
        self.coin_list = COIN_LIST
        self.get_all_data()

    def get_json_data(self, symbol, starting_date="1660885200"):
        url = f"https://lunarcrush.com/api3/coins/{symbol}/time-series?interval=1w&start={starting_date}&bucket=day"
        response = requests.get(url, headers=self.headers)
        json_response = response.json()
        return json_response

    def get_all_data(self):
        responses = []
        for symbol in self.coin_list:
            json_response = self.get_json_data(symbol)
            combined_response = {
                **json_response["data"],
                **json_response["timeSeries"][0],
            }
            responses.append(combined_response)

        self.all_data = pd.DataFrame.from_records(responses)
        self.all_data = self.all_data.drop(
            [
                "news",
                "medium",
                "youtube",
                "reddit_posts",
                "reddit_posts_score",
                "reddit_comments",
                "reddit_comments_score",
            ],
            axis=1,
        )
        self.all_data.replace("", np.nan, inplace=True)
        self.all_data.dropna(axis=1, inplace=True)
