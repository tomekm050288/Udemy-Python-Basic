from datetime import date
from datetime import timedelta


def DaysToEndOfYear(*dates):
    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)
    return


DaysToEndOfYear(date(1999,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15),date.today())
