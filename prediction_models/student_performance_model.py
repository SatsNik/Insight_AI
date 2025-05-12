import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# File path constants
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, '..', 'attached_assets', 'StudentsPerformance.csv')

# Dictionary mapping for race/ethnicity groups
race_ethnicity_mapping = {
    'group A': 'Asian Students',
    'group B': 'African-American Students',
    'group C': 'Hispanic Students',
    'group D': 'European Students',
    'group E': 'Native American Students'
}

# Dictionary for parental education
parental_education_mapping = {
    "bachelor's degree": "Bachelor's Degree",
    "some college": "Some College",
    "master's degree": "Master's Degree",
    "associate's degree": "Associate's Degree",
    "high school": "High School",
    "some high school": "Some High School"
}

# Train model on startup
def load_and_train_model():
    try:
        # Load data
        df = pd.read_csv(csv_path)
        
        # Prepare features and target
        X = df.drop('math score', axis=1)
        y = df['math score']
        
        # Encode categorical features
        label_encoders = {}
        for column in ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']:
            le = LabelEncoder()
            X[column] = le.fit_transform(X[column])
            label_encoders[column] = le
        
        # Train a Random Forest model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        
        return model, label_encoders
    
    except Exception as e:
        logging.error(f"Error loading model: {str(e)}")
        return None, None

# Load the model
model, label_encoders = load_and_train_model()

def predict_student_performance(gender, race_ethnicity, parental_education, lunch, test_preparation, reading_score, writing_score):
    """
    Make a prediction for student math performance
    """
    try:
        # Create a DataFrame with the input features
        input_data = pd.DataFrame({
            'gender': [gender],
            'race/ethnicity': [race_ethnicity],
            'parental level of education': [parental_education],
            'lunch': [lunch],
            'test preparation course': [test_preparation],
            'reading score': [reading_score],
            'writing score': [writing_score]
        })
        
        # Encode categorical features
        for column, le in label_encoders.items():
            if column in input_data.columns:
                input_data[column] = le.transform(input_data[column])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Round to nearest integer
        prediction = round(prediction[0])
        
        # Ensure prediction is within valid range (0-100)
        prediction = max(0, min(100, prediction))
        
        return prediction
    
    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        raise e

def get_race_ethnicity_options():
    """
    Returns the race/ethnicity mapping for UI display
    """
    return race_ethnicity_mapping

def get_parental_education_options():
    """
    Returns the parental education mapping for UI display
    """
    return parental_education_mapping
