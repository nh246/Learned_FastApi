# Health Insurance AI Prediction API

A FastAPI-based web service for predicting health insurance categories based on user-provided health and demographic data. The API uses a machine learning model to classify insurance risk into categories such as Low, Medium, and High.

## Features

- **Health Risk Prediction**: Predicts insurance category based on BMI, age group, lifestyle risk, city tier, income, and occupation.
- **Automatic Calculations**: Computes BMI, lifestyle risk, age group, and city tier from raw input data.
- **Model Confidence**: Provides prediction confidence and class probabilities.
- **Health Check Endpoint**: Includes endpoints for application health and model status.
- **Docker Support**: Easily deployable using Docker.

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Local Setup

1. Clone the repository:
   ```bash
   git clone git@github.com:nh246/Learned_FastApi.git
   cd Health_insurance_ai
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app:app --reload
   ```

The API will be available at `http://localhost:8000`.

### Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t health-insurance-ai .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 health-insurance-ai
   ```

The API will be available at `http://localhost:8000`.

## Usage

### API Endpoints

#### GET /
Returns a simple status check.

**Response:**
```json
{
  "status": "OK"
}
```

#### GET /health
Provides health check information including model version and status.

**Response:**
```json
{
  "status": "healthy",
  "model_version": "1.0.0",
  "model_loaded": true
}
```

#### POST /predict
Predicts the health insurance category based on user input.

**Request Body:**
```json
{
  "age": 30,
  "weight": 70.0,
  "height": 1.75,
  "income_lpa": 5.0,
  "smoker": false,
  "city": "Dhaka",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "response": {
    "predicted_catagory": "Medium",
    "confidence": 0.85,
    "class_probabilities": {
      "Low": 0.1,
      "Medium": 0.3,
      "High": 0.6
    }
  }
}
```

### Input Validation

- **age**: Integer between 1 and 119
- **weight**: Float greater than 0 (in kg)
- **height**: Float between 0 and 2.5 (in meters)
- **income_lpa**: Float greater than 0 (in lakhs per annum)
- **smoker**: Boolean
- **city**: String (normalized to title case)
- **occupation**: One of: 'retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'

### Computed Fields

The API automatically computes the following from input data:
- **BMI**: Calculated as weight / (height²)
- **Lifestyle Risk**: 'low', 'medium', or 'high' based on smoking status and BMI
- **Age Group**: 'young', 'adult', 'middle_aged', or 'senior'
- **City Tier**: 1, 2, or 3 based on predefined city lists

## Model

The prediction model is a machine learning classifier trained on health insurance data. It classifies users into risk categories and provides confidence scores and probability distributions.

- **Model Version**: 1.0.0
- **Model File**: `model/model.pkl`
- **Algorithm**: Scikit-learn classifier (details in model file)

## Project Structure

```
Health_insurance_ai/
├── app.py                 # Main FastAPI application
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── config/
│   └── city_tier.py       # City tier definitions
├── model/
│   ├── predict.py         # Prediction logic
│   └── model.pkl          # Trained ML model
└── schema/
    ├── user_input.py      # Input validation schema
    └── predicion_response.py  # Response schema
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## API Documentation

Once the application is running, visit `http://localhost:8000/docs` for interactive API documentation powered by Swagger UI.</content>
<parameter name="filePath">e:\Learn fast api\Learned_fastapi\Health_insurance_ai\README.md
