from flask import Blueprint, jsonify, request
from backend.db_connection import db
from mysql.connector import Error
from flask import current_app

# Create a Blueprint for Asset routes
assets = Blueprint("assets", __name__)


@assets.route("/assets", methods=["GET"])
def get_all_assets():
    """
    Retrieve all assets with optional filtering by sector or ticker.

    Query parameters:
    - sectorID (int, optional): Filter by sector ID.
    - ticker (str, optional): Filter by ticker symbol.

    Returns:
    - JSON: Success response with asset data or error details.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        current_app.logger.info('Starting get_all_assets request')
        cursor = db.get_db().cursor()

        # Get query parameters for filtering
        sector_id = request.args.get("sectorID")
        ticker = request.args.get("ticker")

        # Prepare the base query
        query = """
        SELECT a.assetID, a.TickerSymbol, a.AssetName, a.AssetType, a.CurrentPrice, 
               a.sectorID, s.sectorName
        FROM Asset a
        JOIN Sector s ON a.sectorID = s.sectorID
        WHERE 1=1
        """
        params = []

        # Add filters if provided
        if sector_id:
            query += " AND a.sectorID = %s"
            params.append(int(sector_id))
        
        if ticker:
            query += " AND a.TickerSymbol = %s"
            params.append(ticker)

        query += " ORDER BY a.TickerSymbol"

        current_app.logger.debug(f'Executing query: {query} with params: {params}')
        cursor.execute(query, params)
        assets_data = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f'Successfully retrieved {len(assets_data)} assets')
        return jsonify({
            "success": True,
            "data": assets_data
        }), 200
    except Error as e:
        current_app.logger.error(f'Database error in get_all_assets: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@assets.route("/assets/<int:asset_id>", methods=["GET"])
def get_asset(asset_id):
    """
    Retrieve detailed information about a specific asset.

    Args:
    - asset_id (int): The ID of the asset to retrieve.

    Returns:
    - JSON: Success response with asset details including ticker, name, type, price, and sector information, or error details if not found.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        current_app.logger.info(f'Starting get_asset request for ID: {asset_id}')
        cursor = db.get_db().cursor()

        # Get asset details with sector information
        query = """
        SELECT a.assetID, a.TickerSymbol, a.AssetName, a.AssetType, a.CurrentPrice, 
               a.sectorID, s.sectorName, s.sectorDescription
        FROM Asset a
        JOIN Sector s ON a.sectorID = s.sectorID
        WHERE a.assetID = %s
        """
        cursor.execute(query, (asset_id,))
        asset = cursor.fetchone()

        if not asset:
            return jsonify({
                "success": False,
                "error": "Asset not found",
                "status_code": 404
            }), 404

        cursor.close()
        current_app.logger.info(f'Successfully retrieved asset {asset_id}')
        return jsonify({
            "success": True,
            "data": asset
        }), 200
    except Error as e:
        current_app.logger.error(f'Database error in get_asset: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@assets.route("/assets/<int:asset_id>/price-history", methods=["GET"])
def get_price_history(asset_id):
    """
    Retrieve price history for a specific asset with optional date filtering.

    Args:
    - asset_id (int): The ID of the asset to get price history for.

    Query parameters:
    - start_date (str, optional): Filter records from this date onwards (YYYY-MM-DD format).
    - end_date (str, optional): Filter records up to this date (YYYY-MM-DD format).

    Returns:
    - JSON: Success response with price history data sorted by date descending, or error details if asset not found.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        current_app.logger.info(f'Starting get_price_history request for asset ID: {asset_id}')
        cursor = db.get_db().cursor()

        # Check if asset exists
        cursor.execute("SELECT assetID FROM Asset WHERE assetID = %s", (asset_id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "Asset not found",
                "status_code": 404
            }), 404

        # Get query parameters for date filtering
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        # Prepare the base query
        query = """
        SELECT priceID, Date, openPrice, closePrice, Volume, assetID
        FROM PriceHistory
        WHERE assetID = %s
        """
        params = [asset_id]

        # Add date filters if provided
        if start_date:
            query += " AND Date >= %s"
            params.append(start_date)
        
        if end_date:
            query += " AND Date <= %s"
            params.append(end_date)

        query += " ORDER BY Date DESC"

        current_app.logger.debug(f'Executing query: {query} with params: {params}')
        cursor.execute(query, params)
        price_history = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f'Successfully retrieved {len(price_history)} price history records')
        return jsonify({
            "success": True,
            "data": price_history
        }), 200
    except Error as e:
        current_app.logger.error(f'Database error in get_price_history: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@assets.route("/assets/sector/<int:sector_id>", methods=["GET"])
def get_assets_by_sector(sector_id):
    """
    Retrieve all assets that belong to a specific sector.

    Args:
    - sector_id (int): The ID of the sector to retrieve assets for.

    Returns:
    - JSON: Success response with sector information and all assets in that sector, sorted by ticker symbol, or error details if sector not found.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        current_app.logger.info(f'Starting get_assets_by_sector request for sector ID: {sector_id}')
        cursor = db.get_db().cursor()

        # Check if sector exists
        cursor.execute("SELECT sectorID, sectorName FROM Sector WHERE sectorID = %s", (sector_id,))
        sector = cursor.fetchone()
        
        if not sector:
            cursor.close()
            return jsonify({
                "success": False,
                "error": "Sector not found",
                "status_code": 404
            }), 404

        # Get all assets in this sector
        query = """
        SELECT a.assetID, a.TickerSymbol, a.AssetName, a.AssetType, a.CurrentPrice, 
               a.sectorID, s.sectorName
        FROM Asset a
        JOIN Sector s ON a.sectorID = s.sectorID
        WHERE a.sectorID = %s
        ORDER BY a.TickerSymbol
        """
        cursor.execute(query, (sector_id,))
        assets_data = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f'Successfully retrieved {len(assets_data)} assets for sector {sector_id}')
        return jsonify({
            "success": True,
            "data": {
                "sector": sector,
                "assets": assets_data
            }
        }), 200
    except Error as e:
        current_app.logger.error(f'Database error in get_assets_by_sector: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500

