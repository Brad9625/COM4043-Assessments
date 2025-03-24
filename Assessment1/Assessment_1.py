import numpy as np
import matplotlib.pyplot as plt


# # Task 2a

# Define the function
# def f(x):
#     return np.exp(-x**2 / 3) + 3 * np.sin(x + np.pi / 4)

# # Generate x values
# x = np.linspace(-10, 10, 400)

# # show the y value
# y = f(x)

# # Plot the function
# plt.figure(figsize=(8, 5))
# plt.plot(x, y, label='f(x)')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.title('f(x) = exp(-x^2 / 3) + 3 * sin(x + pi / 4)')
# plt.legend()
# plt.grid()
# plt.show()


# -----------------------------------------------------------------------------
# # Task 2b

# # Define the function
# def x(t):
#     return 2 * np.sin(t) * np.exp(np.cos(t))

# def y(t):
#     return (-3/2) * np.cos(t) * np.exp(np.sin(2*t))

# # Generate values of t from 0 to 2π
# t_values = np.linspace(0, 2*np.pi, 400)  # 400 points for smooth curve
# y_values = y(t_values)  # show y(t) values

# # Generate t values
# t = np.linspace(0, 2 * np.pi, 400)

# # show the x and y value
# x = x(t)
# y = y(t)

# # Plot the function
# plt.figure(figsize=(8, 5))
# plt.plot(x, y, label='Parametric Curve')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.title('f(x) = 2 * sin(t) * (exp * (cos * t))')
# plt.legend()
# plt.grid()
# plt.show()
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

# Add labels and title
plt.xlabel('Random Integers')
plt.ylabel('Density')
plt.title('1,000 Random Numbers with Normal Distribution Curve')
plt.legend()
plt.show()

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