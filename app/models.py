from app import db

class Place(db.Model):
    __tablename__ = "places"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(db.Text)

    address = db.Column(
        db.String(500)
    )

    latitude = db.Column(
        db.Numeric(10, 7)
    )

    longitude = db.Column(
        db.Numeric(10, 7)
    )

    price_min = db.Column(
        db.Numeric(10, 2)
    )

    price_max = db.Column(
        db.Numeric(10, 2)
    )

    rating = db.Column(
        db.Numeric(2, 1)
    )

    opening_hours = db.Column(
        db.String(255)
    )

    image_url = db.Column(
        db.String(500)
    )

    categories = db.relationship(
        "Category",
        secondary="place_categories",
        back_populates="places"
    )

    foods = db.relationship(
        "Food",
        secondary="place_foods",
        back_populates="places"
    )

    tips = db.relationship(
        "PlaceTip",
        back_populates="place",
        cascade="all, delete-orphan"
    )


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    type = db.Column(
        db.String(50),
        nullable=False
    )

    places = db.relationship(
        "Place",
        secondary="place_categories",
        back_populates="categories"
    )


class PlaceCategory(db.Model):
    __tablename__ = "place_categories"

    place_id = db.Column(
        db.Integer,
        db.ForeignKey("places.id"),
        primary_key=True
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        primary_key=True
    )


class Food(db.Model):
    __tablename__ = "foods"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(255),
        nullable=False,
        unique=True
    )

    description = db.Column(
        db.Text
    )

    image_url = db.Column(
        db.String(500)
    )
    
    places = db.relationship(
        "Place",
        secondary="place_foods",
        back_populates="foods"
    )


class PlaceFood(db.Model):
    __tablename__ = "place_foods"

    place_id = db.Column(
        db.Integer,
        db.ForeignKey("places.id"),
        primary_key=True
    )

    food_id = db.Column(
        db.Integer,
        db.ForeignKey("foods.id"),
        primary_key=True
    )


class PlaceTip(db.Model):
    __tablename__ = "place_tips"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    place_id = db.Column(
        db.Integer,
        db.ForeignKey("places.id"),
        nullable=False
    )

    tip_type = db.Column(
        db.String(50),
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    place = db.relationship(
        "Place",
        back_populates="tips"
    )