from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import db
from mysql.connector import Error

alerts = Blueprint("alerts", __name__)


@alerts.route("/alerts", methods=["GET"])
def get_alerts():
    """Get alerts with optional portfolio and severity filters."""
    try:
        current_app.logger.info("Starting get_alerts request")
        cursor = db.get_db().cursor()

        portfolio_id = request.args.get("portfolioID")
        severity = request.args.get("severity")

        query = """
            SELECT alertID, name, alertType, severity, message, portfolioID, createdAt
            FROM Alert
            WHERE 1=1
        """
        params = []
        if portfolio_id:
            query += " AND portfolioID = %s"
            params.append(int(portfolio_id))
        if severity:
            query += " AND severity = %s"
            params.append(severity)

        query += " ORDER BY createdAt DESC"
        current_app.logger.debug(f"Executing query: {query} with params: {params}")
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f"Successfully retrieved {len(rows)} alerts")
        return jsonify({"success": True, "data": rows}), 200
    except Error as e:
        current_app.logger.error(f"Database error in get_alerts: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@alerts.route("/alerts", methods=["POST"])
def create_alert():
    """Create a new alert rule."""
    try:
        current_app.logger.info("Starting create_alert request")
        data = request.get_json()
        required_fields = ["name", "alertType", "severity", "portfolioID", "message"]
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "error": f"Missing required field: {field}",
                    "status_code": 400
                }), 400

        cursor = db.get_db().cursor()
        insert_sql = """
            INSERT INTO Alert (name, alertType, severity, message, portfolioID, createdAt)
            VALUES (%s, %s, %s, %s, %s, NOW())
        """
        params = (
            data["name"],
            data["alertType"],
            data["severity"],
            data["message"],
            int(data["portfolioID"])
        )
        current_app.logger.debug(f"Executing query: {insert_sql} with params: {params}")
        cursor.execute(insert_sql, params)
        db.get_db().commit()
        new_id = cursor.lastrowid
        cursor.close()

        current_app.logger.info(f"Successfully created alert {new_id}")
        return jsonify({
            "success": True,
            "data": {
                "message": "Alert created successfully",
                "alertID": new_id
            }
        }), 201
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f"Database error in create_alert: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500

