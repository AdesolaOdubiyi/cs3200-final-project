from flask import Blueprint, request, jsonify
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
