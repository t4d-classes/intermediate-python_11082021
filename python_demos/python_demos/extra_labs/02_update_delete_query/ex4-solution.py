""" rates query demo """

import pyodbc

conn_options = [
    "DRIVER={ODBC Driver 17 for SQL Server}",
    "SERVER=localhost,1433",
    "DATABASE=ratesapp",
    "UID=sa",
    "PWD=sqlDbp@ss!"
]


conn_string = ";".join(conn_options)

# print(conn_string)

def main() -> None:
    """ main """

    with pyodbc.connect(conn_string) as con:

        con.execute(
            " ".join([
                "update rates set closingdate = ?, currencysymbol = ?, exchangerate = ?",
                "where ratesid = ?"
            ]), ('2019-01-04', 'USD', 1.23, 3))

        con.execute(
            "delete from rates where ratesid = ?", (3,))


if __name__ == "__main__":
    main()