#Logic: If difficulty score:
# Greater than or equal to 1.5 then allocate 20% more time
# 1.2-1.49 then allocate 10% more time
# 0.8 to 1.19 then make no change 
# Less than 0.8 then decrease 10% time for the subject 

def reallocate_time(plan, difficulty):
    updated_plan = {}

    for subject, current_time in plan.items():
        score = difficulty.get(subject, 1.0)

        if score >= 1.5:
            new_time = current_time * 1.2
        elif score >= 1.2:
            new_time = current_time * 1.1
        elif score < 0.8:
            new_time = current_time * 0.9
        else:
            new_time = current_time

        updated_plan[subject] = round(new_time, 2)

    return updated_plan
