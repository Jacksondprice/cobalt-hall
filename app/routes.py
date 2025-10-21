from flask import Blueprint, jsonify, request

bp = Blueprint("products", __name__, url_prefix="/api/products")
_ITEMS: list[dict] = []


@bp.get("")
def list_items():
    page = int(request.args.get("page", 1))
    return jsonify(_ITEMS[(page - 1) * 50 : page * 50])


@bp.post("")
def create_item():
    body = request.get_json(force=True)
    if not isinstance(body.get("name"), str):
        return {"error": "name is required"}, 400
    item = {"id": len(_ITEMS) + 1, **body}
    _ITEMS.append(item)
    return item, 201
