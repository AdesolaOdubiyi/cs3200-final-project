from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import db
from mysql.connector import Error

users = Blueprint("users", __name__)


@users.route("/users", methods=["GET"])
def get_users():
    """Get all users."""
    try:
        current_app.logger.info("Starting get_users request")
        cursor = db.get_db().cursor()

        query = """
            SELECT UserID, Name, Email, Role, lastLogin
            FROM User
            ORDER BY Name
        """
        current_app.logger.debug(f"Executing query: {query}")
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f"Successfully retrieved {len(rows)} users")
        return jsonify({"success": True, "data": rows}), 200
    except Error as e:
        current_app.logger.error(f"Database error in get_users: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@users.route("/users/<int:user_id>/role", methods=["PUT"])
def update_user_role(user_id):
    """Update a user's role."""
    try:
        current_app.logger.info(f"Starting update_user_role request for ID: {user_id}")
        data = request.get_json()
        new_role = data.get("role")
        if not new_role:
            return jsonify({
                "success": False,
                "error": "Missing required field: role",
                "status_code": 400
            }), 400

        cursor = db.get_db().cursor()
        cursor.execute("SELECT UserID FROM User WHERE UserID = %s", (user_id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({
                "success": False,
                "error": "User not found",
                "status_code": 404
            }), 404

        update_sql = "UPDATE User SET Role = %s WHERE UserID = %s"
        params = (new_role, user_id)
        current_app.logger.debug(f"Executing query: {update_sql} with params: {params}")
        cursor.execute(update_sql, params)
        db.get_db().commit()
        cursor.close()

        current_app.logger.info(f"Successfully updated role for user {user_id}")
        return jsonify({
            "success": True,
            "data": {
                "message": "User role updated successfully"
            }
        }), 200
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f"Database error in update_user_role: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@users.route("/users/<int:user_id>/activity", methods=["GET"])
def get_user_activity(user_id):
    """Get user activity logs."""
    try:
        current_app.logger.info(f"Starting get_user_activity request for ID: {user_id}")
        cursor = db.get_db().cursor()

        start_date = request.args.get("startDate")
        end_date = request.args.get("endDate")

        query = """
            SELECT activityID, userID, activityType, details, createdAt
            FROM UserActivity
            WHERE userID = %s
        """
        params = [user_id]
        if start_date:
            query += " AND createdAt >= %s"
            params.append(start_date)
        if end_date:
            query += " AND createdAt <= %s"
            params.append(end_date)

        query += " ORDER BY createdAt DESC"

        current_app.logger.debug(f"Executing query: {query} with params: {params}")
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f"Successfully retrieved {len(rows)} activity rows for user {user_id}")
        return jsonify({"success": True, "data": rows}), 200
    except Error as e:
        current_app.logger.error(f"Database error in get_user_activity: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500

