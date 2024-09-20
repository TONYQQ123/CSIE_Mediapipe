import matplotlib.pyplot as plt
step = 0
# Read data from file
with open('pydraw.txt', 'r') as file:
    lines = file.readlines()

# Convert data to float
y = [float(line.strip()) for line in lines]
#y = [lines.strip() for line in lines]
# Generate x values (assuming consecutive integers)
# Convert data to integer
#y = [int(line.strip()) for line in lines]
#y = [int(line.strip()) for line in lines if line.strip()]
x = range(1, len(y) + 1)

# Plot
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Data Visualization')
plt.grid(True)
plt.show()

# Increase step if conditions are met
for i in range(2, len(y) - 2):
    if y[i-1] > y[i] and y[i] < y[i+1]:
        step += 1

print("Step:", step)
