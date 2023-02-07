import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# PERMANENT: Plots the data from the JSON file created by getWikiViews.py
#            against the stock data from the CSV file created by getStockData.py
#            to see if there is a correlation between the two, outputting a graph
#            of the data and correlation coefficient (NOTE: UNFINISHED)

tweets_normal = pd.read_csv(r'data/data.csv')
tweets_normal.date = pd.to_datetime(tweets_normal.date, format = '%Y-%m-%d')

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Bitcoin Price (US Dollar)', color=color)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=15))
plt.plot(tweets_normal.date,tweets_normal.price, color=color)
plt.gcf().autofmt_xdate()
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Bitcoin Tweet Sentiment', color=color)  # we already handled the x-label with ax1
ax2.plot(tweets_normal.date,tweets_normal.compound, color=color)
ax2.tick_params(axis='y', labelcolor=color)
plt.xticks(rotation=45)

plt.title('Bitcoin price vs Bitcoin Tweet Sentiment')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()