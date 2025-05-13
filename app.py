import os
import logging
from flask import Flask, render_template, request, jsonify
from prediction_models.student_performance_model import predict_student_performance
from prediction_models.adview_model import predict_adview

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_insightai_secret")

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student-performance')
def student_performance():
    return render_template('student_performance.html')

@app.route('/adview-prediction')
def adview_prediction():
    return render_template('adview_prediction.html')

@app.route('/api/predict-student-performance', methods=['POST'])
def api_predict_student_performance():
    try:
        data = request.get_json()
        
        # Extract features
        gender = data.get('gender')
        race_ethnicity = data.get('race_ethnicity')
        parental_education = data.get('parental_education')
        lunch = data.get('lunch')
        test_preparation = data.get('test_preparation')
        reading_score = int(data.get('reading_score'))
        writing_score = int(data.get('writing_score'))
        
        # Validate input data
        if not all([gender, race_ethnicity, parental_education, lunch, test_preparation]) or \
           not (0 <= reading_score <= 100) or not (0 <= writing_score <= 100):
            return jsonify({"error": "Invalid input data. Please check all fields."}), 400
        
        # Make prediction
        prediction = predict_student_performance(
            gender, race_ethnicity, parental_education, lunch, 
            test_preparation, reading_score, writing_score
        )
        
        return jsonify({"prediction": prediction})
    
    except Exception as e:
        logging.error(f"Error in prediction: {str(e)}")
        return jsonify({"error": f"Prediction error: {str(e)}"}), 500

@app.route('/api/predict-adview', methods=['POST'])
def api_predict_adview():
    try:
        data = request.get_json()
        
        # Extract features
        views = int(data.get('views'))
        likes = int(data.get('likes'))
        dislikes = int(data.get('dislikes'))
        comment_count = int(data.get('comment_count'))
        category = data.get('category')
        
        # Make prediction
        prediction = predict_adview(views, likes, dislikes, comment_count, category)
        
        return jsonify({"prediction": prediction})
    
    except Exception as e:
        logging.error(f"Error in prediction: {str(e)}")
        return jsonify({"error": f"Prediction error: {str(e)}"}), 500

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000, debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

