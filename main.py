import pandas as pd

# Load datasets
f_path1 = r'C:\Users\saani\Downloads\problem\purchase_behaviour.csv' #change this with the path to the file
f_path2 = r'C:\Users\saani\Downloads\problem\transaction_data.csv' #change this with the path to the file
purchase_data = pd.read_csv(f_path1)
transaction_data = pd.read_csv(f_path2)
# Identify top 3 most profitable products
top_products = (
    transaction_data.groupby(["PROD_NBR", "PROD_NAME"])["TOT_SALES"]
    .sum()
    .reset_index()
    .sort_values(by="TOT_SALES", ascending=False)
    .head(3)
)

# Identify most loyal customers (by number of transactions)
loyal_customers = (
    transaction_data.groupby("LYLTY_CARD_NBR")["TXN_ID"]
    .count()
    .reset_index()
    .rename(columns={"TXN_ID": "PURCHASE_COUNT"})
    .sort_values(by="PURCHASE_COUNT", ascending=False)
)

# Merge with purchase behavior data
loyal_customers = loyal_customers.merge(purchase_data, on="LYLTY_CARD_NBR")

# Find the dominant life stage and premium segment of loyal customers
loyal_segments = (
    loyal_customers.groupby(["LIFESTAGE", "PREMIUM_CUSTOMER"])["PURCHASE_COUNT"]
    .sum()
    .reset_index()
    .sort_values(by="PURCHASE_COUNT", ascending=False)
    .head(3)
)

# Display results
print("Top 3 Most Profitable Products:")
print(top_products)
print("\nMost Loyal Customer Segments:")
print(loyal_segments)
