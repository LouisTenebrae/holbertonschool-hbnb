from flask import Blueprint, jsonify, request, abort
from models.class_reviews import Review
from models.places import Places
from models.users import User
from persistence.DataManager import DataManager


review_bp = Blueprint("review", __name__)


@review_bp.route("/places/<place_id>/reviews", methods=["POST"])
def create_review(place_id):
    """Creates a new review"""
    place = DataManager().get(place_id, "Place")
    if place is None:
        abort(404, description="Places not found")
    data = request.json
    if data is None:
        abort(400, description="Missing data")
    fields = ["user_id", "rating", "review"]
    for field in fields:
        if field not in data:
            abort(400, description=f"Missing {field}")
    user = User.get(data["user_id"], "User")
    if user is None:
        abort(404, description="User not found")
    if user.id == place.host_id:
        abort(400, description="Host cannot review their own place")
    review = Review.create(data["user_id"], place_id, data["text"],
                           data["rating"])
    Places().add_review(review)
    User().add_review(review)
    DataManager().save(review.id, "Review")
    return jsonify(Review.to_dict()), 201


@review_bp.route("/reviews/<review_id>", methods=["GET"])
def get_review(review_id):
    """Gets a review by id"""
    review = Review.reload(review_id, "Review")
    if review is None:
        abort(404, description="Review not found")
    return jsonify(review), 200


@review_bp.route("/reviews/<review_id>", methods=["PUT"])
def update_review(review_id):
    """Update a review"""
    review = Review.get(review_id, "Place")
    if review is None:
        abort(404, description="Review not found")
    comment = request.json["review"]
    rating = request.json["rating"]
    review.comment = comment
    review.rating = rating
    DataManager().update(review.id, "Review")
    return jsonify(review.to_dict), 201


@review_bp.route("/review/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    """Deletes a review"""
    review = Review.get(review_id, "Review")
    if review is None:
        abort(404, description="Review not found")
    DataManager().delete(review.id, "Review")
    return "Review successfuly deleted", 204


@review_bp.route("/places/<place_id>/reviews", methods=["GET"])
def get_place_reviews(place_id):
    """Retrieve all reviews for a specific place"""
    place = Places.get(place_id, "Place")
    if place is None:
        abort(404, description="Places not found")
    if place.reviews is None:
        abort(404, description="Places has no reviews")
    place_reviews = [review.to_dict() for review in place.reviews]
    return jsonify(place_reviews), 200


@review_bp.route("/users/<user_id>/reviews", methods=["GET"])
def get_user_reviews(user_id):
    """Retrieve all reviews written by a specific user"""
    user = User.get(user_id, "User")
    if user is None:
        abort(404, description="User not found")
    if user.reviews is None:
        abort(404, description="User has no reviews")
    user_reviews = [review.to_dict() for review in user.reviews]
    return jsonify(user_reviews), 200
