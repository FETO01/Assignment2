import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf

# Load the data
data = pd.read_csv("Data\energy_consumption_data.csv")
# Visualize the data
sns.pairplot(data, x_vars=["production_volume", "rolling_speed", "temperature"], y_vars=["energy_consumption"])
# Fit a linear regression model
model = smf.ols(formula="energy_consumption ~ production_volume + rolling_speed + temperature", data=data).fit()
# Print the model summary
print(model.summary())
# Interpret the results of the regression model and identify opportunities for energy efficiency improvements
for i, coef in enumerate(model.params):
    print(f"{model.params.index[i]}: {coef:.2f}")