import pandas as pd
from datetime import datetime

# Define the function to convert date formats
def convert_date_format(date_str):
    if pd.isna(date_str) or not date_str.strip():
        return date_str
    
    try:
        # Attempt to parse the date in mm/dd/yyyy format
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
        # Convert to yyyy-mm-dd format
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        # If parsing fails, return the original date string
        return date_str

# Load the CSV file
input_csv_file = 'bookData.csv'
df = pd.read_csv(input_csv_file)

# Print the DataFrame to verify the data
print("Original DataFrame:")
print(df.head())

# Convert the 'Publication Date' column
df['Publication Date'] = df['Publication Date'].apply(convert_date_format)

# Print the DataFrame to verify changes
print("\nUpdated DataFrame:")
print(df.head())

# Save the updated DataFrame to a new CSV file
output_csv_file = 'bookData_updated.csv'
df.to_csv(output_csv_file, index=False)

print(f"Updated CSV file saved as '{output_csv_file}'")
