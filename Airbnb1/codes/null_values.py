import pandas as pd

# File path
csv_file_path = "#######"#your csv path

# Read CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the count of null values for each column
null_counts = df.isnull().sum()
print("Null values in each column:")
print(null_counts)


# Name                      8
# Total_bedrooms            5
# Total_beds               13
# Security_deposit       2084
# Cleaning_fee           1531
# Review_scores          1474

