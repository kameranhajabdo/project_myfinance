import json
from stock import Stock


class StockRepository:
    def __init__(self):
        self.stocks = {}
        # self.__load()

    def add(self, new_stock: Stock):
        self.stocks[new_stock.ticker] = new_stock
        self.__save()

    def get_all(self) -> list[Stock]:
        return list(self.stocks.values())

    def remove(self, stock_id: str):
        self.stocks.pop(stock_id)
        self.__save()

    def load(self):
        file = open("database.txt")
        json_items = file.read()
        file.close()
        items = json.loads(json_items)
        # items = list of dictionaries from the file
        for one_item in items:
            new_stock = Stock(one_item["ticker"], one_item["company"], one_item["field"], one_item["amount"])
            self.stocks[one_item["ticker"]] = new_stock

    def __save(self):
        list_json = json.dumps([{
            "ticker": x.ticker,
            "company": x.company,
            "amount": x.amount,
            "field": x.field
        } for x in self.stocks.values()], indent=0)
        file = open("database.txt", "w")
        file.write(list_json)
        file.close()