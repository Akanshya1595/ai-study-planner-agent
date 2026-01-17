def analyze_performance(daily_plan, actual_hours):
    analysis = {}
    subjects = list(daily_plan.keys())

    for i, subject in enumerate(subjects):
        planned = daily_plan[subject]
        actual = actual_hours[i]

        difficulty = round(actual / planned, 2)
        analysis[subject] = difficulty

    return analysis

