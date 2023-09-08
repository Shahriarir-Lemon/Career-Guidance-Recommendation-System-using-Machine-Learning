import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords

import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

import nltk
nltk.download('punkt')



df = pd.read_csv('mising_update.csv')

text_columns  = ['Database Fundamentals', 'Computer Architecture', 'Distributed Computing Systems','Cyber Security','Networking','Software Development','Programming Skills','Project Management','Computer Forensics Fundamentals','Technical Communication','AI ML','Software Engineering','Business Analysis','Communication skills','Data Science','Troubleshooting skills','Graphics Designing']

# Initialize counters for each text column
stopword_counters = {col: Counter() for col in text_columns}
total_word_counters = {col: Counter() for col in text_columns}
column_percentages = {}

# Customize your list of stop words based on your specific data and needs
custom_stop_words = set(["i", "on", "all", "up", "do", "only","so", "is","are","by","at"])

# Define a function to extract words from text, count stop words, and total words
def count_stopwords_and_total_words(text, stopword_counter, total_word_counter):
    words = text.split()
    for word in words:
        total_word_counter[word] += 1
        if word.lower() in custom_stop_words:  # Check if the word is in your custom stop words list
            stopword_counter[word] += 1


# Calculate the percentage of stop words for each text column
for col in text_columns:
    df[col].apply(lambda text: count_stopwords_and_total_words(text, stopword_counters[col], total_word_counters[col]))
    total_stopwords = sum(stopword_counters[col].values())
    total_words = sum(total_word_counters[col].values())
    column_percentages[col] = (total_stopwords / total_words) * 100 if total_words > 0 else 0


# Create a bar chart to visualize stop word percentages for each column
plt.figure(figsize=(10, 6))
plt.bar(column_percentages.keys(), column_percentages.values(), color='blue')
plt.xlabel('Columns')
plt.ylabel('Stop Word Percentage (%)')
plt.title('Stop Word Percentages in CSV Data (Column-wise)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()




# Define your custom stopwords list
custom_stopwords = ["i", "on", "all", "up", "do", "only","so", "is","are","by","at"]  # Add your custom stopwords here

# Function to remove custom stopwords
def remove_custom_stopwords(text):
    words = nltk.word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in custom_stopwords]
    return ' '.join(filtered_words)

# Read the CSV file
career = pd.read_csv('mising_update.csv')

# Define the columns you want to clean
columns_to_clean = ['Database Fundamentals', 'Computer Architecture', 'Distributed Computing Systems',
                    'Cyber Security', 'Networking', 'Software Development', 'Programming Skills',
                    'Project Management', 'Computer Forensics Fundamentals', 'Technical Communication',
                    'AI ML', 'Software Engineering', 'Business Analysis', 'Communication skills',
                    'Data Science', 'Troubleshooting skills', 'Graphics Designing']

# Apply the custom stopwords removal function to the specified columns
for column in columns_to_clean:
    career[column] = career[column].apply(remove_custom_stopwords)

# Save the cleaned DataFrame to a new CSV file
career.to_csv('removed_stopwords.csv', index=False)



df = pd.read_csv('removed_stopwords.csv')

text_columns  = ['Database Fundamentals', 'Computer Architecture', 'Distributed Computing Systems','Cyber Security','Networking','Software Development','Programming Skills','Project Management','Computer Forensics Fundamentals','Technical Communication','AI ML','Software Engineering','Business Analysis','Communication skills','Data Science','Troubleshooting skills','Graphics Designing']

# Initialize counters for each text column
stopword_counters = {col: Counter() for col in text_columns}
total_word_counters = {col: Counter() for col in text_columns}
column_percentages = {}

# Customize your list of stop words based on your specific data and needs
custom_stop_words = set(["i", "on", "all", "up", "do", "only","so", "is","are","by","at"])

# Define a function to extract words from text, count stop words, and total words
def count_stopwords_and_total_words(text, stopword_counter, total_word_counter):
    words = text.split()
    for word in words:
        total_word_counter[word] += 1
        if word.lower() in custom_stop_words:  # Check if the word is in your custom stop words list
            stopword_counter[word] += 1


# Calculate the percentage of stop words for each text column
for col in text_columns:
    df[col].apply(lambda text: count_stopwords_and_total_words(text, stopword_counters[col], total_word_counters[col]))
    total_stopwords = sum(stopword_counters[col].values())
    total_words = sum(total_word_counters[col].values())
    column_percentages[col] = (total_stopwords / total_words) * 100 if total_words > 0 else 0


# Create a bar chart to visualize stop word percentages for each column
plt.figure(figsize=(10, 6))
plt.bar(column_percentages.keys(), column_percentages.values(), color='blue')
plt.xlabel('Columns')
plt.ylabel('Stop Word Percentage (%)')
plt.title('Stop Word Percentages in CSV Data (Column-wise)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
