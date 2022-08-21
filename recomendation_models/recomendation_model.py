import json
import pandas as pd

from description_similarities.description_similarities import (
    get_most_similar_description,
)
from google_trends.google_trends import GoogleTrend
from kmeans.kmeans import get_min_distance_symbol


class RecomendationModel:
    def __init__(self, symbol_json):
        self.symbol_json = symbol_json
        self.load_20_coins()
        self.get_similarities_list()
        # self.get_20_google_trends()
        # self.get_symbol_json_google_trends()
        # self.get_google_trends_scores()
        self.get_kmeans_scores()
        self.get_final_scores()

    def load_20_coins(self):
        json_filename = (
            "/Users/robertoyamanaka/Documents/EthHack/eth-mexico/data/cmc_data_20.json"
        )
        with open(json_filename) as f:
            self.symbol_json_20 = json.load(f)

    # Getting description similarities
    def get_similarities_list(self):
        self.sentence_similarity_scores = {}
        for symbol in self.symbol_json:
            self.sentence_similarity_scores[symbol] = get_most_similar_description(
                symbol
            )

    # Getting google trends
    def get_20_google_trends(self):
        self.symbol_json_20_google_trends = []
        for symbol in self.symbol_json_20:
            keyword = "$" + symbol
            symbol_google_trend = GoogleTrend(keyword=keyword)
            self.symbol_json_20_google_trends.append({symbol: symbol_google_trend})

    def get_symbol_json_google_trends(self):
        self.symbol_json_google_trends = []
        for symbol in self.symbol_json:
            if symbol in list(self.symbol_json_20.keys()):
                self.symbol_json_google_trends.append(
                    self.symbol_json_20_google_trends[self.symbol_json_20.index(symbol)]
                )
            else:
                try:
                    keyword = "$" + symbol
                    symbol_google_trend = GoogleTrend(keyword=keyword)
                    self.symbol_json_google_trends.append({symbol: symbol_google_trend})
                except:
                    self.symbol_json_google_trends.append({symbol: {}})

    def get_google_trends_scores(self):
        self.google_trends_scores = {}
        for symbol in self.symbol_json_google_trends:
            try:
                symbol_key = list(symbol.keys())[0]
                symbol_google_trend = list(symbol.values())[0]
                max_score = 0
                most_similar = ""
                for symbol_20 in self.symbol_json_20_google_trends:
                    symbol_key_20 = list(symbol_20.keys())[0]
                    if symbol_key != symbol_key_20:
                        symbol_google_trend_20 = list(symbol_20.values())[0]
                        score = symbol_google_trend.get_correlation(
                            symbol_google_trend_20
                        )
                        if score > max_score:
                            max_score = score
                            most_similar = symbol_key_20

                self.google_trends_scores[symbol_key] = {
                    "similar_symbol": most_similar,
                    "score": score,
                }
            except:
                self.google_trends_scores.append({symbol: {}})

    # K means
    def get_kmeans_scores(self):
        self.kmeans_scores = {}
        df_coords = pd.read_csv(
            "/Users/robertoyamanaka/Documents/EthHack/eth-mexico/recomendation_models/kmeans/kmeans_results_2.csv"
        )
        for symbol in self.symbol_json:
            similar_symbol, score_raw = get_min_distance_symbol(
                symbol, df_coords, self.symbol_json_20
            )
            score = 1 - score_raw / 40
            self.kmeans_scores[symbol] = {
                "similar_symbol": similar_symbol,
                "percentage": score,
            }

    def get_final_scores(self):
        self.final_scores = {}
        # self.sentence_similarity_scores = {
        #     "GEL": {"similar_symbol": "APE", "percentage": 0.39872121810913086},
        #     "SUSHI": {"similar_symbol": "UNI", "percentage": 0.5800848007202148},
        #     "SNX": {"similar_symbol": "HEX", "percentage": 0.34170082211494446},
        #     "DAI": {"similar_symbol": "APE", "percentage": 0.5156382918357849},
        #     "APE": {"similar_symbol": "DAI", "percentage": 0.5156382918357849},
        # }
        if not self.google_trends_scores:
            self.google_trends_scores = {
                "GEL": {"similar_symbol": "APE", "percentage": 0.5},
                "SUSHI": {"similar_symbol": "UNI", "percentage": 0.5},
                "SNX": {"similar_symbol": "HEX", "percentage": 0.5},
                "DAI": {"similar_symbol": "APE", "percentage": 0.5},
                "APE": {"similar_symbol": "DAI", "percentage": 0.5},
            }
        for symbol in self.symbol_json:
            score_results = []
            desc_similarities = self.sentence_similarity_scores[symbol]
            score_results.append(desc_similarities)
            google_trends = self.google_trends_scores[symbol]
            score_results.append(google_trends)
            kmeans = self.kmeans_scores[symbol]
            score_results.append(kmeans)
            final_df = pd.DataFrame.from_records(score_results)
            final_df = final_df.groupby(["similar_symbol"]).mean().reset_index()
            final_similar_symbol = final_df[
                final_df["percentage"] == final_df["percentage"].max()
            ]["similar_symbol"].values[0]
            final_percentage = final_df[
                final_df["percentage"] == final_df["percentage"].max()
            ]["percentage"].values[0]
            self.final_scores[symbol] = {
                "similar_symbol": final_similar_symbol,
                "percentage": final_percentage,
            }
