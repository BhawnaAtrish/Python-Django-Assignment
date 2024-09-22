import pandas as pd
import re

# Function to validate email addresses
# Return True if the email matches the pattern, else False
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Read the CSV file
input_file = 'user_data.csv'
output_file = 'cleaned_user_data.csv'

# Load the CSV into a pandas DataFrame
df = pd.read_csv(input_file)

# Remove duplicate entries based on 'user_id'
df_cleaned = df.drop_duplicates(subset='user_id')

# Filter out rows with invalid email formats
df_cleaned = df_cleaned[df_cleaned['email'].apply(is_valid_email)]

# Write the cleaned data to a new CSV file
df_cleaned.to_csv(output_file, index=False)

print(f"Cleaned data has been written to {output_file}")
