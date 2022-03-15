import yfinance

tsla = yfinance.Ticker("TSLA")


dataframe = tsla.history("1y")
# print(dataframe)
dataframe.reset_index()

format_df = []
for d in dataframe["Close"]:
    print(d)

from plotly import graph_objects
scatter = graph_objects.Scatter(x=dataframe.index, y=dataframe["Close"])
diagram = graph_objects.Figure([scatter])
diagram.show()


dataframe2 = tsla.financials
dataframe2.reset_index()
scatter2 = graph_objects.Scatter(x=dataframe2.index, y=dataframe2["2021-12-31"])
diagram2 = graph_objects.Figure([scatter2])
diagram2.show()

# dataframe = tsla.financials
# print(dataframe)
# dataframe = dataframe.drop("Total Revenue", axis=1).set_index("formatted_date")
# print(dataframe)