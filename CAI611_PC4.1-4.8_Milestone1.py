#Import Seaborn Library Functions for Scatterplot
import seaborn as sns

#build scatter plot for continous variables Quantity Sold and Unit Price
plt.figure(figsize=(12,7))
sns.scatterplot(x='Quantity_Sold',y='Unit_Price',data=mydf, color='Red', marker='X')
plt.title('Quantity sold vs unit price')
plt.grid

#display scatter plot
plt.show()

#Task 2:Analysis and Visualization Using the Medical Analysis Dataset¶

#aggregate data by using sum function for Total_Sales and groupby Product_Category
Product_Sales = mydf.groupby('Product_Category') ['Total_Sales'].sum()

#make pie chart
plt.figure(figsize=(8,8))
plt.pie(Product_Sales, labels=Product_Sales.index, autopct='%1.1f%%',
colors=['Purple', 'Yellow', 'Green', 'Pink'], startangle=140)

#title for the pie chart
plt.title('Catehory wise Total Sales')
#display the pie chart
plt.show()

#task read read dtat form medical analysis dataset into dataframe

mydf = pd.read_csv('medical_analysis_dataset.csv')
print(mydf)

#make a bar plot for  (Hospital) vs (Patient_Count)
medical = dfMAD.groupby('Hospital')['Patient_Count'].sum()
fig, ax = plt.subplots(figsize=(12,7))

#build a bar plot 
plt.bar(medical.index, medical.values, color=['Red','Green','Blue','Grey','Purple'])

#title of the plot
plt.title('Hospital Vs Patient_Count')

#labeling the axis
plt.xlabel('Hospital')
plt.ylabel('Patient_Count')

#add grid 
plt.grid(axis = 'y')


#Adding a table below the bar chart 
medical_data = pd.DataFrame(medical).reset_index()
medical_data.columns = ['Hospital', 'Patient_Count']

#plotting the table with more space between the chart and table 
ax.table(cellText=medical_data.values, colLabels=medical_data.columns, cellLoc='center', loc='bottom', bbox=[0, -0.6, 1, 0.3])
#display the plot 
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

# Define the continuous variable and the categorical variable
continuous_var = 'Recovery_Days'
categorical_var = 'Department'

# Create the histograms
plt.figure(figsize=(12, 8))
sns.histplot(data=mydf, x=continuous_var, hue=categorical_var, multiple="stack", kde=False)

# Adding titles and labels
plt.title('Distribution of Recovery Days by Department', fontsize=16)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Recovery Days', fontsize=12)


#Aggregate by groupby and sum functions

doctor_treatment_cost = mydf.groupby('Doctor_Name')['Treatment_Cost'].sum().sort_values()

#Create the lollipop chart
plt.figure(figsize=(12, 7))
plt.hlines(y=doctor_treatment_cost.index, xmin=0, xmax=doctor_treatment_cost.values, color='green')
plt.plot(doctor_treatment_cost.values, doctor_treatment_cost.index, "o", color='red')

#Adding titles and labels
plt.title('Ranking of Doctor based on Treatment Cost', fontsize=14)
plt.xlabel('Treatment Cost', fontsize=11)
plt.ylabel('Doctor Name', fontsize=12)

#add grid
plt.grid()

#display the plot
plt.show()





