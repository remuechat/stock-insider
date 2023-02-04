print('What is the name of the Wiki Article?')
article = str(input())
Year = 2023
Month = 2
Day = 1

import requests
from datetime import datetime, timedelta

def get_daily_prices(symbol, start_date, end_date):
    daily_prices = {}
    date = start_date
    while date <= end_date:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&datatype=csv&start_date={start_date}&end_date={end_date}"
        response = requests.get(url)
        data = response.text.strip().split("\n")
        headers = data[0].split(",")
        for i in range(1, len(data)):
            values = data[i].split(",")
            date_str = values[0]
            price = float(values[4])
            daily_prices[date_str] = price
        date += timedelta(days=1)
    return daily_prices

symbol = "AAPL" # Replace with the symbol of the stock you want to retrieve data for
start_date = datetime(2020, 1, 1) # Replace with the start date for the range you want to retrieve data for
end_date = datetime(2020, 12, 31) # Replace with the end date for the range you want to retrieve data for
api_key = "YOUR_API_KEY" # Replace with your Alpha Vantage API key

daily_prices = get_daily_prices(symbol, start_date, end_date)
print(daily_prices)
