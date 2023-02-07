import datetime

#TEMPORARY: only for testing purposes
#RESULT: there's an error between datetime modules, and datetime.date modules
#        so wikiViews to JSON is different from filtering JSON to compare
#        with stock data

startDay, startMonth, startYear = [int(x) for x in input("Enter start date(DD/MM/YYYY) : ").split('/')]
temporaryStartDate = datetime.date(startYear, startMonth, startDay)
print(temporaryStartDate)

endDay, endMonth, endYear = [int(x) for x in input("Enter end date(DD/MM/YYYY) : ").split('/')]
temporaryEndDate = datetime.date(endYear, endMonth, endDay)
print(temporaryEndDate)

date_format = "%Y-%m-%d"
start_date = datetime.strptime(temporaryStartDate, date_format)
end_date = datetime.strptime(temporaryEndDate, date_format)
print(start_date)
print(end_date)


if start_date <= end_date:
    print("True")
else:
    print("False")
