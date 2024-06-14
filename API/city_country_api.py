from flask import Blueprint, jsonify, abort, request
from models.class_country import Country
from models.city import City
from persistence.DataManager import DataManager

city_country_bp = Blueprint('city_country', __name__)


@city_country_bp.route('/countries', methods=['GET'])
def get_all_countries():
    """Endpoint para obtener todos los países."""
    countries = Country.all()
    return jsonify(countries), 200


@city_country_bp.route('/countries/<country_code>', methods=['GET'])
def get_country_by_code(country_code):
    """Endpoint para obtener un país por su código de país."""
    country = Country.get(country_code)
    if country is None:
        abort(404, description="Country not found.")
    return jsonify(country), 200


@city_country_bp.route('/countries/<country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    """Endpoint para obtener todas las ciudades de un país específico por su código de país."""
    country = Country.get(country_code)
    if country is None:
        abort(404, description="Country not found.")
    country_cities = [city.to_dict() for city in City.all() 
                      if city.country_code == country_code]
    return jsonify(country_cities), 200


@city_country_bp.route('/cities', methods=['POST'])
def create_city():
    """Endpoint para crear una nueva ciudad."""
    data = request.json
    if data is None:
        abort(400, description="No data provided (must be JSON).")
    fields = ["name", "country_code"]
    for field in fields:
        if field not in data:
            abort(400, description=f"Missing {field}.")
    city = City(data["name"], data["country_code"])
    city.save(city, "City")
    return jsonify(city.to_dict()), 200

@city_country_bp.route('/cities', methods=['GET'])
def get_all_cities():
    """Endpoint para obtener todas las ciudades."""
    cities = DataManager().all_entities("City")
    if cities is None:
        abort(404, description="Cities not found.")
    cities_data = [city for city in cities]
    if cities_data is None:
        abort(404, description="No cities were found")
    return jsonify(cities_data), 200


@city_country_bp.route('/cities/<city_id>', methods=['GET'])
def get_city_by_id(city_id):
    """Endpoint para obtener una ciudad por su ID de ciudad."""
    city = City.reload(city_id, "City")
    if city is None:
        abort(404, description="City not found.")
    return jsonify(city), 200


@city_country_bp.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Endpoint para actualizar la información de una ciudad existente."""
    city = DataManager().get(city_id, "City")
    if city is None:
        abort(404, description="City not found.")
    data = request.json
    if data is None:
        abort(400, description="Invalid request.")
    if "name" in data:
        city.name = data["name"]
    if "country_code" in data:
        city.country_code = data["country_code"]
    DataManager().update(city.id, "City")
    return jsonify(city.to_dict()), 201


@city_country_bp.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Endpoint para eliminar una ciudad específica."""
    city = DataManager().get(city_id, "City")
    if city is None:
        abort(404, description="City not found.")
    DataManager().delete(city_id, "City")
    return jsonify('City deleted successfully'), 200
