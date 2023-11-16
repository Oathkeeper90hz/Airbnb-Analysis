import pandas as pd
import json
from pathlib import Path

# File paths
json_file_path = "#######"#your json path
csv_output_folder = "#######"#your csv path

# Read JSON file into a DataFrame
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Extract and clean the specified data
cleaned_data = []
for i in data:
    cleaned_data.append({
        "Id": i['_id'],
        "Listing_url": i['listing_url'],
        "Name": i.get('name'),
        "Description": i['description'],
        "House_rules": i.get('house_rules'),
        "Property_type": i['property_type'],
        "Room_type": i['room_type'],
        "Bed_type": i['bed_type'],
        "Min_nights": int(i['minimum_nights']),
        "Max_nights": int(i['maximum_nights']),
        "Cancellation_policy": i['cancellation_policy'],
        "Accomodates": i['accommodates'],
        "Total_bedrooms": i.get('bedrooms'),
        "Total_beds": i.get('beds'),
        "Availability_365": i['availability']['availability_365'],
        "Price": i['price'],
        "Security_deposit": i.get('security_deposit'),
        "Cleaning_fee": i.get('cleaning_fee'),
        "Extra_people": i['extra_people'],
        "Guests_included": i['guests_included'],
        "No_of_reviews": i['number_of_reviews'],
        "Review_scores": i['review_scores'].get('review_scores_rating'),
        "Amenities": ', '.join(i['amenities']),
        "Host_id": i['host']['host_id'],
        "Host_name": i['host']['host_name'],
        "Street": i['address']['street'],
        "Country": i['address']['country'],
        "Country_code": i['address']['country_code'],
        "Location_type": i['address']['location']['type'],
        "Longitude": i['address']['location']['coordinates'][0],
        "Latitude": i['address']['location']['coordinates'][1],
        "Is_location_exact": i['address']['location']['is_location_exact']
    })

# Create a DataFrame from the cleaned data
df = pd.DataFrame(cleaned_data)

# Create the output folder if it doesn't exist
Path(csv_output_folder).mkdir(parents=True, exist_ok=True)

# Define the output CSV file path
csv_output_file = Path(csv_output_folder) / f"{Path(json_file_path).stem}_cleaned.csv"

# Convert DataFrame to CSV
df.to_csv(csv_output_file, index=False)

print(f"Cleaning and conversion successful. Cleaned CSV file saved at: {csv_output_file}")
