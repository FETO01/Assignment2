import pandas as pd
import seaborn as sns
import scipy.stats as stats
# Load the data
data = pd.read_csv("Data\production_defect_data.csv")
# Visualize the data
sns.countplot(x="product", y=,hue="defect", data=data)
# Use a chi-square test to determine if there is a significant relationship between the type of product and the occurrence of defects
contingency_table = pd.crosstab(data["product"], data["defect"])
_, p_value, _, _ = stats.chi2_contingency(contingency_table)
print(f"p-value: {p_value:.3f}")
# Use a t-test to determine if there is a significant difference in the mean rolling speed for products with defects versus those without defects
defects = data.loc[data["defect"]==1, "rolling_speed"]
no_defects = data.loc[data["defect"]==0, "rolling_speed"]
_, p_value = stats.ttest_ind(defects, no_defects)
print(f"p-value: {p_value:.3f}")
# Recommend process improvements or changes to raw materials that could reduce the occurrence of defects
if p_value < 0.05:
    print("There is a significant difference in the mean rolling speed for products with defects versus those without defects. Consider adjusting the rolling speed to reduce defects.")