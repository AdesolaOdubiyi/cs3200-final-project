from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import db
from mysql.connector import Error

audit = Blueprint("audit", __name__)


@audit.route("/events", methods=["GET"])
def get_audit_events():
    """Get audit events with optional filters."""
    try:
        current_app.logger.info("Starting get_audit_events request")
        cursor = db.get_db().cursor()

        start_date = request.args.get("startDate")
        end_date = request.args.get("endDate")
        event_type = request.args.get("eventType")
        user_id = request.args.get("userID")

        query = """
            SELECT auditID, eventType, userID, details, createdAt
            FROM AuditEvent
            WHERE 1=1
        """
        params = []
        if start_date:
            query += " AND createdAt >= %s"
            params.append(start_date)
        if end_date:
            query += " AND createdAt <= %s"
            params.append(end_date)
        if event_type:
            query += " AND eventType = %s"
            params.append(event_type)
        if user_id:
            query += " AND userID = %s"
            params.append(int(user_id))

        query += " ORDER BY createdAt DESC"

        current_app.logger.debug(f"Executing query: {query} with params: {params}")
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f"Successfully retrieved {len(rows)} audit events")
        return jsonify({"success": True, "data": rows}), 200
    except Error as e:
        current_app.logger.error(f"Database error in get_audit_events: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500

