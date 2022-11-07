from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy import text

print("hello")
connection_string = "Driver={SQL Server};Server=TSSPDDWSQLD01;Database=TSSPEDW;Trusted_Connection=yes;"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
with engine.connect() as connection:
    result = connection.execute(text("select count(*) from legalentity"))
    row = result.fetchone()
    print(row)
print("goodbye")