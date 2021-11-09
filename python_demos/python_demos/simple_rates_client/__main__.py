""" main module """

from datetime import date, timedelta
import requests

from .business_days import business_days
from .rates_api_server import rates_api_server


def main() -> None:
    """ main """

    with rates_api_server():

        start_date = date(2019, 1, 3)
        end_date = start_date + timedelta(days=20)

        rate_responses: list[str] = []

        for business_day in business_days(start_date, end_date):

            rate_url = "".join([
                "http://127.0.0.1:5000/api/",
                str(business_day),
                "?base=USD&symbols=EUR"
            ])

            response = requests.get(rate_url)

            rate_responses.append(response.text)

        print("\n".join(rate_responses))


if __name__ == "__main__":
    main()
