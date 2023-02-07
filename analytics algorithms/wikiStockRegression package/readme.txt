*WHAT DOES THESE FILES DO?*

> getWikiViews: uses the Wikipedia API to create a JSON of daily views in a range of time for a wiki page
> getStockPrice: uses AlphaVantage API to create a JSON of daily stock prices in a range of time for a specific stock
> makeFilesCompatible: makes both the getStockPrice and getWikiViews compatible in terms of date so they could be plotted
> wikiAgainstStock: contains a few functions that returns an image: 1) plotInLine - compatible stock price JSON to the wiki views JSON on a line graph; 2) plotInRegressionWiki - plots the stock against regression;   