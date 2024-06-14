from flask import Blueprint, jsonify, request, abort
from models.places import Places
from models.users import User
from persistence.DataManager import DataManager

place_bp = Blueprint("place", __name__)


@place_bp.route("/places", methods=["POST"])
def create_place():
    """Create a place"""
    data = request.json
    if data is None:
        abort(400, description="Missing data")
    fields = ["name", "description", "longitute", "latitude", "address",
              "price", "city_id", "max_guests", "rooms", "bathrooms",
              "amenities", "host_id"]
    for field in fields:
        if field not in data:
            abort(400, description=f"Missing {fields}")
    host = User.get(data["host_id"], "User")
    if host not in data:
        abort(400, description=f"User not found")
    place = Places(data["name"], data["description"], data["address"],
                    data["city_id"], data["latitude"], data["longitude"],
                    data["rooms"], data["bathrooms"], data["price"],
                    data["max_guests"])
    place.host_id = data["host_id"]

    for amenity in data["amenity"]:
        try:
            place.add_amenity(amenity)
        except:
            abort(400, description="Failed to add amenity")
        User().add_place(place)
        DataManager().save(place.id)
    return jsonify(place.to_dict()), 201


@place_bp.route("/places", methods=["GET"])
def get_places():
    """get all places"""
    places = DataManager().all_entities("Place")
    if places is None:
        abort(404, description="No places found")
    data = [place for place in places]
    return jsonify(data), 200


@place_bp.route("/places/<place_id>", methods=["GET"])
def get_place(place_id):
    """get a place"""
    place = DataManager().reload(place_id, "Place")
    if place is None:
        abort(404, description="Places not found")
    return jsonify(place), 200


@place_bp.route("/places/<place_id>", methods=["PUT"])
def update_place(place_id):
    """update a place"""
    place = DataManager().get(place_id, "Place")
    if place is None:
        abort(404, description="Places not found")
    data = request.json
    if data is None:
        abort(400, description="Missing data")
    for key, value in data.items():
        if key in data and key is not place_id:
            setattr(place, key, value)
    DataManager().save(place_id, "Place")
    return jsonify(place.to_dict()), 201


@place_bp.route("/places/<place_id>", methods=["DELETE"])
def delete_place(place_id):
    """delete a place"""
    place = DataManager().get(place_id, "Place")
    if place is None:
        abort(404, description="Places not found")
    host = User.get(place.host_id, "User")
    host.places.remove(place)
    DataManager().delete(place_id, "Place")
    return "Places deleted", 204
