# import the libraries
import pandas as pd
from pytrends.request import TrendReq


class GoogleTrend:
    def __init__(self, keyword, year_start=2021, month_start=9):
        self.keyword = keyword
        self.keyword_list = [keyword]
        self.year_start = year_start
        self.month_start = month_start
        self.pytrend = TrendReq()
        self.historicaldf = self.pytrend.get_historical_interest(
            self.keyword_list,
            year_start=self.year_start,
            month_start=self.month_start,
            day_start=1,
            hour_start=0,
            year_end=2022,
            month_end=9,
            day_end=1,
            hour_end=0,
            cat=0,
            geo="",
            gprop="",
            sleep=2,
        )
        self.clean_data()
        self.summarize_data()  # Monthly

    def clean_data(self):
        self.historicaldf.drop(["isPartial"], axis=1, inplace=True)
        self.historicaldf = self.historicaldf.reset_index(level=0)
        self.historicaldf["date"] = pd.to_datetime(
            self.historicaldf.date, format="%Y-%m-%d"
        )

    def summarize_data(self):  # Monthly
        self.historicaldf["date"] = self.historicaldf["date"].dt.strftime("%Y-%m")
        self.historicaldf = self.historicaldf.groupby(["date"]).sum().reset_index()

    def get_rolling_window(self, min_cut, max_cut):
        self.historicaldf = self.historicaldf[self.historicaldf["date"] >= min_cut]
        self.historicaldf = self.historicaldf[self.historicaldf["date"] <= max_cut]
        self.historicaldf["acum_change"] = 100 * (
            1
            + self.historicaldf[self.keyword].diff()
            / self.historicaldf[self.keyword].iloc[0]
        )

    def get_correlation(
        self,
        extra_gtrend,
        min_cut="2021-09",
        max_cut="2022-09",
    ):
        self.get_rolling_window(min_cut, max_cut)
        extra_gtrend.get_rolling_window(min_cut, max_cut)
        corr = self.historicaldf["acum_change"].corr(
            extra_gtrend.historicaldf["acum_change"]
        )
        return corr

    # def get_relevance(self):
    #     is_relevantdf = pd.DataFrame()
    #     is_relevantdf["date"] = self.historicaldf["date"]
    #     is_relevantdf["min_relevance"] = RELEVANCE
    #     self.historicaldf = pd.merge(
    #         self.historicaldf, is_relevantdf, on="date", how="left"
    #     )
    #     self.historicaldf["is_relevant"] = self.historicaldf[self.keyword].gt(
    #         self.historicaldf["min_relevance"]
    #     )
    #     self.historicaldf.drop(["min_relevance"], axis=1, inplace=True)

    # def is_relevant(self, min_date="2022-08"):
    #     min_date = datetime.strptime(min_date, "%Y-%m")
    #     return self.historicaldf[self.historicaldf["date"] > min_date][
    #         "is_relevant"
    #     ].any()
