from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# تحميل النموذج
model = joblib.load("../model/model.pkl")
@app.route("/")
def home():
    return "API Failure Prediction Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    api_calls = data["api_calls"]
    response_time = data["response_time"]
    previous_failures = data["previous_failures"]

    prediction = model.predict([[
        api_calls,
        response_time,
        previous_failures
    ]])

    result = "FAIL" if prediction[0] == 1 else "PASS"

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)