import yfinance
import sys

from models import StockModel
from stock import Stock


class StockFactory:
    def make(self, info: StockModel) -> Stock:
        yf_ticker = yfinance.Ticker(info.ticker)
        company = yf_ticker.info["longName"]
        field = yf_ticker.info["sector"]
        new_stock = Stock(info.ticker, company, field)
        return new_stock