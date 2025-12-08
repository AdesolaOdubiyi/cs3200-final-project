from flask import Flask
from dotenv import load_dotenv
import os
import logging
from logging.handlers import RotatingFileHandler

from backend.db_connection import db
from backend.simple.simple_routes import simple_routes
from backend.portfolios.portfolio_routes import portfolios
from backend.assets.asset_routes import assets
from backend.positions.position_routes import positions
from backend.macro.macro_routes import macro
from backend.geo.geo_routes import geo
from backend.backtests.backtest_routes import backtests
from backend.performance.performance_routes import performance
from backend.director.director_routes import director
from backend.system.system_routes import system
from backend.transactions.transaction_routes import transactions
from backend.scenarios.scenario_routes import scenarios
from backend.alerts.alert_routes import alerts
from backend.users.user_routes import users
from backend.watchlists.watchlist_routes import watchlists
from backend.audit.audit_routes import audit


def create_app():
    """
    Create and configure the Flask application.

    Sets up database connections, loads environment variables from .env file,
    registers all route blueprints, and configures logging. This is the main
    factory function for creating the Flask app instance.

    Returns:
    - Flask: Configured Flask application instance.

    Raises:
    - EnvironmentError: If required environment variables are missing.
    - DatabaseError: If database connection initialization fails.
    """
    app = Flask(__name__)

    app.logger.setLevel(logging.DEBUG)
    app.logger.info("API startup")

    # Configure file logging if needed
    #   Uncomment the code in the setup_logging function
    # setup_logging(app)

    # Load environment variables
    # This function reads all the values from inside
    # the .env file (in the parent folder) so they
    # are available in this file.  See the MySQL setup
    # commands below to see how they're being used.
    load_dotenv()

    # secret key that will be used for securely signing the session
    # cookie and can be used for any other security related needs by
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # # these are for the DB object to be able to connect to MySQL.
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config["MYSQL_DATABASE_USER"] = os.getenv("DB_USER").strip()
    app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_ROOT_PASSWORD").strip()
    app.config["MYSQL_DATABASE_HOST"] = os.getenv("DB_HOST").strip()
    app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("DB_PORT").strip())
    app.config["MYSQL_DATABASE_DB"] = os.getenv(
        "DB_NAME"
    ).strip()  # Change this to your DB name

    # Initialize the database object with the settings above.
    app.logger.info("current_app(): starting the database connection")
    db.init_app(app)

    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.logger.info("create_app(): registering blueprints with Flask app object.")
    app.register_blueprint(simple_routes)
    app.register_blueprint(portfolios, url_prefix="/portfolio")
    app.register_blueprint(assets, url_prefix="/asset")
    app.register_blueprint(positions, url_prefix="/position")
    app.register_blueprint(macro, url_prefix="/macro")
    app.register_blueprint(geo, url_prefix="/geo")
    app.register_blueprint(backtests, url_prefix="/backtest")
    app.register_blueprint(performance, url_prefix="/performance")
    app.register_blueprint(director, url_prefix="/director")
    app.register_blueprint(system, url_prefix="/system")
    app.register_blueprint(transactions, url_prefix="/transaction")
    app.register_blueprint(scenarios, url_prefix="/scenario")
    app.register_blueprint(alerts, url_prefix="/alert")
    app.register_blueprint(users, url_prefix="/user")
    app.register_blueprint(watchlists, url_prefix="/watchlist")
    app.register_blueprint(audit, url_prefix="/audit")

    # Don't forget to return the app object
    return app


def setup_logging(app):
    """
    Configure logging for the Flask application.

    Sets up both file and console logging handlers. Currently commented out
    but can be enabled when you need to log to files. The function is ready
    to use when uncommented.

    Args:
    - app (Flask): The Flask application instance to configure logging for.

    Returns:
    - None

    Note:
    - This function is currently a placeholder. Uncomment the code inside
      to enable file and console logging handlers.
    """
    # if not os.path.exists('logs'):
    #     os.mkdir('logs')

    ## Set up FILE HANDLER for all levels
    # file_handler = RotatingFileHandler(
    #     'logs/api.log',
    #     maxBytes=10240,
    #     backupCount=10
    # )
    # file_handler.setFormatter(logging.Formatter(
    #     '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    # ))

    # Make sure we are capturing all levels of logging into the log files.
    # file_handler.setLevel(logging.DEBUG)  # Capture all levels in file
    # app.logger.addHandler(file_handler)

    # ## Set up CONSOLE HANDLER for all levels
    # console_handler = logging.StreamHandler()
    # console_handler.setFormatter(logging.Formatter(
    #     '%(asctime)s %(levelname)s: %(message)s'
    # ))
    # Debug level capture makes sure that all log levels are captured
    # console_handler.setLevel(logging.DEBUG)
    # app.logger.addHandler(console_handler)
    pass
