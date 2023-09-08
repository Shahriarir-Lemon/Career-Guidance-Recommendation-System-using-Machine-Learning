import pandas as pd
from sklearn import metrics
import pickle as pk

career = pd.read_csv("corrected_spelling.csv")

from sklearn.preprocessing import LabelEncoder

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

y = career["Role"]
x = career.drop('Role', axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

from sklearn.naive_bayes  import GaussianNB
nb=GaussianNB()
scores = {}
nb.fit(x_train, y_train)

y_pred = nb.predict(x_test)
print('y_pred', y_pred)

scores[5] = metrics.accuracy_score(y_test, y_pred)
print('Accuracy=', scores[5] * 100)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

with open('label_encoders.pkl', 'wb') as file:
    pk.dump(label_encoders, file)

with open('naive.pkl', 'wb') as file:
    pk.dump(nb, file)
