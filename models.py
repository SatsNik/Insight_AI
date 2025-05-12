# This file would normally contain database models, but we're not using a database for this application
# Keeping it as a placeholder for potential future expansion

class PredictionLog:
    """
    A class to represent prediction logs if we implement logging in the future
    """
    def __init__(self, model_type, input_data, prediction_result):
        self.model_type = model_type
        self.input_data = input_data
        self.prediction_result = prediction_result
