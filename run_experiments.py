import subprocess
import configparser
import re

# Define malicious percentages to test
malicious_percentages = [0.0,0.05,0.1,0.15,0.20,0.25,0.30]
success_rate =[]
# Regex pattern to extract success_percent
success_pattern = r"success_percent\s*:\s*([0-9.]+)"


for percent in malicious_percentages:
    print(f"\n{'='*50}")
    print(f"Running with {percent*100}% malicious nodes")
    print(f"{'='*50}\n")
    
    # Update config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['General']['malicious_percent'] = str(percent)
    
    with open('config.ini', 'w') as f:
        config.write(f)
    
    # Run the main script
     # Run the main script and capture output
    result = subprocess.run(
        ['python3', 'run_simulation_mpc.py'],
        capture_output=True,
        text=True
    )
    print("run_simulation_mpc.py")
    # Extract success_percent using regex
    match = re.search(success_pattern, result.stdout)
    if match:
        value = float(match.group(1))
        success_rate.append(value)
        print(f"Extracted success_percent: {value}")
    else:
        success_rate.append(None)
        print("Warning: success_percent not found!")
    
    print(f"\nCompleted {percent*100}% malicious nodes experiment")

print("\n" + "="*50)
print(success_rate)
print("All experiments completed!")