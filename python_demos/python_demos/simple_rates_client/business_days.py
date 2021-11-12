""" business days module """

from collections.abc import Generator
from datetime import date, timedelta
import holidays


def business_days(
        start_date: date, end_date: date) -> Generator[date, None, None]:
    """ business days """

    us_holidays = holidays.UnitedStates()
    date_delta = end_date - start_date
    num_of_days = date_delta.days + 1

    for day in range(num_of_days):
        the_date = start_date + timedelta(day)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            yield the_date

class EndBeforeStartException(Exception):
    pass


def business_days_list(start_date: date, end_date: date) -> list[date]:
    """ business days """

    if (end_date <= start_date):
        raise EndBeforeStartException()

    us_holidays = holidays.UnitedStates()
    days: list[date] = []
    date_delta = end_date - start_date
    num_of_days = date_delta.days + 1

    for day in range(num_of_days):
        the_date = start_date + timedelta(day)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            days.append(the_date)

    return days