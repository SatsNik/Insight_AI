import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import os
import logging
import re

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# File path constants
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, '..', 'attached_assets', 'Adview.csv')

# Dictionary for category mapping
category_mapping = {
    'A': 'Entertainment',
    'B': 'Music',
    'C': 'Education',
    'D': 'Technology',
    'E': 'Lifestyle',
    'F': 'Gaming',
    'G': 'Travel & Events',
    'H': 'Food & Cooking'
}

# Train model on startup
def load_and_train_model():
    try:
        # Load data
        df = pd.read_csv(csv_path)
        
        # Clean data - Remove 'F' values and convert to numeric
        df = df[df.views != 'F']
        df = df[df.likes != 'F']
        df = df[df.dislikes != 'F']
        df = df[df.comment != 'F']
        
        df['views'] = pd.to_numeric(df['views'])
        df['likes'] = pd.to_numeric(df['likes'])
        df['dislikes'] = pd.to_numeric(df['dislikes'])
        df['comment'] = pd.to_numeric(df['comment'])
        df['adview'] = pd.to_numeric(df['adview'])
        
        # Remove videos with adview greater than 2000000 as outliers
        df = df[df['adview'] < 2000000]
        
        # Extract seconds from duration
        def parse_duration(duration):
            minutes = re.search(r'(\d+)M', duration)
            seconds = re.search(r'(\d+)S', duration)
            hours = re.search(r'(\d+)H', duration)
            
            total_seconds = 0
            if hours:
                total_seconds += int(hours.group(1)) * 3600
            if minutes:
                total_seconds += int(minutes.group(1)) * 60
            if seconds:
                total_seconds += int(seconds.group(1))
            
            return total_seconds
        
        # Convert duration to seconds
        df['duration_seconds'] = df['duration'].apply(parse_duration)
        
        # Convert published date to days since epoch
        df['published'] = pd.to_datetime(df['published'])
        df['days_since_epoch'] = (df['published'] - pd.Timestamp('1970-01-01')) // pd.Timedelta('1D')
        
        # Create numerical encoding for category
        le_category = LabelEncoder()
        df['category_encoded'] = le_category.fit_transform(df['category'])
        
        # Select features for the model
        features = ['views', 'likes', 'dislikes', 'comment', 'category_encoded']
        X = df[features]
        y = df['adview']
        
        # Train a Random Forest model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        
        return model, le_category
    
    except Exception as e:
        logging.error(f"Error loading AdView model: {str(e)}")
        return None, None

# Load the model
model, le_category = load_and_train_model()

def predict_adview(views, likes, dislikes, comment_count, category):
    """
    Make a prediction for ad views
    """
    try:
        # Create input features
        category_encoded = le_category.transform([category])[0]
        
        input_data = pd.DataFrame({
            'views': [views],
            'likes': [likes],
            'dislikes': [dislikes],
            'comment': [comment_count],
            'category_encoded': [category_encoded]
        })
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Round to nearest integer
        prediction = round(prediction[0])
        
        # Ensure prediction is not negative
        prediction = max(0, prediction)
        
        return prediction
    
    except Exception as e:
        logging.error(f"AdView prediction error: {str(e)}")
        raise e

def get_category_options():
    """
    Returns the category mapping for UI display
    """
    return category_mapping
