from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import db
from mysql.connector import Error

transactions = Blueprint("transactions", __name__)


@transactions.route("/transactions", methods=["GET"])
def get_transactions():
    """Get transactions with optional portfolio filter."""
    try:
        current_app.logger.info("Starting get_transactions request")
        cursor = db.get_db().cursor()

        portfolio_id = request.args.get("portfolioID")
        query = """
            SELECT transactionID, portfolioID, assetID, transactionType,
                   quantity, price, transactionDate, notes
            FROM Transaction
            WHERE 1=1
        """
        params = []
        if portfolio_id:
            query += " AND portfolioID = %s"
            params.append(int(portfolio_id))

        query += " ORDER BY transactionDate DESC"

        current_app.logger.debug(f"Executing query: {query} with params: {params}")
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()

        current_app.logger.info(f"Successfully retrieved {len(rows)} transactions")
        return jsonify({"success": True, "data": rows}), 200
    except Error as e:
        current_app.logger.error(f"Database error in get_transactions: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500


@transactions.route("/transactions", methods=["POST"])
def create_transaction():
    """Create a new transaction (buy/sell)."""
    try:
        current_app.logger.info("Starting create_transaction request")
        data = request.get_json()
        required_fields = ["portfolioID", "assetID", "transactionType", "quantity", "price"]
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "error": f"Missing required field: {field}",
                    "status_code": 400
                }), 400

        cursor = db.get_db().cursor()
        insert_sql = """
            INSERT INTO Transaction (portfolioID, assetID, transactionType, quantity, price, transactionDate, notes)
            VALUES (%s, %s, %s, %s, %s, COALESCE(%s, NOW()), %s)
        """
        params = (
            int(data["portfolioID"]),
            int(data["assetID"]),
            data["transactionType"],
            float(data["quantity"]),
            float(data["price"]),
            data.get("transactionDate"),
            data.get("notes", "")
        )
        current_app.logger.debug(f"Executing query: {insert_sql} with params: {params}")
        cursor.execute(insert_sql, params)
        db.get_db().commit()
        new_id = cursor.lastrowid
        cursor.close()

        current_app.logger.info(f"Successfully created transaction {new_id}")
        return jsonify({
            "success": True,
            "data": {
                "message": "Transaction recorded successfully",
                "transactionID": new_id,
                "note": "TODO: update positions and cash balances"
            }
        }), 201
    except Error as e:
        db.get_db().rollback()
        current_app.logger.error(f"Database error in create_transaction: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status_code": 500
        }), 500

