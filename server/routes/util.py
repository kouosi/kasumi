from flask import Response, jsonify


def sendError(msg: str, err_code: int = 400) -> tuple[Response, int]:
    data = { "success": False, "error": msg }
    return jsonify(data), err_code

def sendSuccess(content) -> Response:
    data = { "success": True }
    data.update(content)
    return jsonify(data)

