from flask import Response, jsonify

def sendError(msg: str, err_code: int = 400, to_home = False) -> tuple[Response, int]:
    data = { "success": False, "message": msg , "tohome": to_home}
    return jsonify(data), err_code

def sendSuccess(content) -> Response:
    data = { "success": True }
    data.update(content)
    return jsonify(data)

