# Imports for class functionality
import yfinance as yf
import pandas as pd

# Define a class for storing and accessing ticker data because the yahoo
# finance API is finnicky. 
class TickerClass:
    
    # Define class members
    ticker_symbol = ""
    stock_data = pd.DataFrame()
    
    # Constructor
    def __init__(self, ticker):
        self.ticker_symbol = ticker
        
    # Function to retreive data from yf api
    # Note that date needs to be in the following format: 'YYYY-MM-DD'
    def getData(self, start_date, end_date):
        
        # Download stock data from start_date to end_date
        self.stock_data = yf.download(self.ticker_symbol, start = start_date, 
                                 end = end_date)