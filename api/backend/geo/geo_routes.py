from flask import Blueprint, request, jsonify
import logging

geo = Blueprint('geo', __name__)
logger = logging.getLogger('geo')

@geo.route('/assets', methods=['GET'])
def get_asset_locations():
    """
    Get geospatial coordinates of assets.
    """
    region = request.args.get('region', 'Global')
    # Mock data
    assets = [
        {"id": 1, "lat": 37.77, "lon": -122.41, "value": 500, "type": "Factory"},
        {"id": 2, "lat": 40.71, "lon": -74.00, "value": 1200, "type": "Office"},
        {"id": 3, "lat": 51.50, "lon": -0.12, "value": 800, "type": "Hub"}
    ]
    return jsonify(assets), 200

@geo.route('/routes', methods=['GET'])
def get_supply_routes():
    """
    Get supply chain routes.
    """
    routes = [
        {"start": "SFO", "end": "TYO", "volume": 100},
        {"start": "NYC", "end": "LON", "volume": 250}
    ]
    return jsonify(routes), 200
