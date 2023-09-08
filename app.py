from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


with open('decision.pkl', 'rb') as file:
   decision_tree = pickle.load(file)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for form submission and model prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Access form data submitted by the user
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
            # Add more form data for each label in the HTML form
        }

        # Map the form data to numerical values, if needed
        # For example, you can create a dictionary to map options to numerical values
        mapping = {
            'Not Interested': 4,
            'Poor': 5,
            'Beginner': 1,
            'Average': 0,
            'Intermediate': 3,
            'Excellent': 2,
            'Professional': 6
        }

        # Convert the form data to numerical values
        for key, value in data.items():
            data[key] = mapping[value]

        # Convert the data to a numpy array
        data_array = np.array(list(data.values())).reshape(1, -1)

        # Make predictions using the loaded model
        prediction = decision_tree.predict(data_array)

        # Return the prediction as a template variable to display on the result page
        return render_template('result.html', prediction=prediction[0])

    except Exception as e:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
