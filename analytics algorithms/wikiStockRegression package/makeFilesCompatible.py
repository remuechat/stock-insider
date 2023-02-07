import json

article = str(input('What is the name of the company?'))

# Load JSON files into Python dictionaries
with open(f'{article}_wiki_views.json') as views_file:
    views = json.load(views_file)
    # Remove the last key-value pair from the filtered views dictionary
    last_key = list(views.keys())[-1]
    del views[last_key]

with open(f'{article}_perDayPrices.json') as prices_file:
    stock_prices = json.load(prices_file)

# Create a list of common keys between the two dictionaries
common_keys = list(set(views.keys()) & set(stock_prices.keys()))

# Filter the dictionaries to only include the common keys
filtered_views = {key: views[key] for key in common_keys}
filtered_prices = {key: stock_prices[key] for key in common_keys}
filtered_views = dict(sorted(filtered_views.items()))
filtered_prices = dict(sorted(filtered_prices.items()))

# Write the filtered dictionaries to new JSON files
with open(f'{article}_filtered_views.json', 'w') as filtered_views_file:
    json.dump(filtered_views, filtered_views_file)

with open(f'{article}_filtered_prices.json', 'w') as filtered_prices_file:
    json.dump(filtered_prices, filtered_prices_file)
