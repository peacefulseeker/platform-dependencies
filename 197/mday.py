from datetime import date, timedelta

DAYS_IN_A_WEEK = 7

def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    first_may = date(year, 5, 1)
    year, week, weekday = first_may.isocalendar()
    days_timedelta = (DAYS_IN_A_WEEK - weekday) + DAYS_IN_A_WEEK
    mothers_day_date = first_may + timedelta(days=days_timedelta)

    return mothers_day_date


print(get_mothers_day_date(2016))
