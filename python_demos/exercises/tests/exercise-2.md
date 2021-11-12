# Unit Testing - Exercise 2

## Requirements

Note: Please read all requirements before proceeding.

1. Under the `tests` folder, create a folder named `simple_rates_client`. Add an empty `__init__.py` file to the new folder.

2. Create a new file named `test_business_days.py`.

3. Write two unit tests (described below) for the `business_days` function (list version) in the `test_business_days.py` file.

4. The first test should pass in a start date that occurs before the end date. Verify the code works properly.

5. The second test should pass in a start date that occurs after the end date. Test that an exception is thrown. You may need to modify the `business_days` function for this test to pass.

6. Please mock the `holidays` package.

7. Using your editor, run the tests. Ensure they both pass.
