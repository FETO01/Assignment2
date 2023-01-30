import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("Data\hot_strip_mill_data.csv")

# Visualize the data
sns.pairplot(data, x_vars=["rolling_speed", "temperature"], y_vars=["thickness", "surface_roughness"])
plt.show()

# Fit linear regression models

# Thickness Model
model1 = smf.ols(formula="thickness ~ rolling_speed + temperature", data=data).fit()
# Print the model summary
print("========================Thickness Model Summary========================")
print(model1.summary())
# Make predictions for different process variable values
print("=====================Predictions Using Thickness Model========================")
predictions1 = model1.predict({"rolling_speed": [100, 150, 200], "temperature": [700, 750, 800]})
print("rolling_speed = [100, 150, 200], temperature = [700,750,800]")
print(predictions1)

# Surface Roughness Model
model2 = smf.ols(formula="surface_roughness ~ rolling_speed + temperature", data=data).fit()
# Print the model summary
print("=======================Surface Roughness Model Summary=======================")
print(model2.summary())
# Make predictions for different process variable values
print("===================Predictions Using Surface Roughness Model======================")
predictions2 = model2.predict({"rolling_speed": [100, 150, 200], "temperature": [700, 750, 800]})
print("rolling_speed = [100, 150, 200], temperature = [700,750,800]")
print(predictions2)