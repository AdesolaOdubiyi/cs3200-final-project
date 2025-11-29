from flask import Blueprint, jsonify, request
from backend.db_connection import db
from mysql.connector import Error
from flask import current_app

# Create a Blueprint for Portfolio routes
portfolios = Blueprint("portfolios", __name__)


@portfolios.route("/portfolios", methods=["GET"])
def get_all_portfolios():
    """
    Retrieve all portfolios with optional filtering by user ID.

    Query parameters:
    - userID (int, optional): Filter portfolios by user ID.

    Returns:
    - JSON: Success response with portfolio data sorted by creation date (most recent first), or error details.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        current_app.logger.info('Starting get_all_portfolios request')
        cursor = db.get_db().cursor()

        # Get query parameters for filtering
        user_id = request.args.get("userID")

        # Prepare the base query
        query = """
        SELECT p.portfolioID, p.Name, p.Description, p.dateCreated, p.userID, u.Name AS userName
        FROM Portfolio p
        JOIN User u ON p.userID = u.UserID
        WHERE 1=1
        """
        params = []

        # Add filter if provided
        if user_id:
            query += " AND p.userID = %s"
            params.append(int(user_id))

        query += " ORDER BY p.dateCreated DESC"

        current_app.logger.debug(f'Executing query: {query} with params: {params}')
        cursor.execute(query, params)
        portfolios_data = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f'Successfully retrieved {len(portfolios_data)} portfolios')
        return jsonify({
            "success": True,
            "data": portfolios_data
        }), 200
    except Error as e:
        current_app.logger.error(f'Database error in get_all_portfolios: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@portfolios.route("/portfolios/<int:portfolio_id>", methods=["GET"])
def get_portfolio(portfolio_id):
    """
    Retrieve detailed information about a specific portfolio including its positions.

    Args:
    - portfolio_id (int): The ID of the portfolio to retrieve.

    Returns:
    - JSON: Success response with portfolio details including name, description, creation date, owner information, and all positions, or error details if not found.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        current_app.logger.info(f'Starting get_portfolio request for ID: {portfolio_id}')
        cursor = db.get_db().cursor()

        # Get portfolio details
        query = """
        SELECT p.portfolioID, p.Name, p.Description, p.dateCreated, p.userID, u.Name AS userName
        FROM Portfolio p
        JOIN User u ON p.userID = u.UserID
        WHERE p.portfolioID = %s
        """
        cursor.execute(query, (portfolio_id,))
        portfolio = cursor.fetchone()

        if not portfolio:
            return jsonify({
                "success": False,
                "error": "Portfolio not found",
                "status_code": 404
            }), 404

        # Get positions for this portfolio
        positions_query = """
        SELECT pos.positionID, pos.portfolioID, pos.assetID, pos.Quantity, pos.AvgCostBasis,
               a.TickerSymbol, a.AssetName, a.AssetType, a.CurrentPrice
        FROM Position pos
        JOIN Asset a ON pos.assetID = a.assetID
        WHERE pos.portfolioID = %s
        """
        cursor.execute(positions_query, (portfolio_id,))
        positions = cursor.fetchall()

        # Add positions to portfolio data
        portfolio["positions"] = positions

        cursor.close()
        current_app.logger.info(f'Successfully retrieved portfolio {portfolio_id}')
        return jsonify({
            "success": True,
            "data": portfolio
        }), 200
    except Error as e:
        current_app.logger.error(f'Database error in get_portfolio: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@portfolios.route("/portfolios", methods=["POST"])
def create_portfolio():
    """
    Create a new portfolio for a user.

    Request body (JSON):
    - Name (str, required): The name of the portfolio.
    - userID (int, required): The ID of the user who owns the portfolio.
    - Description (str, optional): Optional description of the portfolio.

    Returns:
    - JSON: Success response with the new portfolio ID, or error details if validation fails or user not found.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ["Name", "userID"]
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "error": f"Missing required field: {field}",
                    "status_code": 400
                }), 400

        cursor = db.get_db().cursor()

        # Check if user exists
        cursor.execute("SELECT UserID FROM User WHERE UserID = %s", (data["userID"],))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "User not found",
                "status_code": 404
            }), 404

        # Insert new portfolio
        query = """
        INSERT INTO Portfolio (Name, Description, dateCreated, userID)
        VALUES (%s, %s, NOW(), %s)
        """
        description = data.get("Description", "")
        
        cursor.execute(query, (
            data["Name"],
            description,
            data["userID"]
        ))

        db.get_db().commit()
        new_portfolio_id = cursor.lastrowid
        cursor.close()

        current_app.logger.info(f'Successfully created portfolio {new_portfolio_id}')
        return jsonify({
            "success": True,
            "data": {
                "message": "Portfolio created successfully",
                "portfolioID": new_portfolio_id
            }
        }), 201
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f'Database error in create_portfolio: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@portfolios.route("/portfolios/<int:portfolio_id>", methods=["PUT"])
def update_portfolio(portfolio_id):
    """
    Update an existing portfolio's information.

    Args:
    - portfolio_id (int): The ID of the portfolio to update.

    Request body (JSON):
    - Name (str, optional): New name for the portfolio.
    - Description (str, optional): New description for the portfolio.

    Returns:
    - JSON: Success response confirming the update, or error details if portfolio not found or no valid fields provided.

    Raises:
    - DatabaseError: If query execution fails.
    """
    try:
        data = request.get_json()

        # Check if portfolio exists
        cursor = db.get_db().cursor()
        cursor.execute("SELECT * FROM Portfolio WHERE portfolioID = %s", (portfolio_id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "Portfolio not found",
                "status_code": 404
            }), 404

        # Build update query dynamically based on provided fields
        update_fields = []
        params = []
        allowed_fields = ["Name", "Description"]

        for field in allowed_fields:
            if field in data:
                update_fields.append(f"{field} = %s")
                params.append(data[field])

        if not update_fields:
            cursor.close()
            return jsonify({
                "success": False,
                "error": "No valid fields to update",
                "status_code": 400
            }), 400

        params.append(portfolio_id)
        query = f"UPDATE Portfolio SET {', '.join(update_fields)} WHERE portfolioID = %s"

        cursor.execute(query, params)
        db.get_db().commit()
        cursor.close()

        current_app.logger.info(f'Successfully updated portfolio {portfolio_id}')
        return jsonify({
            "success": True,
            "data": {
                "message": "Portfolio updated successfully"
            }
        }), 200
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f'Database error in update_portfolio: {str(e)}')
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500

