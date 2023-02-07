import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def plotSingleJSON(article, label, color='b'):
    with open(f'{article}_filtered_prices.json') as f:
        data = json.load(f)

    dates = list(data.keys())
    #multiple values will should probably be replaced, like inputting multiple json files
    values = list(data.values())

    plt.plot(dates, values, color=color, label=label)
    plt.xticks(rotation=90)
    plt.xlabel('Date')
    plt.ylabel(label)
    plt.legend()
    plt.show()

def plotMultipleJSON(article, label, color='b'):
    with open(f'{article}_filtered_prices.json') as f:
        data = json.load(f)

    dates = list(data.keys())
    #multiple values will should probably be replaced, like inputting multiple json files
    values = list(data.values())

    plt.plot(dates, values, color=color, label=label)
    plt.xticks(rotation=90)
    plt.xlabel('Date')
    plt.ylabel(label)
    plt.legend()
    plt.show()

def plotPriceAgainstViewsJSON(article):
    with open(f'{article}_filtered_prices.json') as f:
        pricesJSON = json.load(f)

    with open(f'{article}_filtered_views.json') as f:
        viewsJSON = json.load(f)

    x = list(viewsJSON.keys())
    views = list(viewsJSON.values())
    prices = list(pricesJSON.values())

    # Initialize the figure and axis
    fig, ax1 = plt.subplots(figsize=(10, 6), dpi=100)

    # Plot y1 on the left y-axis
    ax1.plot(x, views, color='b', label='')
    ax1.set_xlabel('Dates')
    plt.xticks(rotation=45)
    ax1.set_ylabel('Views', color='g')
    ax1.tick_params(axis='y', labelcolor='b')

    # Create a second y-axis on the right with a different scale
    ax2 = ax1.twinx()
    ax2.plot(x, prices, color='g', label='')
    ax2.set_ylabel('Prices', color='k')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.title(f'{article} Stock Prices vs Wikipedia Views')
    plt.legend()
    plt.show()

def plotJSONwithTrendline(article):
    with open(f'{article}_filtered_prices.json') as f:
        pricesJSON = json.load(f)

    with open(f'{article}_filtered_views.json') as f:
        viewsJSON = json.load(f)

    views = list(viewsJSON.values())
    prices = list(pricesJSON.values())

    viewsReg = np.array(views).reshape((-1, 1))
    pricesReg = np.array(prices)
    model = LinearRegression().fit(viewsReg, pricesReg)
    r_sq = model.score(viewsReg, pricesReg)
    print(f"coefficient of determination: {r_sq}")

    data = {'views': views,
            'stocks': prices}

    df = pd.DataFrame(data)

    # Plot the data and fit a regression line
    sns.regplot(x='views', y='stocks', data=df)


    plt.title(f'{article} Regression of Stock Prices vs Wikipedia Views')
    plt.show()

plotJSONwithTrendline('Apple Inc.')
