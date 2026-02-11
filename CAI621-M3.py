# Import necessary libraries
import pandas as pd
from sklearn. preprocessing import MinMaxScaler, StandardScale

# Load the dataset
movie_data = pd. read_csv('movies.csv')

# Choose an appropriate numerical column for normalization (replace 'numerical_column' with an actual column name)
numerical_column = 'Revenue' # Replace with the actual column name
data = movie_data[[numerical_column]].dropna().values

# Apply Min-Max normalization to the chosen numerical column using Scikit-learn
min_max_scaler = MinMaxScaler()
min_max_scaled_data = min_max_scaler.fit_transform(data)
print(f"Min-Max Scaled '{numerical_column}' column:\n", min_max_scaled_data [:5])

# Apply Mean normalization to the chosen numerical column using Scikit-learn
mean_scaler = StandardScaler(with_mean=True, with_std=False)
mean_normalized_data = mean_scaler.fit_transform(data)
print(f"\nMean Normalized '{numerical_column}' column:\n", mean_normalized_data [:5])

# Question 1: Load the dataset from Population.csv and split it into training and testing sets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn. linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
population_data = pd. read_csv('population.csv')

# Assume 'Population' is the target variable and the rest are features
X = population_data.drop(columns=['Population']).values
y = population_data ['Population']. values

# Split the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construct a linear regression model using the training data, fit the model then calculate the Mean Square Error (M!
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#Calculate MSE
MSE = mean_squared_error(y_test, y_pred)
print("Mean Square Error (MSE):", MSE)

# Calculate Accuracy
r2_score = model.score(X_test, y_test)
print("R^2 Score: ", r2_score)


#Task3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn. linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#Click to add a breakpoint om stock. csv and handle missing values by filling them with the mean of their respective columns
# Luau the uataset
stock_data = pd. read_csv('stock.csv')
stock_data. head()

# Handle missing values by filling them with the mean (one simple line)
stock_data. fillna(stock_data.mean(), inplace=True)

# Split the data into features and target variable
# Assuming the last column is the target variable
X = stock_data. iloc[:, :- 1].values
y = stock_data. iloc[:, -1]. values

# Split the dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit a linear regression model and calculate the Mean Square Error (MSE) of the model's predictions on the testing data

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Square Error (MSE):", mse)


# Plot the test data against the predicted values to visualize the model's performance
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")
plt.show()


# Make Future Predictions
# Use the model to make future predictions of values using the linear regression model
# Example future data with the same number of features
future_data = np.array([[90, 90, 90,90,90,90,90,90], [90, 90, 90,90,90,90,90, 90] ] ) # Replace with actual future data
#Don't forget to replace the 90 with resonable future data
future_predictions = model.predict(future_data)
print("Future Predictions:", future_predictions)





