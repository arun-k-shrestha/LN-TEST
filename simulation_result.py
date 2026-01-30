import matplotlib.pyplot as plt

# This is of 40 nodes with 25 transactions - the result might change as we increase number of nodes and transactions

# X values: percentages from 0% to 30% with 5% steps
# x = [0,5,10,15,20,25,30]

# Three lists of success rates

# under different Malacious conditions #fixed balance
# base_score = [66, 56, 48, 37, 39, 22, 27]
# additive =   [100, 79, 75, 53, 57, 36, 31]
# mpc = [100, 85, 61, 41, 45, 32, 25]


# under different Malacious conditions #random balance
# base_score = [75, 66, 47, 40, 32, 29, 27]  # vs  [1.0, 0.74, 0.7, 0.56, 0.29, 0.32, 0.32] # 1 processor # 100 times
# additive =  [100,96,75,54,54,29,30] #[100, 74, 70, 56, 29, 32, 32] # 1000
# mpc = [100, 88, 63, 60, 37, 28, 27]


y = [0,2.5,5,7.5,10,12.5,15]

# Three lists of success rates

# under different Malacious conditions #fixed balance
# base_score = [68.0, 59.0, 56.99, 53.0, 52.0, 34.0, 41.0]
# additive =   [0.72, 0.95, 0.53, 0.61, 0.71, 0.44, 0.53]
# mpc = [100, 92, 81, 76, 67, 56, 52]


# under different Malacious conditions #random balance
base_score = [72.0, 70.0, 61.0, 50.0, 47.0, 47.0, 41.0]  # vs  [1.0, 0.74, 0.7, 0.56, 0.29, 0.32, 0.32] # 1 processor # 100 times
additive =  [100, 91, 85, 67, 65, 48, 36] #[100, 74, 70, 56, 29, 32, 32] # 1000
mpc = [100, 87, 76, 62, 71, 54, 50]




# plt.plot(y, base_score, marker='o', label='Baseline')
# plt.plot(y, additive, marker='s', label='Additive Score')
# plt.plot(y, mpc, marker='^', label='MPC Score')

# Plot the lines
# plt.plot(x, base_score, marker='o', label='Baseline')
# plt.plot(x, additive, marker='s', label='Additive Score')
# plt.plot(x, mpc, marker='^', label='MPC Score')

plt.plot(y, base_score, marker='o', label='Baseline')
plt.plot(y, additive, marker='s', label='Additive Score')
plt.plot(y, mpc, marker='^', label='MPC Score')

# Labels and title
plt.xlabel('Percentage (%)')
plt.ylabel('Success Rate (%)')
plt.title('Success Rate vs Malacious Node')

# Axis limits
plt.xlim(0, 16)
plt.ylim(0, 100)

# Grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
