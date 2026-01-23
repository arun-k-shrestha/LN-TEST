import matplotlib.pyplot as plt

# This is of 40 nodes with 25 transactions - the result might change as we increase number of nodes and transactions

# X values: percentages from 0% to 30% with 5% steps
x = [0, 5, 10, 15]

# Three lists of success rates

# under different Malacious conditions
base_score = [100, 82.2, 62.5,44]
additive = [100, 87.3, 68, 45]
inverse = [100, 86.1, 59, 40.1]

# Plot the lines
plt.plot(x, base_score, marker='o', label='Baseline')
plt.plot(x, additive, marker='s', label='Additive Score')
plt.plot(x, inverse, marker='^', label='Inverse Score')

# Labels and title
plt.xlabel('Percentage (%)')
plt.ylabel('Success Rate (%)')
plt.title('Success Rate vs Malacious Node')

# Axis limits
plt.xlim(0, 30)
plt.ylim(0, 100)

# Grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
