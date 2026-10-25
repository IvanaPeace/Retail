import pandas as pd

#file path 
file_path = "data/raw/Online Retail.xlsx"

#loading the large dataset
df = pd.read_excel(file_path)

# Create a separate copy for cleaning later.
df_clean = df.copy()

# column names 
print(df.columns)

# print the first five rows.
print("#######first five rows ####")
print(df.head())

# shapes shows how many rows and columns within the dataset.
print("####### Before cleaning check shape #####")
print(df.shape)

if df.shape[0] > 1000:
    print("large dataset detected!")

#checking the shape of the dataframe
print("####### information ######")
df.info()

# check how many records are missing. Can we safely remove those records, fill them, or do we need to retain them?
print("####### Missing values #######")
print(df.isnull().sum())

print("####### Missing value percentages #######")
missing_percentage = df.isnull().mean() * 100
print(missing_percentage)

# Are the missing CustomerIDs associated with particular transactions?
#Are they associated with certain countries?
#Are they associated with cancellations?
#Do they have other useful information that means we should retain them?

print("####### Missing CustomerID by country #######")
# new DataFrame containing only rows where CustomerID is missing.
#For those records with missing CustomerIDs, which countries appear most often?
missing_customer_id = df[df["CustomerID"].isnull()]
print(missing_customer_id["Country"].value_counts().head(10))

print("####cancellations#####")
# some invoiceNo's start with a "C" meaning they could be cancelled.
cancelled_missing_id = missing_customer_id[
    missing_customer_id["InvoiceNo"].astype(str).str.startswith("C")
]

# total missing Customer ID's
print("Missing CustomerID records:", len(missing_customer_id))
# missing customer ID's with invoices numbers starting with C
print("Cancelled records with missing CustomerID:", len(cancelled_missing_id))

print("####### Examples of missing CustomerID records #######")
print(missing_customer_id.head(10))

print("####### Duplicate records #######")
duplicate_count = df.duplicated().sum()
print("Number of duplicate rows:", duplicate_count)

print("####### Example duplicate records #######")
duplicates = df[df.duplicated(keep=False)]
print(duplicates.head(20))
# Are they actually duplicate transactions, or could the same transaction legitimately appear more than once?

print("####### Quantity checks #######")
#some quanitites are larger than others.
print("Negative quantities:", (df["Quantity"] < 0).sum())
print("Zero quantities:", (df["Quantity"] == 0).sum())

print("####### Negative quantity investigation #######")
negative_quantity = df[df["Quantity"] < 0]
cancelled_negative_quantity = negative_quantity[
    negative_quantity["InvoiceNo"].astype(str).str.startswith("C")
]
print(negative_quantity.head(10))
print("Negative quantity records:", len(negative_quantity))
print("Negative quantity records with C invoice:", len(cancelled_negative_quantity))


print("###############negative records not cancelled ############")
# Give me the negative records where the invoice number doesn't start with C.
non_cancelled_negative = negative_quantity[
    ~negative_quantity["InvoiceNo"].astype(str).str.startswith("C")
]

print("Negative quantity records without C invoice:", len(non_cancelled_negative))
print("####### Examples #######")
print(non_cancelled_negative.head(20))

print("####### Zero price investigation #######")
zero_price = df[df["UnitPrice"] == 0]
print("Zero price records:", len(zero_price))
negative_zero_price = zero_price[zero_price["Quantity"] < 0]
print("Zero price records with negative quantity:", len(negative_zero_price))

print("####### Examples of zero price negative quantities #######")
print(negative_zero_price.head(20))


print("####### Zero price positive quantity investigation #######")
zero_price_positive = zero_price[zero_price["Quantity"] > 0]
print("Zero price records with positive quantity:", len(zero_price_positive))
print("####### Examples #######")
print(zero_price_positive.head(20))

print("####### Zero price customer investigation #######")
zero_price_with_customer = zero_price["CustomerID"].notna().sum()
zero_price_without_customer = zero_price["CustomerID"].isna().sum()
print("Zero price records with CustomerID:", zero_price_with_customer)
print("Zero price records without CustomerID:", zero_price_without_customer)

zero_price_with_description = zero_price["Description"].notna().sum()
zero_price_without_description = zero_price["Description"].isna().sum()
print("Zero price records with Description:", zero_price_with_description)
print("Zero price records without Description:", zero_price_without_description)



####### cleaning ########
print("####### Cleaning duplicates #######")

#df.clean was declared at the start of the 
before_duplicates = len(df_clean)

df_clean = df_clean.drop_duplicates()

# look at data types again
df_clean.info()

# Convert the text columns from 'object' to the official 'string' type
text_cols = ['InvoiceNo', 'StockCode', 'Description']
df_clean[text_cols] = df[text_cols].astype('string')

# Convert CustomerID to a nullable integer from float64.
df_clean['CustomerID'] = df['CustomerID'].astype('Int64')

# validation check to see that the data types have changed.
df_clean.info()

#No need to change the quantity to Int64 datatype due to not having any null values.

after_duplicates = len(df_clean)

print("Rows before removing duplicates:", before_duplicates)
print("Rows after removing duplicates:", after_duplicates)
print("Duplicate rows removed:", before_duplicates - after_duplicates)

print("####### Duplicate validation #######")
print("Remaining duplicate rows:", df_clean.duplicated().sum()) # validate the change 

######################################
print("####### Unit price checks #######")

negative_prices = (df_clean["UnitPrice"] < 0).sum()

print("Negative unit prices:", negative_prices)

######################################
print("####### Date checks #######")
print("Missing InvoiceDate:", df_clean["InvoiceDate"].isna().sum())
print("Earliest InvoiceDate:", df_clean["InvoiceDate"].min())
print("Latest InvoiceDate:", df_clean["InvoiceDate"].max())

#I've identified several data-quality issues. I've investigated them and distinguished between genuine anomalies 
# and values that may have legitimate business meaning. I've removed exact duplicates, while retaining records such as
# returns and missing customer information because there isn't sufficient evidence that they're invalid.

print("original dataset rows: ", df.shape)

# Save cleaned dataset
output_path = "data/processed/Online Retail_cleaned.xlsx"

df_clean.to_excel(output_path, index=False) # index=false prevents pandas from adding the dataframes row numbers as an extra column in excel.

print("Cleaned dataset saved to:", output_path)

saved_file_path = "data/processed/Online Retail_cleaned.xlsx"

#loading the large dataset
df_validation = pd.read_excel(saved_file_path)

print("saved file dataset rows: ", df_validation.shape)
