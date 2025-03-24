import numpy as np
import matplotlib.pyplot as plt
import random


# # Task 2a

# Define the function
def f(x):
    return np.exp(-x**2 / 3) + 3 * np.sin(x + np.pi / 4)

# Generate x values
x = np.linspace(-10, 10, 400)

# show the y value
y = f(x)

# Plot the function
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('f(x) = exp(-x^2 / 3) + 3 * sin(x + pi / 4)')
plt.legend()
plt.grid()
plt.show()


# -----------------------------------------------------------------------------
# # Task 2b

# Define the function
def x(t):
    return 2 * np.sin(t) * np.exp(np.cos(t))

def y(t):
    return (-3/2) * np.cos(t) * np.exp(np.sin(2*t))

# Generate values of t from 0 to 2π
t_values = np.linspace(0, 2*np.pi, 400)  # 400 points for smooth curve
y_values = y(t_values)  # show y(t) values

# Generate t values
t = np.linspace(0, 2 * np.pi, 400)

# show the x and y value
x = x(t)
y = y(t)

# Plot the function
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Parametric Curve')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('f(x) = 2 * sin(t) * (exp * (cos * t))')
plt.legend()
plt.grid()
plt.show()
# -----------------------------------------------------------------------------
# Task 3

random_numbers = np.random.randint(1, 100, 1000)

# Plot the histogram

plt.hist(random_numbers, bins=20, color='green', edgecolor='black', density=True, alpha=0.6, label='Histogram')

# Fit a normal distribution curve
mean = np.mean(random_numbers)
std_dev = np.std(random_numbers)
x = np.linspace(min(random_numbers), max(random_numbers), 1000)
normal_curve = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

# Plot the normal distribution curve
plt.plot(x, normal_curve, color='red', label='Normal Distribution')

# Calculate descriptive statistics
median = np.median(random_numbers)
min_value = np.min(random_numbers)
max_value = np.max(random_numbers)

# Print the statistics
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
print(f"Minimum Value: {min_value}")
print(f"Maximum Value: {max_value}")
# Add labels and title
plt.xlabel('Random Integers')
plt.ylabel('Density')
plt.title('1,000 Random Numbers with Normal Distribution Curve')
plt.legend()
plt.show()




# -----------------------------------------------------------------------------
# Task 4

# Bradley Howson
# 2315432

# 1) Change myID to your own student ID. This MUST be your student ID.
myID = "2315432"  # Change this to your actual student ID

# 2) User input validation
while True:
    try:
        varCount = int(input("Enter an number equal or more than 50: "))
        if varCount >= 50:
            break
        else:
            print("Error: Please enter a number of 50 or more.")
    except ValueError:
        print("Error: wrong input. Please enter a valid number.")

# 3) randSeedNum
s_d = sum(int(d) for d in myID)  # Converts each character in myID to an integer and sums them
random.seed(s_d)

# 4) Random list creation
data = [random.randint(1, 200) for _ in range(varCount)]

# Compute the sum of data
data_sum = sum(data)

# Compute the mean of data
data_mean = data_sum / len(data)

# Compute the minimum and maximum of data
data_min = min(data)
data_max = max(data)

# Print the results
print(f"Sum: {data_sum}, Mean: {data_mean:.2f}, Min: {data_min}, Max: {data_max}")

# Plot a histogram of data
plt.hist(data, bins=10, edgecolor='black', alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Random Data")
plt.show()
