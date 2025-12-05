from flask import Blueprint, request, jsonify
import logging

director = Blueprint('director', __name__)
logger = logging.getLogger('director')

@director.route('/summary', methods=['GET'])
def get_director_summary():
    """
    Get executive summary metrics.
    """
    data = {
        "total_aum": 4250000000,
        "ytd_growth": 12.5,
        "firm_alpha": 3.4,
        "active_strategies": 18,
        "drift_flags": 2
    }
    return jsonify(data), 200

@director.route('/alerts', methods=['GET'])
def get_strategy_alerts():
    """
    Get strategy drift alerts.
    """
    alerts = [
        {
            "fund": "Global Macro Fund",
            "issue": "Cash position > 15% (Target: 5%)",
            "severity": "medium",
            "action": "Review"
        },
        {
            "fund": "Tech Growth Alpha",
            "issue": "Drawdown -15% (Stop: -12%)",
            "severity": "high",
            "action": "Halt"
        }
    ]
    return jsonify(alerts), 200

@director.route('/activity', methods=['GET'])
def get_analyst_activity():
    """
    Get summary of analyst activity.
    """
    activity = {
        "backtests_run": 142,
        "new_models": 8,
        "research_notes": 24
    }
    return jsonify(activity), 200
