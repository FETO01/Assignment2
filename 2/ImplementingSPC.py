import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Load the data
data = pd.read_csv("Data\SPC_data.csv")
# Calculate the process mean (X-bar) and standard deviation (R)
n = data.shape[0]  # sample size
X_bar = data["temperature"].mean()
R = data["temperature"].std()
print("mean = " + str(X_bar))
print("std = " + str(R))
# Calculate the control limits for an X-bar and R chart
UCL_X_bar = X_bar + 3*R/np.sqrt(n)
LCL_X_bar = X_bar - 3*R/np.sqrt(n)
print("[LCL,UCL] for mean = [" + str(LCL_X_bar) + "," + str(UCL_X_bar) + "]")
UCL_R = 3*R
LCL_R = 0
print("[LCL,UCL] for std = [" + str(LCL_R) + "," + str(UCL_R) + "]")
# Plot the X-bar and R charts
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(data.index, data["temperature"], "o-")
ax1.hlines(UCL_X_bar, data.index[0], data.index[-1], "r")
ax1.hlines(LCL_X_bar, data.index[0], data.index[-1], "r")
ax1.set_ylabel("Temperature")
# Calculate the moving range (MR) and plot the MR chart
MR = data["temperature"].diff().abs()
ax2.plot(MR, "o-")
ax2.hlines(UCL_R, MR.index[0], MR.index[-1], "r")
ax2.hlines(LCL_R, MR.index[0], MR.index[-1], "r")
ax2.set_ylabel("MR")
# Show both charts
plt.show()
# Interpret the control charts and identify any points that fall outside of the control limits
for i, value in enumerate(data["temperature"]):
    if value > UCL_X_bar or value < LCL_X_bar:
        print(f"Temperature out of control at index {i}: {value}")
for i, value in enumerate(MR):
    if value > UCL_R or value < LCL_R:
        print(f"MR out of control at index {i}: {value}")
# Investigate the causes of any out-of-control points and recommend corrective actions