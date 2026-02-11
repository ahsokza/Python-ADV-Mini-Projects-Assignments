pip install seaborn

#Full name:Khaled Kanaan Albreiki
#Emirates ID number: 
#School ID: 302679


#import libararies
import pandas as pd
import numpy as np

#load datasets into datasframes 
flight_data = pd.read_csv('flight_data.csv')
passenger_data_1 = pd.read_csv('passenger_data_1.csv')
booking_data = pd.read_csv('booking_data.csv')

#display data 
flight_data.head ()
passenger_data_1.head()
booking_data.head() 

#Task 1 - Continued
import pandas as pd

# Assuming you have two DataFrames: flight_data and passenger_data
merged_data = pd.merge(flight_data, passenger_data, on='Flight number', how='inner')

# Display the merged data
print(merged_data)

#Task 1 -  Continued
import pandas as pd

# Assuming you have two DataFrames: flight_data and booking_data
merged_data = pd.merge(flight_data, booking_data, on='Flight number', how='left')

# Display the merged data
print(merged_data)

#task 1 - continued
import pandas as pd

# Assuming you have two DataFrames: flight_data and booking_data
merged_data = pd.merge(flight_data, booking_data, on='Flight number', how='left')

# Display the merged data
print(merged_data)

#task 1 - continued

import pandas as pd

# Assuming you have the merged DataFrame (from the left join) and passenger_data
final_merged_data = pd.merge(merged_data, passenger_data, on='Passenger ID', how='outer')

# Display the final merged data
print(final_merged_data)


#task 1 - continuted

import pandas as pd

# Assuming you have the merged DataFrame (from the left join) and passenger_data
final_merged_data = pd.merge(merged_data, passenger_data, on='Passenger ID', how='outer')

# Display the final merged data
print(final_merged_data)


import pandas as pd

# Assuming you have a DataFrame named passenger_data
# Identify duplicate rows
duplicate_rows = passenger_data[passenger_data.duplicated()]

# Remove duplicate rows
passenger_data_cleaned = passenger_data.drop_duplicates()

# Display the duplicates and the cleaned data
print("Duplicate Rows:\n", duplicate_rows)
print("\nCleaned Passenger Data:\n", passenger_data_cleaned)

#Full name:Khaled Kanaan Albreiki
#Emirates ID number: 
#School ID: 302679
#Task 1- Branch h


import pandas as pd

# Sample data
data = {
    'Flight status': ['On Time', 'Cancelled', 'Delayed', 'On Time', 'Cancelled']
}

# Create DataFrame
df = pd.DataFrame(data)

# Replace values in the 'Flight status' column
df['Flight status'] = df['Flight status'].replace({
    'On Time': 'On-time',
    'Cancelled': 'Canceled'
})

# Display the updated DataFrame
print(df)


import pandas as pd

# Sample data
data = {
    'Flight status': ['On Time', 'Cancelled', 'Delayed', 'On Time', 'Cancelled']
}

# Create DataFrame
df = pd.DataFrame(data)

# Replace values in the 'Flight status' column
df['Flight status'] = df['Flight status'].replace({
    'On Time': 'On-time',
    'Cancelled': 'Canceled'
})

# Display the updated DataFrame
print(df)


import pandas as pd

# Step 1: Import the dataset
df = pd.read_csv('passenger_data_1.csv')

# Step 2: Check for missing data
missing_data_count = df.isnull().sum()
print("Count of missing values in each column:")
print(missing_data_count)

# Step 3: Find and display rows where 'Age' has values
age_notnull_rows = df[df['Age'].notnull()]
print("\nRows where 'Age' has values:")
print(age_notnull_rows)



mport pandas as pd

# Step 1: Import the dataset
passenger_data = pd.read_csv('passenger_data_1.csv')

# Step 2: Use dropna() to remove rows with missing values
data_dropped = passenger_data.dropna()
print("Data after dropping rows with missing values:\n", data_dropped)

# Step 3: Use fillna(method='ffill') to forward fill missing values
data_forward_filled = passenger_data.fillna(method='ffill')
print("\nData after forward filling missing values:\n", data_forward_filled)

# Step 4: Use fillna(method='bfill') to backward fill missing values
data_backward_filled = passenger_data.fillna(method='bfill')
print("\nData after backward filling missing values:\n", data_backward_filled)

# Step 5: Use interpolate() to fill missing values using linear interpolation
data_interpolated = passenger_data.interpolate()
print("\nData after linear interpolation of missing values:\n", data_interpolated)










