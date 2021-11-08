""" main module """

from datetime import date

from .business_days import business_days


def main() -> None:
    """ main """

    start_date = date(2019, 1, 3)
    end_date = date(2019, 1, 23)

    for the_date in business_days(start_date, end_date):
        print(the_date)


if __name__ == "__main__":
    main()
