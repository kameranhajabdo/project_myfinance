from abc import ABC, abstractmethod
from typing import List


class StockPersistanceInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[dict]:
        pass

    @abstractmethod
    def add(self, stock_info: dict):
        pass

    @abstractmethod
    def remove(self, stock_id: str):
        pass