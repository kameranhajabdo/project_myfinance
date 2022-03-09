# this is our root file, when we execute this we will start our app
# webpage for fastapi framework https://fastapi.tiangolo.com/tutorial/,
# also https://realpython.com/fastapi-python-web-apis/

# uvicorn index:app --reload --port 7777
# uvicorn is the server which will start
# index:app, index -> the file name, app -> the FastAPI object name
# --reload -> the server will restart when we modify the code
# --port <port_number> -> select on which port to start


from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_utils.tasks import repeat_every

from stock.stock_factory import StockFactory
from stock.stock_repo import StockRepository
from configuration.config import Configuration
from database.stock_file_persistance import StockFilePersistance
from database.stock_sql_persistance import StockSqlPersistance
from models import StockModel, StockExtendedModel
from exceptions import StockNotFound

app = FastAPI(
    title="Name of our app",  # TODO for homework, name your application
    # <major_version>.<minor_version>.<patch_version>
    version="0.2.0",  # increase version after finishing homework
    description="",  # TODO add a description
)


@app.get(
    "/health",
    summary="This will be visible at start",
    description="We can describe this API call",
    response_description="We can describe the response",
)
def health() -> dict:
    return {
        "status": "online",
        "engine": "on",
    }


conf = Configuration()
if conf.get_db_type() == "file":
    persistance = StockFilePersistance(conf.get_db_path())
if conf.get_db_type() == "sql":
    persistance = StockSqlPersistance(conf.get_db_path())
stock_repo = StockRepository(persistance)


@app.post("/stocks")
def add_new_stock(stock_info: StockModel):
    new_stock = StockFactory().make_from_model(stock_info)
    stock_repo.add(new_stock)


# example if you want to do a tasks app return the list of tasks, and rename the url /items -> /tasks
@app.get("/stocks", response_model=list[StockModel])
def get_stocks(field: str = None, min_employees: int = None, page: int = None, items_per_page: int = None):
    stocks = stock_repo.get_all()
    if field:
        stocks = [s for s in stocks if s.field == field]
    if min_employees:
        stocks = [s for s in stocks if s.number_of_employees >= min_employees]
    if page is not None and page >= 0:
        # below, it's called a ternary operator
        number_of_items_per_page = items_per_page if items_per_page else conf.get_number_of_items_per_page()
        # page = 0, 0:2
        # page = 1, 2:4
        stocks = stocks[page * number_of_items_per_page:(page + 1) * number_of_items_per_page]
    return stocks


# TODO create a get for a single stock, we give the ticker and receive more information
# additional information: long summary, on which exchange it is, country, number of employees, industry

# we can put an id in the URL to select only one resource
@app.get("/stocks/{ticker_id}", response_model=StockExtendedModel)
def get_one_stock(ticker_id: str):
    return stock_repo.get_by_ticker(ticker_id)


# TODO add a put method to edit your domain item


@app.delete("/stocks")
def remove_stock(ticker: str):
    stock_repo.remove(ticker)


@app.on_event("startup")
def load_list_of_items():
    stock_repo.load()
    tickers = stock_repo.stocks.keys()
#    for a_ticker in tickers:
#        yf_ticker = yfinance.Ticker(a_ticker)
#        price = yf_ticker.info["currentPrice"]
#        stock_repo.stocks[a_ticker].set_price(price)


import yfinance
# import logging
# import sys

# @repeat_every(seconds=5, wait_first=True, logger=logging.basicConfig(stream=sys.stdout, level=logging.DEBUG))  # every 5 seconds we run this function
# def update_prices():
#     # get all stocks
#     # get price (yfinance)
#     # stock set price
     if not stock_repo.stocks:
         return
     print("ssss ------ sssss")
     tickers = stock_repo.stocks.keys()
     for a_ticker in tickers:
         yf_ticker = yfinance.Ticker(a_ticker)
         price = yf_ticker.info["currentPrice"]
         stock_repo.stocks[a_ticker].set_price(price)


@app.exception_handler(StockNotFound)
def handle_stock_not_found(exception, request):
    return JSONResponse(content="The stock you requested was not saved in our app!", status_code=404)