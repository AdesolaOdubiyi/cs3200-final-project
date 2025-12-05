from flask import Blueprint, request, jsonify
import logging

macro = Blueprint('macro', __name__)
logger = logging.getLogger('macro')

@macro.route('/indicators', methods=['GET'])
def get_indicators():
    """
    Get list of available economic indicators.
    """
    indicators = [
        {"id": "GDP", "name": "GDP (Current US$)"},
        {"id": "CPI", "name": "Inflation, consumer prices (annual %)"},
        {"id": "POP", "name": "Population, total"},
        {"id": "CO2", "name": "CO2 emissions (metric tons per capita)"}
    ]
    return jsonify(indicators), 200

@macro.route('/data/<indicator_id>', methods=['GET'])
def get_macro_data(indicator_id):
    """
    Get data for a specific indicator.
    """
    year = request.args.get('year', 2022)
    # In a real app, query DB or external API here
    data = {
        "indicator": indicator_id,
        "year": year,
        "values": [
            {"country": "USA", "value": 25.46},
            {"country": "CHN", "value": 17.96},
            {"country": "JPN", "value": 4.23}
        ]
    }
    return jsonify(data), 200
