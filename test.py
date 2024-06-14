#!/usr/bin/python3
from models import User, Places, Review, Amenity, City, Country


def main():
    # Create a country
    puertorico = Country(name="Puerto Rico")

    # Create a city
    villalba = City(name="Villalba")

    # add city to country list
    puertorico.add_city(villalba)

    # Create users
    charlie = User(email="ccolon@mail.com", password="ch4rl13",
                   first_name="Carlos", last_name="Colon")
    juanjo = User(email="jjjr@mail.com", password="ju4n",
                  first_name="Juan", last_name="Mendez")

    # Create a place
    rancho = Places(
        name="Rancho Rico",
        description="Rancho lejos de todos. Perfecto para relajarte",
        address="carr #149 km 1.5",
        city=villalba.id,
        latitude=40.7128,
        longitude=-74.0060,
        rooms=2,
        bathrooms=1,
        price=100.0,
        max_guests=4
    )

    # Add the place to the user
    charlie.add_place(rancho)

    # Create an amenity
    wifi = Amenity(name="Wi-Fi")

    # Add the amenity to the place
    rancho.add_amenity(wifi)

    # Create a review
    review = Review(user_id=juanjo.id, place_id=rancho.id, text="Bello!", rating=3.5)

    # Add the review to the place
    rancho.add_review(review)

    # Add the review to the user
    juanjo.add_review(review)

    # Print details to verify
    print(f"Country: {puertorico.name}, City: {villalba.name}")
    print(f"{charlie.first_name} {charlie.last_name}, Email: {charlie.email}")
    print(f"ID: {charlie.id}, Owns: {charlie.places[0].name}")
    print(f"Place: {rancho.name}, Host ID: {rancho.host_id}, Host Name: {rancho.host_name}")
    print(f"Amenity: {rancho.amenities[0].name}")
    print(f"{rancho.review[0].user_name} said: {rancho.review[0].text}")


if __name__ == "__main__":
    main()