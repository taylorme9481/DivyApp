from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(trip_id):
    return Data.query.get(trip_id)


class Data(db.Model, UserMixin):
    trip_id = db.Column(db.String, primary_key = True)
    start_time = db.Column(db.DateTime, nullable = True )
    stop_time = db.Column(db.DateTime, nullable = True )
    bike_id = db.Column(db.Integer, nullable = True)
    from_station_id = db.Column(db.Integer, nullable = True)
    from_station_name = db.Column(db.String(150), nullable = True)
    to_station_id = db.Column(db.Integer, nullable = True)
    to_station_name = db.Column(db.String(150), nullable = True)
    user_type = db.Column(db.String(150), nullable = True)
    gender = db.Column(db.String, nullable = True)
    birthday = db.Column(db.String, nullable = True)
    trip_duration = db.Column(db.Integer, nullable = True)

    def __init__(self, trip_id, start_time, stop_time, bike_id, from_station_id, from_station_name, to_station_id, to_station_name, usertype, trip_duration, gender, birthday):
        self.trip_id = trip_id
        self.start_time = start_time
        self.stop_time = stop_time
        self.bike_id = bike_id
        self.from_station_id = from_station_id
        self.from_station_name = from_station_name
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.usertype = usertype
        self.trip_duration = trip_duration
        self.gender = gender
        self.birthday = birthday