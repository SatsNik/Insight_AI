# Insight AI[(Live🔗)](https://insight-ai-903t.onrender.com/)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.1-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0-orange)
![Status](https://img.shields.io/badge/Status-Active-green)

A powerful machine learning platform offering predictive analytics for ad viewership and student performance. Insight AI leverages cutting-edge algorithms to deliver actionable intelligence for marketing and educational domains.

**Deployed on Render**: https://insight-ai-903t.onrender.com/
## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Models](#models)
  - [Ad View Prediction](#ad-view-prediction)
  - [Student Performance Prediction](#student-performance-prediction)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Data Format](#data-format)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

Insight AI is a comprehensive analytics platform that harnesses the power of machine learning to derive predictive insights from complex datasets. The platform currently features two robust prediction models:

1. **Ad View Prediction Model**: Predicts user engagement with advertisements based on multiple parameters
2. **Student Performance Prediction Model**: Forecasts academic performance based on historical and behavioral data

This platform offers a user-friendly web interface and robust API endpoints for seamless integration with existing systems.

## ✨ Features

- **Dual Prediction Models**: Specialized algorithms for both marketing and educational domains
- **Interactive Web Interface**: Easy-to-use dashboard for data visualization and prediction
- **REST API**: Simple integration points for external applications
- **Real-time Analysis**: On-the-fly prediction capabilities
- **Data Visualization**: Comprehensive charts and graphs for better understanding
- **Secure**: Data protection and privacy compliance built-in

## 🤖 Models

### Ad View Prediction

Our Ad View prediction model forecasts user engagement with advertisements by analyzing various factors including:

- User demographics
- Browsing history
- Time of day
- Device type
- Ad content type

The model employs a gradient boosting algorithm trained on extensive historical ad view data, achieving an accuracy of 85% in predicting whether a user will view an ad to completion.

**Key Implementation:**

```python
# Ad view prediction sample usage
from prediction_models.adview_model import AdViewPredictor

predictor = AdViewPredictor()
prediction = predictor.predict({
    'user_age': 28,
    'device_type': 'mobile',
    'time_of_day': 'evening',
    'content_category': 'technology',
    'ad_duration': 15
})

print(f"Probability of ad view completion: {prediction:.2f}")
```

### Student Performance Prediction

Our Student Performance prediction model analyzes various academic and behavioral metrics to forecast student performance, including:

- Previous academic scores
- Study habits
- Attendance rate
- Participation metrics
- Demographic factors

Using a random forest classifier, this model achieves 82% accuracy in predicting student performance categories (Excellent, Good, Average, Needs Improvement).

**Key Implementation:**

```python
# Student performance prediction sample usage
from prediction_models.student_performance_model import StudentPerformancePredictor

predictor = StudentPerformancePredictor()
prediction = predictor.predict({
    'previous_score': 78,
    'attendance_rate': 0.92,
    'study_hours_per_week': 15,
    'participation_score': 4,
    'extracurricular_activities': 2
})

print(f"Predicted performance category: {prediction}")
```

## 📂 Project Structure

```
insight-ai/
├── attached_assets/                # Data assets for model training
│   ├── Adview.csv                  # Ad viewership dataset
│   ├── Adview.ipynb                # Jupyter notebook for ad view analysis
│   ├── StudentsPerformance.csv     # Student performance dataset
│   └── performance.ipynb           # Jupyter notebook for performance analysis
├── prediction_models/              # Core ML model implementations
│   ├── adview_model.py             # Ad view prediction model
│   └── student_performance_model.py # Student performance prediction model
├── static/                         # Static web assets
│   ├── css/                        # Stylesheet files
│   │   └── style.css               # Main CSS styles
│   └── js/                         # JavaScript files
│       ├── form-validation.js      # Form validation utilities
│       └── script.js               # Main application scripts
├── templates/                      # HTML templates
│   ├── adview_prediction.html      # Ad view prediction interface
│   ├── index.html                  # Landing page
│   ├── layout.html                 # Base template layout
│   └── student_performance.html    # Student performance interface
├── .gitignore                      # Git ignore file
├── app.py                          # Main Flask application
├── main.py                         # Application entry point
├── models.py                       # Model definitions and interfaces
├── Dockerfile                      # Docker container configuration
├── docker-compose.yml              # Docker Compose services
├── Procfile                        # Process file for deployments
├── pyproject.toml                  # Python project configuration
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🔧 Tech Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask**: Web framework for the application
- **Scikit-Learn**: Machine learning library for prediction models
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib/Seaborn**: Data visualization
- **Jupyter Notebook**

### Frontend
- **HTML5/CSS3**: Structure and styling
- **JavaScript**: Client-side interactions
- **Bootstrap 5**: Responsive design framework
- **Chart.js**: Interactive data visualization

### Deployment
- **Docker**: Containerization
- **Gunicorn**: WSGI HTTP Server

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/insight-ai.git
   cd insight-ai
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the web interface:**
   Open your browser and navigate to `http://localhost:5000`

## 💻 Usage

### Web Interface

1. Navigate to the home page
2. Select either "Ad View Prediction" or "Student Performance Prediction"
3. Fill in the required parameters in the form
4. Click "Generate Prediction" to view results
5. Explore visualizations and insights based on the prediction

### API Usage

**Ad View Prediction API:**
```bash
curl -X POST http://localhost:5000/api/predict/adview \
  -H "Content-Type: application/json" \
  -d '{
    "user_age": 28,
    "device_type": "mobile",
    "time_of_day": "evening",
    "content_category": "technology",
    "ad_duration": 15
  }'
```

**Student Performance Prediction API:**
```bash
curl -X POST http://localhost:5000/api/predict/performance \
  -H "Content-Type: application/json" \
  -d '{
    "previous_score": 78,
    "attendance_rate": 0.92,
    "study_hours_per_week": 15,
    "participation_score": 4,
    "extracurricular_activities": 2
  }'
```

## 📊 API Reference

### Ad View Prediction

**Endpoint:** `/api/predict/adview`
**Method:** `POST`
**Content-Type:** `application/json`

**Request Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| user_age | integer | Age of the user |
| device_type | string | Type of device (desktop, mobile, tablet) |
| time_of_day | string | Time period (morning, afternoon, evening, night) |
| content_category | string | Category of content being viewed |
| ad_duration | integer | Duration of the ad in seconds |

**Response:**
```json
{
  "prediction": 0.78,
  "message": "78% probability of completing the ad view",
  "timestamp": "2025-05-17T14:35:42"
}
```

### Student Performance Prediction

**Endpoint:** `/api/predict/performance`
**Method:** `POST`
**Content-Type:** `application/json`

**Request Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| previous_score | integer | Previous academic score (0-100) |
| attendance_rate | float | Attendance rate (0.0-1.0) |
| study_hours_per_week | integer | Weekly study hours |
| participation_score | integer | Classroom participation (1-5) |
| extracurricular_activities | integer | Number of activities |

**Response:**
```json
{
  "prediction": "Good",
  "confidence": 0.82,
  "details": {
    "projected_score_range": "75-85",
    "improvement_areas": ["participation", "study_consistency"]
  },
  "timestamp": "2025-05-17T14:37:22"
}
```

## 📈 Data Format

### Ad View Dataset Structure

The ad view prediction model is trained on data with the following structure:

```
user_id, age, gender, device_type, time_of_day, content_category, ad_duration, completed_view
```

### Student Performance Dataset Structure

The student performance model is trained on data with the following structure:

```
student_id, gender, age, previous_score, attendance_rate, study_hours_per_week, participation_score, extracurricular_activities, performance_category
```
