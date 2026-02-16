# Import matplotlib
import matplotlib.pyplot as plt

# Data
malicious_percentage = [0, 3, 6, 9, 12, 15]
MPC_Time = [0.2217, 0.2130, 0.2174, 0.2147, 0.2104, 0.2049]
LND_Time = [0.2208, 0.2121, 0.2181, 0.2135, 0.2099, 0.2037]

# Create plot
plt.figure()
plt.plot(malicious_percentage, MPC_Time)
plt.plot(malicious_percentage, LND_Time)

# Labels and title
plt.xlabel("Malicious Node Percentage (%)")
plt.ylabel("Path Find Time")
plt.title("MPC vs LND Path Find Time Comparison")

plt.show()
