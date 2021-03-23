from datetime import date, timedelta

DAYS_IN_A_WEEK = 7

def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    first_may = date(year, 5, 1)
    year, week, weekday = first_may.isocalendar()
    return first_may + timedelta(days=(DAYS_IN_A_WEEK - weekday) + DAYS_IN_A_WEEK)


print(get_mothers_day_date(2016))
