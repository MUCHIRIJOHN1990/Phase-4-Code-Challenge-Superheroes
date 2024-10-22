from flask import Flask, jsonify, request
from flask_migrate import Migrate

from models import Hero, HeroPower, Power, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)
Migrate(app, db)


@app.route('/heroes', methods=['GET'])
def get_heroes():
    """Get a list of all heroes."""
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(rules=('-hero_powers', )) for hero in heroes])


@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    """Return a hero by ID."""
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'errors': ['Hero not found']}), 404
    return jsonify(hero.to_dict())


@app.route('/powers', methods=['GET'])
def get_powers():
    """Get a list of all powers."""
    powers = Power.query.all()
    return jsonify(
        [power.to_dict(rules=('-hero_powers', )) for power in powers])


@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def get_or_update_power(id):
    """Get a power by ID or update a power."""
    power = Power.query.get(id)
    if not power:
        return jsonify({'errors': ['Power not found']}), 404

    if request.method == 'GET':
        return jsonify(power.to_dict(rules=('-hero_powers', )))

    if request.method == 'PATCH':
        data = request.json

        for key, value in data.items():
            setattr(power, key, value)

        db.session.commit()
        return jsonify(power.to_dict(rules=('-hero_powers', )))


@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    """Create a new hero-power relationship."""
    data = request.json

    # Ensure hero and power exist
    hero = Hero.query.get(data.get('hero_id'))
    power = Power.query.get(data.get('power_id'))

    if not hero:
        return jsonify({'errors': ['Invalid hero_id provided.']}), 400
    if not power:
        return jsonify({'errors': ['Invalid power_id provided.']}), 400

    # Create the new HeroPower relationship
    new_hero_power = HeroPower(strength=data.get('strength'),
                               hero_id=hero.id,
                               power_id=power.id)

    db.session.add(new_hero_power)
    db.session.commit()


if __name__ == '__main__':
    app.run(port=5555, debug=True)
