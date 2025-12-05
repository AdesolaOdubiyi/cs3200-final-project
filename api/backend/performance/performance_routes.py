from flask import Blueprint, request, jsonify
import logging

performance = Blueprint('performance', __name__)
logger = logging.getLogger('performance')

@performance.route('/firm/summary', methods=['GET'])
def get_firm_summary():
    """
    Get high-level firm performance metrics.
    """
    data = {
        "total_aum": 4250000000,
        "ytd_return": 12.5,
        "active_strategies": 18,
        "funds": [
            {"name": "Global Macro Fund", "aum": 1200000000, "return": 8.4, "risk": "Medium"},
            {"name": "Tech Growth Alpha", "aum": 850000000, "return": 18.2, "risk": "High"},
            {"name": "Income & Yield", "aum": 600000000, "return": 4.5, "risk": "Low"},
            {"name": "Emerging Markets", "aum": 450000000, "return": -2.1, "risk": "High"}
        ]
    }
    return jsonify(data), 200
