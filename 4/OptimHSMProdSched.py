import pandas as pd
import pulp
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("Data\HSM_prod_sched_data.csv")
# Create the optimization model
model = pulp.LpProblem("Hot Strip Mill Production Scheduling", pulp.LpMaximize)
# Define the decision variables
production_variables = pulp.LpVariable.dicts("production", (data["product"], data["deadline"]), lowBound=0, cat="Integer")
# Define the objective function
model += sum(production_variables[i][j]*data.loc[(data["product"]==i) & (data["deadline"]==j), "profit"].values[0] for i in data["product"] for j in data["deadline"])
# Define the capacity constraints
model += sum(production_variables[i][j] for i in data["product"] for j in data["deadline"]) <= data.loc[:, "capacity"].sum()
# Define the deadline constraints
for j in data["deadline"]:
    model += sum(production_variables[i][j] for i in data["product"]) <= data.loc[data["deadline"]==j, "demand"].sum()
# Solve the optimization problem
model.solve()
# Print the optimal production schedule
A_tot = 0
B_tot = 0
C_tot = 0
for i in data["product"]:
    for j in data["deadline"]:
        if production_variables[i][j].value() > 0: # if quantity to be produced > 0
            print(f"Product {i} should be produced in quantity {production_variables[i][j].value()} for deadline {j}")
            if i == "A":
                A_tot += production_variables[i][j].value()
            elif i == "B":
                B_tot += production_variables[i][j].value()
            elif i == "C":
                C_tot += production_variables[i][j].value()
# Print the optimal objective value (total profit)
print("Total quantity of Product A = ",A_tot)
print("Total quantity of Product B = ",B_tot)
print("Total quantity of Product C = ",C_tot)
plt.figure()
plt.bar(["A","B","C"],[A_tot,B_tot,C_tot],edgecolor="black")
plt.xlabel("Product")
plt.ylabel("Total Quantity")
plt.show()
print(f"Total Profit: ${pulp.value(model.objective):.2f}")