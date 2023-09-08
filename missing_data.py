import matplotlib.pyplot as plt
import pandas as pd
career = pd.read_csv('ca.csv')


missing_percent = (career.isnull().sum() / len(career)) *100

plt.bar(missing_percent.index, missing_percent.values)
plt.xlabel('Columns')
plt.ylabel('Percentage of Missing Values')
plt.title('Percentage of Missing Values in Each Column')
plt.xticks(rotation=90)  # Rotate x-labels for better readability
plt.tight_layout()  # Prevent label cutoff
plt.show()

columns_to_impute = ['Database Fundamentals', 'Computer Architecture', 'Distributed Computing Systems','Cyber Security','Networking','Software Development','Programming Skills','Project Management','Computer Forensics Fundamentals','Technical Communication','AI ML','Software Engineering','Business Analysis','Communication skills','Data Science','Troubleshooting skills','Graphics Designing']


for column in columns_to_impute:
    if column in career.columns and career[column].dtype == 'object':
        mode_value = career[column].mode().values[0]  # Calculate the mode
        career[column].fillna(mode_value, inplace=True)  # Replace missing values with the mode

        career.to_csv('mising_update.csv', index=False)

career1= pd.read_csv('mising_update.csv')

missing_percent1 = (career1.isnull().sum() / len(career)) *100

plt.bar(missing_percent1.index, missing_percent1.values)
plt.xlabel('Columns')
plt.ylabel('Percentage of Missing Values')
plt.title('Percentage of Missing Values in Each Column')
plt.xticks(rotation=90)  # Rotate x-labels for better readability
plt.tight_layout()  # Prevent label cutoff
plt.show()