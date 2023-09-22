from datetime import datetime

def GET_TODAY():
    Today_Day = datetime.today()
    year = Today_Day.year
    month = Today_Day.month
    day = Today_Day.day
    return (day, month, year)