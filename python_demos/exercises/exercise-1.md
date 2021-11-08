# Exercise 1

1. Create a new folder in the `python_demos` folder named `simple_rates_client`.

2. Create a new Python file named `business_days.py` in the `simple_rates_client` folder. Create a function in the `business_days.py` file named `business_days`. Call the `business_days` function from the `__main__.py` file in the `simple_rates_client` folder.

3. The `business_days` function returns the business days between a start date and an end date. The date range should be inclusive of the start and end date. You can do this by producing a list or you may use a generator

4. A business day is defined as any date that is not a weekend or a US holiday. Explore the `holidays` package on PyPi.org to figure out how to determine US holidays.

5. Using the `business_days` function display a listing of all business days between the start and end date in the console. Please display one date per line.