from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    super_name = db.Column(db.String(80), nullable=False)
    hero_powers = db.relationship('HeroPower',
                                  backref='hero',
                                  cascade="all, delete")


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    hero_powers = db.relationship('HeroPower',
                                  backref='power',
                                  cascade="all, delete")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if len(value) < 20:
            raise ValueError("Description must be at least 20 characters.")
        self._description = value


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer,
                         db.ForeignKey('powers.id'),
                         nullable=False)

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError(
                "Strength must be 'Strong', 'Weak', or 'Average'.")
        self._strength = value
