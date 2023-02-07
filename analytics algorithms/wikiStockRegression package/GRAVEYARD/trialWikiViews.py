import requests
import json
from datetime import datetime

#thisisjusttemporary
print('What is the name of the Wiki Article?')
article = str(input())
Year = 2023
Month = 2
Day = 1


def get_views_per_day(start_date, end_date):
    params = {
        'action': 'query',
        'format': 'json',
        'titles': article,
        'prop': 'pageviews',
        'pvip': '2023-02-01',
        'pvdir': 'older',
        'pvstart': start_date.strftime('%Y-%m-%dT00:00:00Z'),
        'pvend': end_date.strftime('%Y-%m-%dT00:00:00Z')
    }
    response = requests.get('https://en.wikipedia.org/w/api.php', params=params)
    #add error handling in case API doesn't return data
    data = response.json()
    pageviews = data['query']['pages'].popitem()[1]['pageviews']
    views_per_day = {}
    for date, views in pageviews.items():
        date = datetime.strptime(date, '%Y-%m-%d').date()
        views_per_day[date.strftime('%Y-%m-%d')] = views
    return views_per_day

start_date = datetime(Year, Month, Day)
print(start_date)
#edit this later, user should be able to input the date
end_date = datetime.now()
print(end_date)

views_per_day = get_views_per_day(start_date, end_date)

with open(f'{article}_views_per_day.json', 'w') as file:
    file.write(json.dumps(views_per_day, indent=4))
