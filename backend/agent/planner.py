import json
import os

def generate_initial_plan(subjects, hours_per_day, days_left):
    daily_hours_per_subject = round(hours_per_day / len(subjects), 2)

    daily_plan = {}
    for subject in subjects:
        daily_plan[subject] = daily_hours_per_subject

    os.makedirs("data", exist_ok=True)

    with open("data/plan.json", "w") as f:
        json.dump(daily_plan, f, indent=4)

    meta = {
        "days_left": days_left
    }

    with open("data/meta.json", "w") as f:
        json.dump(meta, f, indent=4)

    print("Daily plan generated:", daily_plan)
    return daily_plan



#total available hours calculated and divided equally then this plan is stored in 'agent' memory