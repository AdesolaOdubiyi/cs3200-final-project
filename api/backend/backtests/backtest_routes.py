from flask import Blueprint, request, jsonify, current_app
import logging
import random
from datetime import datetime, timedelta

backtests = Blueprint('backtests', __name__)
logger = logging.getLogger('backtests')

@backtests.route('/results/<backtest_id>', methods=['GET'])
def get_backtest_results(backtest_id):
    """
    Get detailed results for a specific backtest.
    """
    # Mock data generation
    dates = [datetime.now() - timedelta(days=x) for x in range(30)]
    dates.reverse()
    
    equity_curve = []
    base_value = 100000
    current_value = base_value
    
    for _ in dates:
        change = random.uniform(-0.02, 0.03)
        current_value *= (1 + change)
        equity_curve.append(current_value)
        
    data = {
        "id": backtest_id,
        "strategy": "Momentum Alpha v2",
        "dates": [d.strftime("%Y-%m-%d") for d in dates],
        "equity_curve": equity_curve,
        "metrics": {
            "total_return": f"{(current_value - base_value) / base_value * 100:.2f}%",
            "sharpe_ratio": 1.85,
            "max_drawdown": "-12.4%",
            "win_rate": "62%"
        },
        "trades": [
            {"date": "2024-10-01", "symbol": "AAPL", "side": "BUY", "price": 175.20, "qty": 100},
            {"date": "2024-10-05", "symbol": "AAPL", "side": "SELL", "price": 182.50, "qty": 100},
            {"date": "2024-10-10", "symbol": "NVDA", "side": "BUY", "price": 450.00, "qty": 50}
        ]
    }
    return jsonify(data), 200


@backtests.route('/backtests', methods=['GET'])
def list_backtests():
    """List backtests (placeholder)."""
    try:
        current_app.logger.info("Starting list_backtests request")
        data = [
            {"backtestID": 1, "name": "Momentum Alpha v2", "status": "COMPLETED"},
            {"backtestID": 2, "name": "Value Tilt", "status": "PENDING"}
        ]
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        current_app.logger.error(f"Error in list_backtests: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@backtests.route('/backtests', methods=['POST'])
def create_backtest():
    """Create a backtest (skeleton)."""
    try:
        current_app.logger.info("Starting create_backtest request")
        payload = request.get_json() or {}
        name = payload.get("name")
        if not name:
            return jsonify({
                "success": False,
                "error": "Missing required field: name",
                "status_code": 400
            }), 400

        response = {
            "message": "Backtest created successfully",
            "backtestID": 999,
            "status": "PENDING",
            "note": "TODO: persist backtest configuration"
        }
        return jsonify({"success": True, "data": response}), 201
    except Exception as e:
        current_app.logger.error(f"Error in create_backtest: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@backtests.route('/backtests/<backtest_id>', methods=['PUT'])
def update_backtest(backtest_id):
    """Update a backtest (skeleton)."""
    try:
        current_app.logger.info(f"Starting update_backtest for ID: {backtest_id}")
        return jsonify({
            "success": True,
            "data": {
                "message": "Backtest update accepted",
                "backtestID": backtest_id,
                "note": "TODO: implement persistence"
            }
        }), 200
    except Exception as e:
        current_app.logger.error(f"Error in update_backtest: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@backtests.route('/backtests/<backtest_id>', methods=['DELETE'])
def delete_backtest(backtest_id):
    """Delete a backtest (skeleton)."""
    try:
        current_app.logger.info(f"Starting delete_backtest for ID: {backtest_id}")
        return jsonify({
            "success": True,
            "data": {
                "message": "Backtest deleted",
                "backtestID": backtest_id,
                "note": "TODO: remove stored results"
            }
        }), 200
    except Exception as e:
        current_app.logger.error(f"Error in delete_backtest: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500