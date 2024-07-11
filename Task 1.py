import matplotlib.pyplot as plt

# Sample data: ages of a population
ages = [23, 45, 56, 45, 23, 67, 34, 23, 45, 56, 78, 34, 56, 34, 45, 23, 56, 67, 78, 89, 34, 23, 45, 67, 34]

# Create histogram
plt.hist(ages, bins=10, edgecolor='black')

# Add title and labels
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Show plot
plt.show()
