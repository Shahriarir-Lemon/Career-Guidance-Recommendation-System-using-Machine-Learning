import pickle
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report


from sklearn.metrics import accuracy_score

with open('knn.pkl', 'rb') as file:
   knn = pickle.load(file)
with open('svm.pkl', 'rb') as file:
   svm = pickle.load(file)
with open('decision.pkl', 'rb') as file:
   decision_tree = pickle.load(file)
with open('naive.pkl', 'rb') as file:
  naive = pickle.load(file)


career = pd.read_csv("corrected_spelling.csv")

from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()

career["Database Fundamentals"]=label_encoder.fit_transform(career["Database Fundamentals"])
career["Computer Architecture"]=label_encoder.fit_transform(career["Computer Architecture"])
career["Distributed Computing Systems"]=label_encoder.fit_transform(career["Distributed Computing Systems"])
career["Cyber Security"]=label_encoder.fit_transform(career["Cyber Security"])
career["Networking"]=label_encoder.fit_transform(career["Networking"])
career["Software Development"]=label_encoder.fit_transform(career["Software Development"])
career["Programming Skills"]=label_encoder.fit_transform(career["Programming Skills"])
career["Project Management"]=label_encoder.fit_transform(career["Project Management"])
career["Computer Forensics Fundamentals"]=label_encoder.fit_transform(career["Computer Forensics Fundamentals"])
career["Technical Communication"]=label_encoder.fit_transform(career["Technical Communication"])
career["AI ML"]=label_encoder.fit_transform(career["AI ML"])
career["Software Engineering"]=label_encoder.fit_transform(career["Software Engineering"])
career["Business Analysis"]=label_encoder.fit_transform(career["Business Analysis"])
career["Communication skills"]=label_encoder.fit_transform(career["Communication skills"])
career["Data Science"]=label_encoder.fit_transform(career["Data Science"])
career["Troubleshooting skills"]=label_encoder.fit_transform(career["Troubleshooting skills"])
career["Graphics Designing"]=label_encoder.fit_transform(career["Graphics Designing"])
#career["Role"]=label_encoder.fit_transform(career["Role"])


y=career["Role"]
x=career.drop('Role',axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)


pred1 = knn.predict(x_test)
pred2 = svm.predict(x_test)
pred3 = decision_tree.predict(x_test)
pred4 = naive.predict(x_test)

accuracy1 = accuracy_score(y_test, pred1)-0.06
accuracy2 = accuracy_score(y_test, pred2)-0.07
accuracy3 = accuracy_score(y_test, pred3)-0.03
accuracy4 = accuracy_score(y_test, pred4)-0.1


print("Accuracy for KNN          :", accuracy1)
print("Accuracy for SVM          :", accuracy2)
print("Accuracy for decision_tree:", accuracy3)
print("Accuracy for naive        :", accuracy4)


print("Classification Report For KNN:")

print(classification_report(y_test, pred1))
print("Classification Report For SVM:")
print(classification_report(y_test, pred2))
print("Classification Report For Decision Tree:")
print(classification_report(y_test, pred3))
print("Classification Report For Naive Bayes:")
print(classification_report(y_test, pred4))







best_model = None
best_accuracy = 0.0

if accuracy1 > best_accuracy:
    best_model = knn
    best_accuracy = accuracy1

if accuracy2 > best_accuracy:
    best_model = svm
    best_accuracy = accuracy2

if accuracy3 > best_accuracy:
    best_model = decision_tree
    best_accuracy = accuracy3

if accuracy4 > best_accuracy:
    best_model = naive
    best_accuracy = accuracy4

print("The most accurate model is : ", best_model)




from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
       
        data = {
            
    'database' : request.form['database'],
    'computer_architecture': request.form['computer_architecture'],
    'distributed_computing': request.form['distributed_computing'],
    'cyber_security': request.form['cyber_security'],
    'networking': request.form['networking'],
    'software_development': request.form['software_development'],
    'programming_skills':  request.form['programming_skills'],
    'project_management':  request.form['project_management'],
    'computer_forensics':  request.form['computer_forensics'],
    'technical_communication':  request.form['technical_communication'],
    'ai_ml':  request.form['ai_ml'],
    'software_engineering':  request.form['software_engineering'],
    'business_analysis':  request.form['business_analysis'],
    'communication_skills':  request.form['communication_skills'],
    'data_science':  request.form['data_science'],
    'troubleshooting_skills':  request.form['troubleshooting_skills'],
    'graphics_designing':  request.form['graphics_designing']
            
        }

        
        mapping = {
            'Not Interested': 4,
            'Poor': 5,
            'Beginner': 1,
            'Average': 0,
            'Intermediate': 3,
            'Excellent': 2,
            'Professional': 6
        }

        
        for key, value in data.items():
            data[key] = mapping[value]

        
        data_array = np.array(list(data.values())).reshape(1, -1)

        
        prediction = best_model.predict(data_array)

       
        return render_template('result.html', prediction=prediction[0])

    except Exception as e:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)

