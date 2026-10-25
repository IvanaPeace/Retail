import sqlite3

database_path = "data/online_retail.db"

connection = sqlite3.connect(database_path)

# select the number of rows from the transactions table. Like len(df) in pandas.
#query = """
#SELECT COUNT(*)
#FROM transactions;
#"""

# select all columns and show 10 records from the transactions table.
#query = """
#SELECT *
#FROM transactions
#LIMIT 10;
#"""

#select all columns where quantity is negative and show 10 records. similar to pandas comaparison "df[df["Quantity"] < 0]"
query = """
SELECT *
FROM transactions
WHERE Quantity < 0
LIMIT 10;
"""

#select COUNT of all columns where quantity is negative"
query = """
SELECT COUNT(*)
FROM transactions
WHERE Quantity < 0
"""

# how many negative invoices have an invoice number beginning with a C
query = """
SELECT COUNT(*)
FROM transactions
WHERE Quantity < 0
AND InvoiceNo LIKE 'C%';
"""

# Update query
#query = """ 
#UPDATE transactions
#SET Description = 'Correct descriptions'
#WHERE StockCode = '85123A';  
#"""

# insert query (add a new record)
#query = """ 
#INSERT INTO customers (CustomerID, Country)
#VALUES (20000, 'United Kingdom')
#"""

#DELETE 
#query = """ 
#DELETE FROM transactions
#WHERE InvoiceNo = '123456'; # without the WHERE the query would remove every row from the table.
#"""

#ALTER 
##query = """ 
#ALTER TABLE transactions
#ADD COLUMN TotalValue REAL;
#"""

# if you wanted to populate the the new column.
##query = """ 
#UPDATE transactions
#SET TotalValue = Quantity * UnitPrice;
#"""

# run the sql query against the database.
result = connection.execute(query)

# only retrieves one row
print(result.fetchone())

# if a query wants more than one row use 
#print(result.fetchall())

#
connection.close()