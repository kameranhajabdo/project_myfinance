import json
from stock.persistance_interface import StockPersistanceInterface


class StockFilePersistance(StockPersistanceInterface):
    def __init__(self, path: str):
        self.path = path

    def get_all(self) -> list[dict]:
        file = open(self.path)
        json_items = file.read()
        file.close()
        items = json.loads(json_items)
        return items

    def add(self, stock_info: dict):
        items = self.get_all()
        items.append(stock_info)
        list_json = json.dumps(items, indent=2)
        self.__save(list_json)

    def __save(self, list_json):
        file = open(self.path, "w")
        file.write(list_json)
        file.close()

    def remove(self, stock_id: str):
        items = self.get_all()
        items = [i for i in items if i ["ticker"] != stock_id]
        list_json = json.dumps(items, indent=2)
        self.__save(list_json)


