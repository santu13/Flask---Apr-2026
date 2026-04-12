from flask import Flask, request
import pickle

app = Flask(__name__)

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return "<h1>Welcome to Loan API</h1>"

@app.route('/predict')
def predict():
    return 'I will predict the loan status based on the input data'

@app.route('/predict', methods=['POST'])
def make_predict():
    data = request.get_json()  # Get the JSON data from the POST request
    print(data)  # Print the received data to the console for debugging
    if data['Gender'] == 'Male':
        gender = 0
    else:
        gender = 1

    if data['Married'] == 'No':
        married = 0
    else:
        married = 1
    input_features = [[gender, married, data['ApplicantIncome'], data['LoanAmount'], data['Credit_History']]]
    print(input_features)
    result = model.predict(input_features)
    if result[0] == 0:
        result = "Loan is Rejected"
    else:
        result = "Loan is Approved"

    return {'loan_approval_status': result}

    #return 'POST REQUEST RECEIVED'

if __name__ == '__main__':
    app.run(debug=True) # Run the Flask application in debug mode for development purposes