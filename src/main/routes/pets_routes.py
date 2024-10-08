from flask import Blueprint
from flask import Blueprint, jsonify

pet_routes_bp = Blueprint("pets_routes", __name__, url_prefix="/pets")

@pet_routes_bp.route("", methods=["GET"]) 
def list_pets():
    return jsonify({"msg": "hellow word!"})