import matplotlib.pyplot as plt
import json

#this is just temporary
print('What is the name of the Wiki Article?')
article = str(input())

def show_article(article):
    # Load the data from the file as a dictionary
    with open(f'{article}_views_per_day.json') as f:
        data = json.load(f)

    # Extract the dates and views into separate lists
    dates = list(data.keys())
    views = list(data.values())

    # Plot the data in a line plot
    plt.plot(dates, views)

    # Add labels and title
    plt.xlabel('Dates')
    plt.ylabel('Views')
    plt.title(f'{article} Views Over Time')

    # Show the plot
    plt.show()

show_article(article)


