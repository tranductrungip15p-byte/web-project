from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://root:T123@localhost/localtrip?charset=utf8mb4"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.models import Place, PlaceTip, Food

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/test-db")
    def test_db():
        try:
            db.session.execute(db.text("SELECT 1"))
            return "MySQL connection: OK"
        except Exception as e:
            return f"MySQL connection: ERROR - {e}"

    @app.route("/places")
    def places():
        all_places = Place.query.order_by(Place.id).all()

        for place in all_places:
            print(
                place.id,
                repr(place.name),
                [ord(char) for char in place.name]
            )

        return render_template(
            "places.html",
            places=all_places
        )

    @app.route("/places/<int:place_id>")
    def place_detail(place_id):
        place = Place.query.get_or_404(place_id)

        tips = PlaceTip.query.filter_by(
            place_id=place.id
        ).order_by(PlaceTip.id).all()

        return render_template(
            "place_detail.html",
            place=place,
            tips=tips
        )

    @app.route("/foods")
    def foods():
        all_foods = Food.query.order_by(Food.id).all()
        return render_template(
            "foods.html",
            foods=all_foods
        )


    @app.route("/foods/<int:food_id>")
    def food_detail(food_id):
        food = Food.query.get_or_404(food_id)

        return render_template(
            "food_detail.html",
            food=food
        )


    return app