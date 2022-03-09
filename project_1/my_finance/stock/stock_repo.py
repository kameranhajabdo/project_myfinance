from stock.stock import Stock
from exceptions import StockNotFound
from stock.persistance_interface import StockPersistanceInterface


class StockRepository:
    def __init__(self, persistance: StockPersistanceInterface):
        self.stocks = {}
        self.persistance = persistance
        # self.__load()

    def add(self, new_stock: Stock):
        self.stocks[new_stock.ticker] = new_stock
        stock_info = {
            "ticker": new_stock.ticker,
            "company": new_stock.company,
            "amount": new_stock.amount,
            "field": new_stock.field,
            "longSummary": new_stock.long_summary,
            "exchange": new_stock.exchange,
            "country": new_stock.country,
            "numberOfEmployees": new_stock.number_of_employees,
        }
        self.persistance.add(stock_info)

    def get_all(self) -> list[Stock]:
        print([s.price for s in self.stocks.values()])
        return list(self.stocks.values())

    # if we do not have the stock, we can raise an error or return None
    def get_by_ticker(self, ticker: str) -> Stock:
        if ticker in self.stocks.keys():
            return self.stocks[ticker]
        else:
            raise StockNotFound()
        # return StockFactory().make_extended_stock(ticker)

    def remove(self, stock_id: str):
        self.stocks.pop(stock_id)
        self.persistance.remove(stock_id)

    def load(self):
        items = self.persistance.get_all()
        # items = list of dictionaries from the file
        for one_item in items:
            new_stock = Stock(one_item["ticker"], one_item["company"], one_item["field"],
                              one_item["country"], one_item["numberOfEmployees"], one_item["amount"])
            if "longSummary" in one_item and "exchange" in one_item:
                new_stock.set_long_summary(one_item["longSummary"])
                new_stock.set_exchange(one_item["exchange"])
            self.stocks[one_item["ticker"]] = new_stock