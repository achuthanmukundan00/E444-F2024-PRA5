# ECE444 Lab 5: Fake News Detection

This is a Flask application that allows users to interact with a machine learning model for fake news detection via POST requests. The app is deployed on AWS Elastic Beanstalk, making the model accessible as a service through a RESTful API.

## Features
- **Machine Learning Integration**: The app uses a trained model to classify news articles as "real" or "fake" based on their content.
- **RESTful API**: Users can send POST requests to the `/predict` endpoint to receive predictions.
- **AWS Elastic Beanstalk Deployment**: The app is deployed to AWS, providing a scalable and easily accessible web service.

## How to Use
To interact with the app, send a POST request to the endpoint:
```
POST http://ece444-pra5-app-environment.eba-3c2rf3gh.us-east-2.elasticbeanstalk.com/predict
```

### Sample Request
```json
{
  "text": "This is an example news article."
}
```

### Sample Response
```json
{
  "prediction": "fake"
}
```

## API Latency Measurements
![API Latency](https://github.com/achuthanmukundan00/E444-F2024-PRA5/blob/master/boxplot.png)

