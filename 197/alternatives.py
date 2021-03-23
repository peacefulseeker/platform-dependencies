from datetime import date

from dateutil.relativedelta import relativedelta, SU

MAY = 5

# Elegant, though another import
def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    first_of_may = date(year=year, month=MAY, day=1)
    return first_of_may + relativedelta(weeks=1, weekday=SU)
