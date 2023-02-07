import requests
import json
from datetime import datetime

# PERMANANENT: Takes data from Wiki API to create a JSON file
#              of views per day for a given article
#        NOTE: To make this work, you need to install the requests module
#              as well as use the compatible datetime.datetime module for]
#              the start and end dates

def get_views_per_day(article, start_date, end_date):
    params = {
        'action': 'query',
        'format': 'json',
        'titles': article,
        'prop': 'pageviews',
        'pvdir': 'older',
        'pvstart': start_date.strftime('%Y-%m-%dT00:00:00Z'),
        'pvend': end_date.strftime('%Y-%m-%dT00:00:00Z')
    }
    try:
        response = requests.get('https://en.wikipedia.org/w/api.php', params=params)
        response.raise_for_status()
        data = response.json()
        pageviews = data['query']['pages'].popitem()[1]['pageviews']
        views_per_day = {}
        for date, views in pageviews.items():
            date = datetime.strptime(date, '%Y-%m-%d').date()
            views_per_day[date.strftime('%Y-%m-%d')] = views
        return views_per_day
    except requests.exceptions.RequestException as e:
        print("There was an error with the API request: ", e)
        return None


def filter_views_per_day(views_per_day, start, end, datetime_object=None):
    filtered_views = {}
    # start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    start_date = datetime_object.date(start_date)
    end_date = datetime_object.date(end_date)
    # end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    for date, views in views_per_day.items():
        # date = datetime.strptime(date, '%Y-%m-%d').date()
        if start_date <= date <= end_date:
            filtered_views[date.strftime('%Y-%m-%d')] = views
    return filtered_views


print("What is the name of the Wiki Article?")
searchArticle = str(input())

date_format = "%Y-%m-%d"
start_date = datetime.strptime(input('What date will you want to start? (YYYY-MM-DD): '), date_format)
end_date = datetime.strptime(input('What date will you want to end? (YYYY-MM-DD): '), date_format)

views_per_day = get_views_per_day(searchArticle, start_date, end_date)

with open(f'{searchArticle}_wiki_views.json', 'w') as file:
    file.write(json.dumps(views_per_day, indent=4))
