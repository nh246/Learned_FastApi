from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, MODEL_VERSION
from schema.predicion_response import PredictionResponse


app = FastAPI()

#home endpoint
@app.get('/')
def home():
    return {
        'status': 'OK'
    }

# health check endpoint
@app.get('/health')
def health_check():
    return {
        'status': 'healthy',
        'model_version': MODEL_VERSION,
        'model_loaded': True
    }
     
# Endpoint to get predictions
@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):
    
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'response': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)}) 
        
    
    