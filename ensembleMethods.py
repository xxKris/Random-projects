import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
from sklearn.model_selection import train_test_split

# Load the historical stock prices into a pandas dataframe
stock_data = pd.read_csv('stock_prices.csv')

# Define the predictor and target variables
X = stock_data[['Open', 'High', 'Low', 'Volume']]
y = stock_data['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the individual models
rf = RandomForestRegressor()
gb = GradientBoostingRegressor()

# Create the ensemble model
ensemble = VotingRegressor([('rf', rf), ('gb', gb)])

# Train the ensemble model on the training data
ensemble.fit(X_train, y_train)

# Use the ensemble model to make predictions on the test data
y_pred = ensemble.predict(X_test)

# Calculate the ensemble model's accuracy
accuracy = ensemble.score(X_test, y_test)
print("Accuracy: {:.2f}%".format(accuracy*100))
