import json
from flask import Flask, render_template
from flask_restful import Api#, Resource
from timetable import get_timetable

APP = Flask(__name__)
API = Api(APP)

@APP.route("/")
def index():
    return render_template("index.html")

@APP.route("/show_timetable/<course_id>", methods=["POST"])
def show_timetable(course_id):
    return json.dumps(get_timetable(course_id), indent=4)

if __name__ == '__main__':
    APP.run(host='localhost', port=80, debug=True)
