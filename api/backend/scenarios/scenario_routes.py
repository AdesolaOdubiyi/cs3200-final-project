from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import db
from mysql.connector import Error

scenarios = Blueprint("scenarios", __name__)


@scenarios.route("/scenarios", methods=["GET"])
def get_scenarios():
    """Get scenario results for a portfolio."""
    try:
        current_app.logger.info("Starting get_scenarios request")
        cursor = db.get_db().cursor()

        portfolio_id = request.args.get("portfolioID")
        query = """
            SELECT scenarioID, name, scenarioType, portfolioID, impactPct, createdAt
            FROM ScenarioResult
            WHERE 1=1
        """
        params = []
        if portfolio_id:
            query += " AND portfolioID = %s"
            params.append(int(portfolio_id))

        query += " ORDER BY createdAt DESC"
        current_app.logger.debug(f"Executing query: {query} with params: {params}")
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f"Successfully retrieved {len(rows)} scenarios")
        return jsonify({"success": True, "data": rows}), 200
    except Error as e:
        current_app.logger.error(f"Database error in get_scenarios: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500

