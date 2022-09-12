import json
from flask import current_app, abort, request


def serialize_response(response: dict) -> str:
    return json.dumps(response)


def get_request_json() -> dict:
    try:
        return json.loads(request.data)
    except json.decoder.JSONDecodeError:
        error_message = "invalid values in the json"
        response = current_app.response_class(
            response=json.dumps({"error": error_message}),
            status=400,
            mimetype="application/json"
        )
        abort(response)
