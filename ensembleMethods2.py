import pandas as pd
from sklearn.ensemble import BaggingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Load the historical stock prices into a pandas dataframe
stock_data = pd.read_csv('stock_prices.csv')

# Define the predictor and target variables
X = stock_data[['Open', 'High', 'Low', 'Volume']]
y = stock_data['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the base model
dt = DecisionTreeRegressor()

# Create the Bagging ensemble model
bagging = BaggingRegressor(base_estimator=dt, n_estimators=10, random_state=42)

# Create the Boosting ensemble model
boosting = AdaBoostRegressor(base_estimator=dt, n_estimators=10, random_state=42)

# Train the ensemble models on the training data
bagging.fit(X_train, y_train)
boosting.fit(X_train, y_train)

# Use the ensemble models to make predictions on the test data
y_pred_bagging = bagging.predict(X_test)
y_pred_boosting = boosting.predict(X_test)

# Calculate the ensemble models' accuracy
accuracy_bagging = bagging.score(X_test, y_test)
accuracy_boosting = boosting.score(X_test, y_test)
print("Accuracy of Bagging: {:.2f}%".format(accuracy_bagging*100))
print("Accuracy of Boosting: {:.2f}%".format(accuracy_boosting*100))
