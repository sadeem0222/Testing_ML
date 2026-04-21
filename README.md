 API Failure Prediction System (Flask + Machine Learning)

 Project Overview

This project is a **Machine Learning-based API Failure Prediction System** that predicts whether an API request will **PASS or FAIL** based on input features such as:

- Number of API calls
- Response time
- Previous failures

The trained model is deployed using **Flask**, allowing real-time predictions through an API endpoint.
A frontend (React) can be connected to interact with the prediction system.



 Machine Learning Model

The system uses:

- **Algorithm:** Random Forest Classifier
- **Libraries:**

  - scikit-learn
  - pandas
  - numpy
  - joblib

The model is trained using synthetic data simulating API behavior and failures.

##  Testing

API endpoints were tested using Postman to validate request-response behavior.

Tested Features:

* API request validation
* JSON request handling
* Prediction response verification
* Error handling scenarios

##  Deployment

The project is prepared for deployment using modern cloud tools.

### Backend Deployment

* Platform: Render
* Server: Flask with Gunicorn
* Dependencies managed using requirements.txt

##  Frontend (React)

A simple React-based user interface was developed to interact with the Machine Learning model.

Users can:

* Enter API testing data
* Send requests to the Flask backend
* Receive real-time predictions (PASS / FAIL)

The frontend communicates with the Flask API using HTTP POST requests.

To run the frontend:

```bash
cd frontend
npm install
npm start
```


##  Features Used

- api_calls
- response_time
- previous_failures

These features help the model identify patterns that lead to API failures.



## Future Improvements

- Add real-time dashboard
- Connect React frontend
- Use real API logs dataset
- Deploy using Docker
- Improve model accuracy

  ## Testing with Postman

1. Open Postman  
2. Set method to **POST**  
3. URL:
   http://127.0.0.1:5000/predict  
4. Go to Body → raw → JSON  
5. Paste request example  
6. Click Send  


##  Author

Developed by **Sadeem**
Machine Learning & Software Testing Enthusiast
