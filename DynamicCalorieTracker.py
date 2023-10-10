from flask import Flask
DynamicCalorieTracker = Flask(__name__)

@DynamicCalorieTracker.route("/")
def home():
    return "Dynamic Calorie Tracker hi"
