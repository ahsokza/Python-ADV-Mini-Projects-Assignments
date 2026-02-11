##Task 2: Detecting and Removing Outliers in Flight Price Data Using a Custom Threshold and np.abs()

#Full name:Khaled Kanaan Albreiki
#Emirates ID number: 
#School ID: 302679
#Task 2- Branch a

#import numpy library

import numpy as np

#import flight_price_data.csv file into Dataframe

flight_Price_Data_DF = pd.read_csv("flight_price_data.csv")
#display the data

flight_Price_Data_DF.head()
#declare the threshold value

trs_v = 10000
# Detect outliens for 'Ticket Price' more than threshold value
outl= flight_Price_Data_DF[np.abs(flight_Price_Data_DF['Ticket Price']) >= trs_v]

#display the outlier values
print("Outlier values are =", outl)

#Task 2- Branch b

#remove the outlier values from dataset
clean_flight_price_df = flight_Price_Data_DF[~flight_Price_Data_DF.index.isin(outl.index)]

#display the clean dataset
clean_flight_price_df.head()


#Task 2- Branch d

#import flight_price_data.csv file into dataframe
fpd_df =pd.read_csv("flight_price_data.csv")

#display the dataframe
fpd_df.head()

#select columns Departure City and Arrival City from dataframe
city = ["Departure City","Arrival City"]

#creating duplicate variables for selected columns
fpd_duplicate = pd.get_dummies(fpd_df, columns=city)

# Display the updated DataFrame with duplicates
print("Flight Price Data with dupliacte values:")
print(fpd_duplicate.head())


