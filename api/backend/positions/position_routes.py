from flask import Blueprint, jsonify, request
from backend.db_connection import db
from mysql.connector import Error
from flask import current_app

# Create a Blueprint for Position routes
positions = Blueprint("positions", __name__)


@positions.route("/positions", methods=["GET"])
def get_all_positions():
    """
    Retrieve all positions with optional filtering by portfolio ID.

    Query parameters:
    - portfolioID (int, optional): Filter positions by portfolio ID.

    Returns:
    - JSON: Success response with position data sorted by portfolio ID and ticker symbol, or error details.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        current_app.logger.info('Starting get_all_positions request')
        cursor = db.get_db().cursor()

        # Get query parameters for filtering
        portfolio_id = request.args.get("portfolioID")

        # Prepare the base query
        query = """
        SELECT pos.positionID, pos.portfolioID, pos.assetID, pos.Quantity, pos.AvgCostBasis,
               a.TickerSymbol, a.AssetName, a.AssetType, a.CurrentPrice,
               p.Name AS portfolioName
        FROM Position pos
        JOIN Asset a ON pos.assetID = a.assetID
        JOIN Portfolio p ON pos.portfolioID = p.portfolioID
        WHERE 1=1
        """
        params = []

        # Add filter if provided
        if portfolio_id:
            query += " AND pos.portfolioID = %s"
            params.append(int(portfolio_id))

        query += " ORDER BY pos.portfolioID, a.TickerSymbol"

        current_app.logger.debug(f'Executing query: {query} with params: {params}')
        cursor.execute(query, params)
        positions_data = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f'Successfully retrieved {len(positions_data)} positions')
        return jsonify({
            "success": True,
            "data": positions_data
        }), 200
    except Error as e:
        current_app.logger.error(f'Database error in get_all_positions: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@positions.route("/positions/<int:position_id>", methods=["GET"])
def get_position(position_id):
    """
    Retrieve detailed information about a specific position.

    Args:
    - position_id (int): The ID of the position to retrieve.

    Returns:
    - JSON: Success response with position details including quantity, average cost basis, and related asset and portfolio information, or error details if not found.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        current_app.logger.info(f'Starting get_position request for ID: {position_id}')
        cursor = db.get_db().cursor()

        # Get position details with asset and portfolio information
        query = """
        SELECT pos.positionID, pos.portfolioID, pos.assetID, pos.Quantity, pos.AvgCostBasis,
               a.TickerSymbol, a.AssetName, a.AssetType, a.CurrentPrice,
               p.Name AS portfolioName, p.Description AS portfolioDescription
        FROM Position pos
        JOIN Asset a ON pos.assetID = a.assetID
        JOIN Portfolio p ON pos.portfolioID = p.portfolioID
        WHERE pos.positionID = %s
        """
        cursor.execute(query, (position_id,))
        position = cursor.fetchone()

        if not position:
            return jsonify({
                "success": False,
                "error": "Position not found",
                "status_code": 404
            }), 404

        cursor.close()
        current_app.logger.info(f'Successfully retrieved position {position_id}')
        return jsonify({
            "success": True,
            "data": position
        }), 200
    except Error as e:
        current_app.logger.error(f'Database error in get_position: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@positions.route("/positions", methods=["POST"])
def create_position():
    """
    Create a new position in a portfolio.

    Request body (JSON):
    - portfolioID (int, required): The ID of the portfolio to add the position to.
    - assetID (int, required): The ID of the asset for this position.
    - Quantity (int/float, required): The quantity of the asset held.
    - AvgCostBasis (float, required): The average cost basis for this position.

    Returns:
    - JSON: Success response with the new position ID, or error details if validation fails, portfolio/asset not found, or position already exists.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ["portfolioID", "assetID", "Quantity", "AvgCostBasis"]
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "error": f"Missing required field: {field}",
                    "status_code": 400
                }), 400

        cursor = db.get_db().cursor()

        # Check if portfolio exists
        cursor.execute("SELECT portfolioID FROM Portfolio WHERE portfolioID = %s", (data["portfolioID"],))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "Portfolio not found",
                "status_code": 404
            }), 404

        # Check if asset exists
        cursor.execute("SELECT assetID FROM Asset WHERE assetID = %s", (data["assetID"],))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "Asset not found",
                "status_code": 404
            }), 404

        # Check if position already exists (unique constraint on portfolioID + assetID)
        cursor.execute(
            "SELECT positionID FROM Position WHERE portfolioID = %s AND assetID = %s",
            (data["portfolioID"], data["assetID"])
        )
        if cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "Position already exists for this portfolio and asset",
                "status_code": 400
            }), 400

        # Insert new position
        query = """
        INSERT INTO Position (portfolioID, assetID, Quantity, AvgCostBasis)
        VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(query, (
            data["portfolioID"],
            data["assetID"],
            data["Quantity"],
            float(data["AvgCostBasis"])
        ))

        db.get_db().commit()
        new_position_id = cursor.lastrowid
        cursor.close()

        current_app.logger.info(f'Successfully created position {new_position_id}')
        return jsonify({
            "success": True,
            "data": {
                "message": "Position created successfully",
                "positionID": new_position_id
            }
        }), 201
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f'Database error in create_position: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@positions.route("/positions/<int:position_id>", methods=["PUT"])
def update_position(position_id):
    """
    Update an existing position's information.

    Args:
    - position_id (int): The ID of the position to update.

    Request body (JSON):
    - Quantity (int/float, optional): New quantity for the position.
    - AvgCostBasis (float, optional): New average cost basis for the position.

    Returns:
    - JSON: Success response confirming the update, or error details if position not found or no valid fields provided.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        data = request.get_json()

        # Check if position exists
        cursor = db.get_db().cursor()
        cursor.execute("SELECT * FROM Position WHERE positionID = %s", (position_id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "Position not found",
                "status_code": 404
            }), 404

        # Build update query dynamically based on provided fields
        update_fields = []
        params = []
        allowed_fields = ["Quantity", "AvgCostBasis"]

        for field in allowed_fields:
            if field in data:
                update_fields.append(f"{field} = %s")
                if field == "AvgCostBasis":
                    params.append(float(data[field]))
                else:
                    params.append(data[field])

        if not update_fields:
            cursor.close()
            return jsonify({
                "success": False,
                "error": "No valid fields to update",
                "status_code": 400
            }), 400

        params.append(position_id)
        query = f"UPDATE Position SET {', '.join(update_fields)} WHERE positionID = %s"

        cursor.execute(query, params)
        db.get_db().commit()
        cursor.close()

        current_app.logger.info(f'Successfully updated position {position_id}')
        return jsonify({
            "success": True,
            "data": {
                "message": "Position updated successfully"
            }
        }), 200
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f'Database error in update_position: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@positions.route("/positions/<int:position_id>", methods=["DELETE"])
def delete_position(position_id):
    """
    Delete a position from the system.

    Args:
    - position_id (int): The ID of the position to delete.

    Returns:
    - JSON: Success response confirming the deletion, or error details if position not found.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        current_app.logger.info(f'Starting delete_position request for ID: {position_id}')
        cursor = db.get_db().cursor()

        # Check if position exists
        cursor.execute("SELECT * FROM Position WHERE positionID = %s", (position_id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "Position not found",
                "status_code": 404
            }), 404

        # Delete the position
        cursor.execute("DELETE FROM Position WHERE positionID = %s", (position_id,))
        db.get_db().commit()
        cursor.close()

        current_app.logger.info(f'Successfully deleted position {position_id}')
        return jsonify({
            "success": True,
            "data": {
                "message": "Position deleted successfully"
            }
        }), 200
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f'Database error in delete_position: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500

