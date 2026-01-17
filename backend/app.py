from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from agent.planner import generate_initial_plan
from agent.analyzer import analyze_performance
from agent.decision import reallocate_time
import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "../frontend"),
    static_url_path=""
)

CORS(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/plan", methods=["POST"])
def plan():
    data = request.get_json()
    print("Received data:", data)  # DEBUG

    subjects = data["subjects"]
    hours_per_day = data["hours_per_day"]
    days_left = data["days_left"]

    plan = generate_initial_plan(subjects, hours_per_day, days_left)

    # Save metadata (agent memory)
    meta = {
        "days_left": days_left
    }

    with open("data/meta.json", "w") as f:
        json.dump(meta, f)

    return jsonify(plan)

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json()
    actual_hours = data["actual_hours"]

    # Load daily plan
    with open("data/plan.json", "r") as f:
        plan = json.load(f)

    # Load metadata
    with open("data/meta.json", "r") as f:
        meta = json.load(f)

    days_left = meta["days_left"]

    if days_left <= 1:
        return jsonify({"message": "Study period completed!"})

    # Analyze today
    analysis = analyze_performance(plan, actual_hours)

    # Decide next day's plan
    updated_plan = reallocate_time(plan, analysis)

    # One day passes
    meta["days_left"] = days_left - 1

    # Save updated state
    with open("data/plan.json", "w") as f:
        json.dump(updated_plan, f, indent=4)

    with open("data/meta.json", "w") as f:
        json.dump(meta, f, indent=4)

    response = {
        "days_left": meta["days_left"],
        "analysis": analysis,
        "next_day_plan": updated_plan
    }

    print("Agent state:", response)
    return jsonify(response)

@app.route("/next-day", methods=["POST"])
def next_day():
    with open("data/plan.json", "r") as f:
        plan = json.load(f)

    with open("data/meta.json", "r") as f:
        meta = json.load(f)

    if meta["days_left"] <= 0:
        return jsonify({"message": "Study plan completed!"})

    response = {
        "days_left": meta["days_left"],
        "today_plan": plan
    }

    return jsonify(response)





if __name__ == "__main__":
    app.run(debug=True)


    
#An API endpoint for when frontend sends json data, the planner agent generates a plan and it is sent back as json to frontend