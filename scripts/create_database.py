import pandas as pd 
import sqlite3

# file path to the cleaned excel file.
file_path = "data/processed/Online Retail_cleaned.xlsx"

#read the excel file.
df = pd.read_excel(file_path)

# where the database file will live.
database_path = "data/online_retail.db"

# opens connection to the database.
connection = sqlite3.connect(database_path)

#take the dataframe and put it into a SQL table called "transactions". "replace" will replace the table if the script is run again.
df.to_sql("transactions", connection, if_exists="replace", index=False) # flase means Don't put pandas' row index into the database.

print("Database created successfully.")
print("Rows in database:", len(df))

connection.close()






