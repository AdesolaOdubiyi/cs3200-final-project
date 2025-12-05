from flask import Blueprint, request, jsonify
import logging
import time

ml_models = Blueprint('ml_models', __name__)
logger = logging.getLogger('ml_models')

@ml_models.route('/models', methods=['GET'])
def get_models():
    """
    Get list of all ML models and their status.
    """
    # Mock database query
    models = [
        {"id": "MOD-001", "name": "Price_Forecast_LSTM_v2", "type": "Regression", "accuracy": "87.5%", "status": "Active", "last_trained": "2024-10-24"},
        {"id": "MOD-002", "name": "Sentiment_Analyzer_BERT", "type": "NLP", "accuracy": "92.1%", "status": "Active", "last_trained": "2024-10-20"},
        {"id": "MOD-003", "name": "Risk_Factor_PCA", "type": "Dimensionality Reduction", "accuracy": "N/A", "status": "Training", "last_trained": "In Progress..."},
        {"id": "MOD-004", "name": "Legacy_Price_Model_v1", "type": "Regression", "accuracy": "81.2%", "status": "Deprecated", "last_trained": "2023-12-15"},
        {"id": "MOD-005", "name": "Sector_Rotation_Classifier", "type": "Classification", "accuracy": "76.4%", "status": "Active", "last_trained": "2024-10-25"},
    ]
    return jsonify(models), 200

@ml_models.route('/train', methods=['POST'])
def train_model():
    """
    Initiate a model training job.
    """
    data = request.json
    # Mock training initiation
    job_id = f"TRN-{int(time.time())}"
    return jsonify({
        "job_id": job_id,
        "status": "Started",
        "message": f"Training started for {data.get('model_name', 'New Model')}",
        "estimated_time": "45 minutes"
    }), 200
