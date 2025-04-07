import yfinance as yf
import pandas as pd

ticker_names = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "AMZN": "Amazon.com, Inc.",
    "SHOP": "Shopify Inc.",
    "JPM": "JPMorgan Chase & Co.",
    "BAC": "Bank of America Corporation",
    "XOM": "Exxon Mobil Corporation",
    "CVX": "Chevron Corporation",
    "JNJ": "Johnson & Johnson",
    "PFE": "Pfizer Inc.",
    "NEM": "Newmont Corporation",
    "WPM": "Wheaton Precious Metals Corp.",
    "BHP": "BHP Group Limited",
    "BA": "The Boeing Company",
    "LMT": "Lockheed Martin Corporation",
    "TSLA": "Tesla, Inc.",
    "F": "Ford Motor Company",
    "GLD": "SPDR Gold Trust",
    "SLV": "iShares Silver Trust",
    "BTC-USD": "Bitcoin",
    "ETH-USD": "Ethereum",
    "SOL-USD": "Solana",
    "BNB-USD": "Binance Coin",
    "ADA-USD": "Cardano"
}
data = {}
period = '5y'
interval = '1d'
for ticker in ticker_names.keys():
    df = yf.download(ticker, period=period, interval=interval)
    # Reset index existing columns
    df = df.reset_index()
    # Check if column names are nested/multi-index (fix it)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # select required columns & save
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    df.to_csv(f"../../data/raw/{ticker}_{period}_{interval}.csv", index=False)

print("Data downloaded successfully!")
