import pandas as pd
from sklearn import metrics
import pickle as pk
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

career = pd.read_csv("corrected_spelling.csv")
print(career)
# Define the columns you want to apply LabelEncoder to
columns_to_encode = [
    "Database Fundamentals",
    "Computer Architecture",
    "Distributed Computing Systems",
    "Cyber Security",
    "Networking",
    "Software Development",
    "Programming Skills",
    "Project Management",
    "Computer Forensics Fundamentals",
    "Technical Communication",
    "AI ML",
    "Software Engineering",
    "Business Analysis",
    "Communication skills",
    "Data Science",
    "Troubleshooting skills",
    "Graphics Designing",
]

label_encoders = {} 

for column in columns_to_encode:
    label_encoder = LabelEncoder()
    career[column] = label_encoder.fit_transform(career[column])
    label_encoders[column] = label_encoder

print(career)
y = career["Role"]
x = career.drop('Role', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

knn = KNeighborsClassifier()
scores = {}
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)
print('y_pred', y_pred)

scores[5] = metrics.accuracy_score(y_test, y_pred)
print('Accuracy=', scores[5] * 100)

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

# Save the label encoders to a file for later use
with open('label_encoders.pkl', 'wb') as file:
    pk.dump(label_encoders, file)

# Save the trained KNeighborsClassifier to a file
with open('knn.pkl', 'wb') as file:
    pk.dump(knn, file)
