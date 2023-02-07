import datetime

startDay, startMonth, startYear = [int(x) for x in input("Enter start date(DD/MM/YYYY) : ").split('/')]
temporaryStartDate = datetime.date(startYear, startMonth, startDay)
print(temporaryStartDate)

endDay, endMonth, endYear = [int(x) for x in input("Enter end date(DD/MM/YYYY) : ").split('/')]
temporaryEndDate = datetime.date(endYear, endMonth, endDay)
print(temporaryEndDate)