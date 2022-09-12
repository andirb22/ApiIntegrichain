import os
import flask
import json
from controllers import Books_Controller
import controllers.Books_Controller
from models.configDB import app
from flask_cors import CORS

def create_flask_app_with_error_handlers():
    CORS(app, supports_credentials=True)
    @ app.errorhandler(500)
    def handle_exception(exception):
        app.log_exception(exception)
        return app.response_class(
            response=json.dumps({"error": "internal server error"}),
            status=500,
            mimetype="application/json"
        )

    @ app.errorhandler(404)
    def page_not_found(exception):
        return app.response_class(
            response=json.dumps({"error": str(exception)}),
            status=404,
            mimetype="application/json"
        )

    @ app.errorhandler(405)
    def method_not_allow(exception):
        return app.response_class(
            response=json.dumps({"error": str(exception)}),
            status=405,
            mimetype="application/json"
        )
    return app