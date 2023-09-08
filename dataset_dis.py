import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file into a DataFrame
file_path = 'ca.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Specify the categorical column you want to analyze
categorical_column = 'Role'  # Replace with the name of your categorical column

# Get a Series with counts for each category
category_counts = df[categorical_column].value_counts()

# Calculate the percentage for each category
total_data_points = len(df)
percentage_counts = (category_counts / total_data_points) * 100

# Create a pie chart with labels and percentages
plt.figure(figsize=(8, 8))  # Adjust the figure size as needed
plt.pie(percentage_counts, labels=[f'{cat}: {perc:.1f}%' for cat, perc in zip(category_counts.index, percentage_counts)], startangle=140, autopct='%1.1f%%')

# Add a title
#plt.title(f'Percentage Distribution of Categories in "{categorical_column}"')
print( "  ")

# Show the pie chart
plt.axis('equal')
plt.show()
