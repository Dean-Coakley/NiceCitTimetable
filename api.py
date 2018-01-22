from flask import Flask, render_template
from flask_restful import Resource, Api
from timetable import get_timetable
import json 

app = Flask(__name__)
api = Api(app) 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/show_timetable/<course_id>", methods=["POST"])
def show_timetable(course_id):
    return json.dumps(get_timetable(course_id), indent=4)

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
