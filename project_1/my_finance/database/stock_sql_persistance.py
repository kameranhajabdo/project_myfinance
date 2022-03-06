import sqlite3

from stock.persistance_interface import StockPersistanceInterface


class StockSqlPersistance(StockPersistanceInterface):
    def __init__(self, path: str):
        self.path = path

    def get_all(self) -> list[dict]:
        #TODO get info from DB
        return []

    def add(self, stock_info: dict):
        command = f"INSERT INTO stocks (ticker, company, field, amount, long_summary, exchange, country, employees) " \
                  f"VALUES ('{stock_info['ticker']}','{stock_info['company']}','{stock_info['field']}',0," \
                  f"'{stock_info['longSummary']}','{stock_info['exchange']}','{stock_info['country']}'," \
                  f"{stock_info['numberOfEmployees']});"
        print("SQL command for add: " + command)
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
        connection.close()

    def remove(self, stock_id: str):

        pass