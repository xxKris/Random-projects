import yfinance as yf

# Get stock data for a specific ticker
ticker = "AAPL"
stock = yf.Ticker(ticker)
info = stock.info

# Print stock data
print("Current price:", info["regularMarketPrice"])
print("Day's range:", info["regularMarketDayRange"])
print("Volume:", info["regularMarketVolume"])
