import yfinance
import openpyxl


tiker = yfinance.Ticker("PFE")
history = ticker.history("3y")

history.to_excel("yfinance.xls")