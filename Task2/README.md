# CSV Email Validator and Data Cleaner - README

## Overview

This Python script performs data cleaning on a CSV file containing user data. It reads the data, removes duplicate entries based on a unique `user_id` column, validates email addresses using a regex pattern, and writes the cleaned data to a new CSV file.

## Features

- **Duplicate Removal**: Eliminates duplicate entries based on the `user_id` column.
- **Email Validation**: Ensures that all email addresses are valid by matching them against a predefined regular expression (regex).
- **CSV Processing**: Uses `pandas` for efficient CSV file handling and manipulation.
- **File Output**: Saves the cleaned data to a new CSV file, free of duplicates and invalid email addresses.

## Requirements

Before running the script, make sure the following dependencies are installed:

- **Python 3.x**
- **pandas** library
- **re** module (for regex matching)

You can install `pandas` via pip if it's not already installed:

```bash
pip install pandas
```

## Files Used

- **Input File**: The script reads from a CSV file (`user_data.csv`) containing user information.
- **Output File**: After cleaning, the cleaned data is written to a new CSV file (`cleaned_user_data.csv`).

## Script Description

### 1. **Email Validation Function**

The function `is_valid_email(email)` checks if an email address matches the required format using a regex pattern.

- **Input**: A string representing the email address.
- **Output**: Returns `True` if the email is valid, otherwise `False`.

```python
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None
```

### 2. **Loading and Cleaning the Data**

The script reads the input CSV file (`user_data.csv`) into a pandas DataFrame. It performs the following steps:

- **Remove Duplicates**: Entries with duplicate `user_id` values are removed using the `drop_duplicates()` function.
  
```python
df_cleaned = df.drop_duplicates(subset='user_id')
```

- **Validate Emails**: The script filters out rows where the `email` column contains invalid email addresses.

```python
df_cleaned = df_cleaned[df_cleaned['email'].apply(is_valid_email)]
```

### 3. **Saving the Cleaned Data**

The cleaned data is written to a new CSV file (`cleaned_user_data.csv`) using `to_csv()`, excluding the index column.

```python
df_cleaned.to_csv(output_file, index=False)
```

### 4. **Output**

A message is printed to indicate that the cleaned data has been saved.

```python
print(f"Cleaned data has been written to {output_file}")
```

## Usage Instructions

1. **Place the CSV file**: Ensure the input CSV file (`user_data.csv`) is in the same directory as the script, or modify the `input_file` path accordingly.
   
2. **Run the Script**:
   
```bash
python script_name.py
```

3. **Check Output**: After execution, the cleaned CSV file will be saved as `cleaned_user_data.csv`.

## Example

### Input CSV (`user_data.csv`):

| user_id | email              |
|---------|--------------------|
| 1       | validemail@domain.com |
| 2       | invalidemail@domain |
| 3       | valid2@domain.com   |
| 1       | duplicate@domain.com |

### Output CSV (`cleaned_user_data.csv`):

| user_id | email               |
|---------|---------------------|
| 1       | validemail@domain.com |
| 3       | valid2@domain.com    |


