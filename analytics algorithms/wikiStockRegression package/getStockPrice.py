import requests
import json
from datetime import datetime, timedelta

#PERMANENT: (unfinished)

def get_daily_prices(symbol, start_date, end_date):
    daily_prices = {}
    date = start_date
    while date <= end_date:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&datatype=csv&start_date={start_date}&end_date={end_date}"
        response = requests.get(url)
        #add error handling if the response is null
        data = response.text.strip().split("\n")
        headers = data[0].split(",")
        for i in range(1, len(data)):
            values = data[i].split(",")
            date_str = values[0]
            price = float(values[4])
            daily_prices[date_str] = price
        date += timedelta(days=1)
    return daily_prices

api_key = "6WQ39K46TPM7TSFO"
symbol = ""
# filler dates for the mean time, add user input later, add error handling
symbol = str(input('What is the name of the Stock?'))
date_format = "%Y-%m-%d"
start_date = datetime.strptime(input('What date will you want to start? (YYYY-MM-DD): '), date_format)
end_date = datetime.strptime(input('What date will you want to end? (YYYY-MM-DD): '), date_format)

perDayPrices = get_daily_prices(symbol, start_date, end_date)

#store in a JSON file
with open('perDayPrices.json', 'w') as fp:
    json.dump(perDayPrices, fp)