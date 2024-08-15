from flask import Response, jsonify


def sendError(msg: str, err_code: int) -> tuple[Response, int]:
    data = { "success": False, "error": msg }
    return jsonify(data), err_code

def sendSuccess(content) -> Response:
    data = { "success": True }
    data.update(content)
    return jsonify(data)

