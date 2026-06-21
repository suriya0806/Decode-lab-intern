import pandas as pd

# Load dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

print("===== DATA CLEANING REPORT =====")

# 1. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Fill Missing Values in CouponCode
if 'CouponCode' in df.columns:
    df['CouponCode'] = df['CouponCode'].fillna('No Coupon')

# 3. Check Duplicate Rows
duplicate_rows = df.duplicated().sum()
print("\nDuplicate Rows:", duplicate_rows)

# Remove duplicate rows
df = df.drop_duplicates()

# 4. Check Duplicate Order IDs
if 'OrderID' in df.columns:
    duplicate_ids = df['OrderID'].duplicated().sum()
    print("Duplicate Order IDs:", duplicate_ids)

# 5. Convert Date Column to Proper Format
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    invalid_dates = df['Date'].isnull().sum()
    print("Invalid Dates:", invalid_dates)

# 6. Dataset Information
print("\nDataset Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

# 7. Save Cleaned Dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned dataset saved as 'Cleaned_Dataset.xlsx'")
