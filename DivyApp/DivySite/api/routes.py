from flask import Blueprint, request, jsonify, render_template
from models import db, Data
from flask_login import current_user
import datetime

api = Blueprint('api', __name__, template_folder='api_templates')
import pandas as pd


@api.route('/add', methods=['POST', 'GET'])
def add():
    file = pd.read_csv('DivvyChallenge.csv')
    file_trip = file['trip_id']
    start_time = datetime.datetime.now()
    stop_time = datetime.datetime.now()
    bike_id = 0
    from_station_id = 0
    from_station_name = ""
    to_station_id = 0
    to_station_name = 0
    usertype = ""
    gender = ''
    birthday = ''
    trip_duration = 0

    for trip_id in file_trip:
        user = Data(trip_id, start_time, stop_time, bike_id, from_station_id, from_station_name, to_station_id,
                    to_station_name, usertype, gender, birthday, trip_duration)
        db.session.add(user)

    deebee = Data.query.get(current_user.trip_id)

    file_start = file['starttime']
    file_stop = file['stoptime']
    file_bike = file['bikeid']
    file_from = file['from_station_id']
    file_from_name = file['from_station_name']
    file_to = file['to_station_id']
    file_to_name = file['to_station_name']
    file_user = file['usertype']
    file_gender = file['gender']
    file_birthday = file['birthday']

    for a in file_start:
        a = deebee.start_time
        db.session.add()

    db.session.commit()
    return render_template("add.html")