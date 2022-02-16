from pydantic import BaseModel, Field

class StockModel(BaseModel):
      ticker: str = Field(description="The ticker ID of the stock, for example Tesla has TSLA")
      company: str = Field(default="",description="The full company name, leace empty for POST")
      field: str = Field(default="")


      class Config:
            orm_mode = True

