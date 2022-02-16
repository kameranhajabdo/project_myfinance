
class Stock:
    def __init__(self, ticker: str, company_name: str, field: str, amount: float = 0):
        self.ticker = ticker
        self.company = company_name
        self.field = field
        self.amount = amount

