import pandas as pd

# Load the CSV files
paynt_df = pd.read_csv('./logs/paynt-final.csv')
dtcontrol_df = pd.read_csv('./logs/dtcontrol-final.csv')
omdt_df = pd.read_csv('./logs/omdt-final.csv')

# Merge the dataframes based on the "model" column
merged_df = pd.merge(paynt_df, dtcontrol_df, on='model', how='inner')
# Convert "dtcontrol nodes" to integers
merged_df['dtcontrol nodes'] = merged_df['dtcontrol nodes'].astype(int)

merged_df['model'] = merged_df['model'].str.replace('^omdt-|^qcomp-', '', regex=True)

# Merge the merged_df with omdt_df based on "model" and "max_depth" columns
merged_df = pd.merge(merged_df, omdt_df, on=['model', 'max_depth'], how='inner')

# Save the merged dataframe to a new CSV file
merged_df.to_csv('./logs/final-merge.csv', index=False)
