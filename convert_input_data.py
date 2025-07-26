import pyreadr
import pandas as pd

# Path to the RData file
rdata_file = r"C:\Users\hood_\Dropbox\urban economics sp24\problem sets\problem set 1\r_submissions\berlin_36_86.RData"

# Path to save the Parquet file in the specified directory
parquet_file = "c:/urban_economics/agglomeration/berlin_36_86.parquet"

# Load the RData file
result = pyreadr.read_r(rdata_file)  # This returns a dictionary with dataframes

# Extract the first dataframe from the RData file
# Assuming the RData file contains only one dataframe
df = list(result.values())[0]

# Save the dataframe as a Parquet file
df.to_parquet(parquet_file)

print(f"Data successfully converted to {parquet_file}")