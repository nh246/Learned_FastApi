import pickle
import pandas as pd



# import the model
with open('./model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# model version 
MODEL_VERSION = '1.0.0'

# get clases labels from model 
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    
    # predict the class 
    predicted_class = model.predict(df)[0]
    
    # get probabilities
    probabilities = model.predict_proba(df)[0]
    confidence= max(probabilities)
    
    # create mapping of class labels and probabilities
    class_probs = dict(zip(class_labels,map(lambda x: round(x,4), probabilities)))
    
     
   
    return {
        'predicted_catagory': predicted_class,
        'confidence': round(confidence,4),
        'class_probabilities': class_probs
    }