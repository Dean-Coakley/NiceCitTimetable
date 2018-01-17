from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) 

@app.route("/")
def index():
    return "twenny wan"

@app.route("/get_timetable/<course_id>")
def get_timetable(course_id):
    return open(course_id + ".json", "r")

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)