import pandas as pd

# File path
csv_file_path = "#######"#your csv path

# Read CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Filling Empty values
df['Description'].fillna('No Description Provided', inplace=True)
df['House_rules'].fillna('No House rules Provided', inplace=True)
df['Amenities'].fillna('Not Available', inplace=True)
df['Name'].fillna('No Name  Provided', inplace=True)
df.Total_bedrooms.fillna(df.Total_bedrooms.mode()[0],inplace=True)
df.Total_beds.fillna(df.Total_beds.median(),inplace=True)
df.Security_deposit.fillna(df.Security_deposit.median(),inplace=True)
df.Cleaning_fee.fillna(df.Cleaning_fee.median(),inplace=True)
df.Review_scores.fillna(df.Review_scores.median(),inplace=True)

# Save the updated DataFrame to a new CSV file
updated_csv_file_path = "#######"#your csv path
df.to_csv(updated_csv_file_path, index=False)

print(f"Empty values filled and updated CSV file saved at: {updated_csv_file_path}")
