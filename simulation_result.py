import matplotlib.pyplot as plt

# --------        Figure 1: Fixed Amount      -----------


malacious_percentage = [0,3,6,9,12,15]

# under different Malacious conditions with the fixed balance
lnd_path_fixed = [68, 59, 57, 53, 52, 40]
reputation_score_fixed =   [100, 93, 84, 75, 72, 60]
mpc_fixed = [100, 88, 73, 72, 63, 54]
shortest_path_fixed = [46,38,41,34.5,35,29]

plt.plot(malacious_percentage, lnd_path_fixed, marker='o', label='LND Routing')
plt.plot(malacious_percentage, reputation_score_fixed, marker='o', label='MPC + Rating Score')
plt.plot(malacious_percentage, mpc_fixed, marker='o', label='MPC Score')
plt.plot(malacious_percentage, shortest_path_fixed, marker='o', label='Shortest Path')

# Labels and title
plt.xlabel('Malicious Percentage (%)')
plt.ylabel('Success Rate (%)')
plt.title('Fixed Amount: Success Rate vs Malacious Node')

# Force x-axis ticks at specific values
plt.xticks([0, 3, 6, 9, 12, 15])

# Axis limits
plt.xlim(0, 16)
plt.ylim(0, 100)

plt.grid(True)
plt.legend()
# Show the plot
plt.show()



# --------        Figure 1: Random Amount      -----------


# under different Malacious conditions with the random balance
lnd_path_random = [72, 70, 61, 50, 47, 47]
reputation_score_random =   [100, 90, 88, 75, 80, 65]
mpc_random = [100, 87, 76, 62, 61, 54]
shortest_path_random = [46,39,41,37,33,29]

plt.plot(malacious_percentage, lnd_path_random, marker='o', label='LND Routing')
plt.plot(malacious_percentage, reputation_score_random, marker='o', label='MPC + Rating Score')
plt.plot(malacious_percentage, mpc_random, marker='o', label='MPC Score')
plt.plot(malacious_percentage, shortest_path_random, marker='o', label='Shortest Path')

# Labels and title
plt.xlabel('Malicious Percentage (%)')
plt.ylabel('Success Rate (%)')
plt.title('Random Amount: Success Rate vs Malacious Node')

# Force x-axis ticks at specific values
plt.xticks([0, 3, 6, 9, 12, 15])

# Axis limits
plt.xlim(0, 16)
plt.ylim(0, 100)

plt.grid(True)
plt.legend()
# Show the plot
plt.show()


# --------        Figure 3: MPC Overhead      -----------

# average time it takes for a payment under different Malacious conditions with the random balance
malacious_percentage = [0,3,6,9,12,15]
MPC_Time = [0.2217,0.2130,0.2174,0.2147,0.2104,0.2049]
LND_Time = [0.2208,0.2121,0.2181,0.2135,0.2099,0.2037]

# MPC_Success = [100,88,75,71,57,49]
# LND_Success = [72,65,57,55,45,41]

plt.plot(malacious_percentage, MPC_Time, marker='o', label='MPC')
plt.plot(malacious_percentage, LND_Time, marker='o', label='LND Routing')

# Labels and title
plt.xlabel('Malicious Percentage (%)')
plt.ylabel('Average Payment Time (seconds)')
plt.title('')

# Force x-axis ticks at specific values
plt.xticks([0, 3, 6, 9, 12, 15])

# Axis limits
plt.xlim(0, 16)
plt.ylim(0.19, 0.23)

plt.grid(True)
plt.legend()
# Show the plot
plt.show()



# MPC and LND Path find time difference testing
# Calcuation based on 10,000 simulation
# under [0%, 3%, 6%, 9%, 12%, 15%] malacious node
MPC_Time = [0.2217,0.2130,0.2174,0.2147,0.2104,0.2049]
LND_Time = [0.2208,0.2121,0.2181,0.2135,0.2099,0.2037]

#successrate
MPC_Success = [100,88,75,71,57,49]
LND_Success = [72,65,57,55,45,41]



# Reputation score Half-life tuning
# Calcuation based on 10,000 simulation
# under Half-life 1,2,4,8,16 events, and alpha = 1 and beta = 1
half_life_success = [72,68,67,69,72] #[1,2,4,8,16]


# Reputation score Half-life tuning
# Calcuation based on 10,000 simulation
# under Half-life, alpha, and beta = 1,2,4,8,16 
half_life_alpha_beta_success = [72,72,74,63,70] #[1,2,4,8,16]


# Reputation score Half-life tuning
# Calcuation based on 10,000 simulation
# under Half-life, alpha, and beta = 4, with rating score 0.05,0.10, 0.15, 0.20, 0.25
half_life_alpha_beta_success_threshold = [77,67,65,66,58] #[0.05,0.10,0.15,0.25]