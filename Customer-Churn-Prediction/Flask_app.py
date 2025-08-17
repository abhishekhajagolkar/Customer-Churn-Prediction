from flask import Flask, request, render_template
from Model import model  # Make sure model is properly loaded in Model.py (e.g., using pickle)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict_churn_view():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
            # Extract and convert form data
            gender = int(request.form['gender'])
            age = int(request.form['age'])
            tenure = int(request.form['tenure'])
            monthly = float(request.form['monthlyCharges'])
            total = float(request.form['totalCharges'])
            payment = int(request.form['paymentMethod'])
            contract = int(request.form['contractType'])
            internet = int(request.form['internetService'])
            streaming = int(request.form['streamingServices'])
            tech = int(request.form['techSupport'])

            # Make prediction using your ML model
            prediction = model.predict([[gender, age, tenure, monthly, total, payment, contract, internet, streaming, tech]]) # Assuming output is binary or label
            y_pred = round(prediction[0], 2)

            # Send result to template
            return render_template('Output.html', result=y_pred)


if __name__ == '__main__':
    app.run(debug=True)
