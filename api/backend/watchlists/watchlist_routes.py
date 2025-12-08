from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import db
from mysql.connector import Error

watchlists = Blueprint("watchlists", __name__)


@watchlists.route("/watchlists", methods=["GET"])
def get_watchlists():
    """Get watchlist items with optional user filter."""
    try:
        current_app.logger.info("Starting get_watchlists request")
        cursor = db.get_db().cursor()

        user_id = request.args.get("userID")
        query = """
            SELECT watchlistID, userID, assetID, addedDate
            FROM Watchlist
            WHERE 1=1
        """
        params = []
        if user_id:
            query += " AND userID = %s"
            params.append(int(user_id))

        query += " ORDER BY addedDate DESC"

        current_app.logger.debug(f"Executing query: {query} with params: {params}")
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f"Successfully retrieved {len(rows)} watchlist rows")
        return jsonify({"success": True, "data": rows}), 200
    except Error as e:
        current_app.logger.error(f"Database error in get_watchlists: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@watchlists.route("/watchlists", methods=["POST"])
def create_watchlist_item():
    """Add an asset to a watchlist."""
    try:
        current_app.logger.info("Starting create_watchlist_item request")
        data = request.get_json()
        required_fields = ["userID", "assetID"]
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "error": f"Missing required field: {field}",
                    "status_code": 400
                }), 400

        cursor = db.get_db().cursor()
        insert_sql = """
            INSERT INTO Watchlist (userID, assetID, addedDate)
            VALUES (%s, %s, NOW())
        """
        params = (int(data["userID"]), int(data["assetID"]))
        current_app.logger.debug(f"Executing query: {insert_sql} with params: {params}")
        cursor.execute(insert_sql, params)
        db.get_db().commit()
        new_id = cursor.lastrowid
        cursor.close()

        current_app.logger.info(f"Successfully created watchlist item {new_id}")
        return jsonify({
            "success": True,
            "data": {
                "message": "Asset added to watchlist",
                "watchlistID": new_id
            }
        }), 201
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f"Database error in create_watchlist_item: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@watchlists.route("/watchlists/<int:watchlist_id>", methods=["DELETE"])
def delete_watchlist_item(watchlist_id):
    """Delete a watchlist item."""
    try:
        current_app.logger.info(f"Starting delete_watchlist_item request for ID: {watchlist_id}")
        cursor = db.get_db().cursor()

        cursor.execute("SELECT watchlistID FROM Watchlist WHERE watchlistID = %s", (watchlist_id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "Watchlist item not found",
                "status_code": 404
            }), 404

        cursor.execute("DELETE FROM Watchlist WHERE watchlistID = %s", (watchlist_id,))
        db.get_db().commit()
        cursor.close()

        current_app.logger.info(f"Successfully deleted watchlist item {watchlist_id}")
        return jsonify({
            "success": True,
            "data": {
                "message": "Watchlist item deleted successfully"
            }
        }), 200
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f"Database error in delete_watchlist_item: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500

