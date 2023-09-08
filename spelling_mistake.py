import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import enchant  # Import the enchant library
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

df = pd.read_csv('corrected_spelling.csv')


text_columns  = ['Database Fundamentals', 'Computer Architecture', 'Distributed Computing Systems','Cyber Security','Networking','Software Development','Programming Skills','Project Management','Computer Forensics Fundamentals','Technical Communication','AI ML','Software Engineering','Business Analysis','Communication skills','Data Science','Troubleshooting skills','Graphics Designing']

mistake_counters = {col: Counter() for col in text_columns}
total_word_counters = {col: Counter() for col in text_columns}
column_percentages = {}

dictionary = enchant.Dict("en_US")

# Define a function to extract words from text, count unique spelling mistakes, and total words
def count_spelling_mistakes_and_total_words(text, mistake_counter, total_word_counter):
    words = text.split()
    for word in words:
        total_word_counter[word] += 1
        if not dictionary.check(word):  # Check if the word is a spelling mistake
            mistake_counter[word] += 1


# Calculate the unique spelling mistake percentages for each text column
for col in text_columns:
    df[col].apply(lambda text: count_spelling_mistakes_and_total_words(text, mistake_counters[col], total_word_counters[col]))
    total_mistakes = sum(mistake_counters[col].values())
    total_words = sum(total_word_counters[col].values())
    column_percentages[col] = (total_mistakes / total_words) * 100 if total_words > 0 else 0


# Create a bar chart to visualize unique spelling mistake percentages for each column
print(plt.figure(figsize=(10, 6)))
print(plt.bar(column_percentages.keys(), column_percentages.values(), color='red'))
plt.xlabel('Columns')
plt.ylabel('Spelling Mistake Percentage (%)')
plt.title('Spelling Mistake Percentages in CSV Data (Column-wise)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


career= pd.read_csv('removed_stopwords.csv')

valid_categories_dict = {
    'Database Fundamentals': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Computer Architecture': ['Professional','Not Interested',  'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Distributed Computing Systems': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Cyber Security': ['Professional','Not Interested',  'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Networking': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Software Development': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Programming Skills': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Project Management': ['Professional', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Computer Forensics Fundamentals': ['Professional','Not Interested',  'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Technical Communication': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'AI ML': ['Professional', 'Excellent', 'Not Interested', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Software Engineering': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Business Analysis': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Communication skills': ['Professional','Not Interested',  'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Data Science': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Troubleshooting skills': ['Professional','Not Interested',  'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    'Graphics Designing': ['Professional', 'Not Interested', 'Excellent', 'Intermediate', 'Average', 'Beginner', 'Poor'],
    
}

def find_closest_match(category, valid_categories):
    closest_match, score = process.extractOne(category, valid_categories, scorer=fuzz.token_sort_ratio)
    if score >= 60:  # Adjust the threshold as needed
        return closest_match
    else:
        return category  # Keep the original category if no close match is found

# Iterate through the categorical columns and apply the correction function
for column in valid_categories_dict.keys():
    valid_categories = valid_categories_dict[column]
    career[column] = career[column].apply(lambda x: find_closest_match(x, valid_categories))

career.to_csv('corrected_spelling.csv', index=False)



df = pd.read_csv('corrected_spelling.csv')


text_columns  = ['Database Fundamentals', 'Computer Architecture', 'Distributed Computing Systems','Cyber Security','Networking','Software Development','Programming Skills','Project Management','Computer Forensics Fundamentals','Technical Communication','AI ML','Software Engineering','Business Analysis','Communication skills','Data Science','Troubleshooting skills','Graphics Designing']

mistake_counters = {col: Counter() for col in text_columns}
total_word_counters = {col: Counter() for col in text_columns}
column_percentages = {}

dictionary = enchant.Dict("en_US")

# Define a function to extract words from text, count unique spelling mistakes, and total words
def count_spelling_mistakes_and_total_words(text, mistake_counter, total_word_counter):
    words = text.split()
    for word in words:
        total_word_counter[word] += 1
        if not dictionary.check(word):  # Check if the word is a spelling mistake
            mistake_counter[word] += 1


# Calculate the unique spelling mistake percentages for each text column
for col in text_columns:
    df[col].apply(lambda text: count_spelling_mistakes_and_total_words(text, mistake_counters[col], total_word_counters[col]))
    total_mistakes = sum(mistake_counters[col].values())
    total_words = sum(total_word_counters[col].values())
    column_percentages[col] = (total_mistakes / total_words) * 100 if total_words > 0 else 0


# Create a bar chart to visualize unique spelling mistake percentages for each column
print(plt.figure(figsize=(10, 6)))
print(plt.bar(column_percentages.keys(), column_percentages.values(), color='red'))
plt.xlabel('Columns')
plt.ylabel('Spelling Mistake Percentage (%)')
plt.title('Spelling Mistake Percentages in CSV Data (Column-wise)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()