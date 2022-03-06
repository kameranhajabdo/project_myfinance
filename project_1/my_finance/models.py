from pydantic import BaseModel, Field

class StockModel(BaseModel):
      ticker: str = Field(description="The ticker ID of the stock, for example Tesla has TSLA")
      company: str = Field(default="",description="The full company name, leace empty for POST")
      field: str = Field(default="")


      class Config:
            orm_mode = True

class StockExtendedModel(StockModel):
      long_summary: str = Field(description="The business summary of the company")
      exchange: str = Field(description="the name of the exchange")
      country: str = Field()
      number_of_employees: str = Field()

