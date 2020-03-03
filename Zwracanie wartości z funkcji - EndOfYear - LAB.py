from datetime import date
from datetime import timedelta


def ToEndYear(year = date.today().year,month = date.today().month,day = date.today().day):
    today = date(year,month,day)
    EndOfYear = date(year,12,31)
    DaysToEndYear = EndOfYear - today
     
    return DaysToEndYear.days


print(ToEndYear())
print(ToEndYear(2020,2,28))

zmienna = ToEndYear(2020,5,31)
print(zmienna)
