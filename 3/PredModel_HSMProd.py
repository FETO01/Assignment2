import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("Data\hot_strip_mill_production_data.csv")
# Split the data into training and test sets
X = data[["market_demand", "raw_material_availability"]]
y = data["production"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print("Training n =", len(X_train))
print("Testing n =", len(X_test))
# Visualize data
plt.figure()
plt.subplot(211)
plt.plot(X["market_demand"],y, "ro")
plt.xlabel("market_demand")
plt.ylabel("production")
plt.subplot(212)
plt.plot(X["raw_material_availability"],y, "ro")
plt.xlabel("raw_material_availability")
plt.ylabel("production")
plt.subplots_adjust(hspace=.5)
# sns.pairplot(data, x_vars=["market_demand", "raw_material_availability"], y_vars=["production"])

# Fit a linear regression model
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
print("Regression Eqaution: Production = ",round(lin_reg.intercept_,3),round(lin_reg.coef_[0],3),"* market_demand",round(lin_reg.coef_[1],2),"* raw_market_availability")
# Make predictions and evaluate the model performance
y_pred = lin_reg.predict(X_test)
mae = round(mean_absolute_error(y_test, y_pred),3)
mse = round(mean_squared_error(y_test, y_pred),3)
r_squared = round(lin_reg.score(X_test,y_test),3) # coefficient of determination
print("Linear Regression: MAE =", mae, ", MSE =", mse, ", R-squared =", r_squared)

# Fit a decision tree model
tree_reg = DecisionTreeRegressor(max_depth=3)
tree_reg.fit(X_train, y_train)
# Make predictions and evaluate the model performance
y_pred = tree_reg.predict(X_test)
mae = round(mean_absolute_error(y_test, y_pred),3)
mse = round(mean_squared_error(y_test, y_pred),3)
r_squared = round(tree_reg.score(X_test,y_test),3) # coefficient of determination
print("Decision Tree: MAE =", mae, ", MSE =", mse, ", R-squared =", r_squared)
# Visualize tree
plt.figure()
plot_tree(tree_reg, filled=True)
plt.show()