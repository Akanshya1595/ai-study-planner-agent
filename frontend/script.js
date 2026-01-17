function generatePlan() {
    const days = document.getElementById("days").value;
    const hours = document.getElementById("hours").value;
    const subjectsRaw = document.getElementById("subjects").value;

    const subjects = subjectsRaw.split(",").map(s => s.trim());

    console.log("Sending data:", {
        days_left: days,
        hours_per_day: hours,
        subjects: subjects
    });

    fetch("/plan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            days_left: Number(days),
            hours_per_day: Number(hours),
            subjects: subjects
        })
    })
    .then(res => res.json())
    .then(data => {
        let output = "";
        for (let subject in data) {
            output += `${subject}: ${data[subject]} hours\n`;
        }
        document.getElementById("result").textContent = output;
    })
    .catch(err => {
        console.error(err);
        alert("Backend error – check console");
    });
}

function submitFeedback() {
    const feedbackRaw = document.getElementById("feedback").value;
    const feedbackValues = feedbackRaw.split(",").map(v => Number(v.trim()));

    fetch("/feedback", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            actual_hours: feedbackValues
        })
    })
    .then(res => res.json())
    .then(data => {
        let output = "Difficulty Analysis (Today):\n";
        for (let subject in data.analysis) {
            output += `${subject}: ${data.analysis[subject]}\n`;
        }

        let nextPlan = "Tomorrow's Study Plan:\n";
        for (let subject in data.next_day_plan) {
            nextPlan += `${subject}: ${data.next_day_plan[subject]} hours\n`;
        }

        output += `\nDays left: ${data.days_left}`;

        document.getElementById("analysis").textContent = output;
        document.getElementById("nextPlan").textContent = nextPlan;
    })


    .catch(err => {
        console.error(err);
        alert("Feedback processing failed");
    });
}

function startNextDay() {
    fetch("/next-day", {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            return;
        }

        let output = "";
        for (let subject in data.today_plan) {
            output += `${subject}: ${data.today_plan[subject]} hours\n`;
        }

        document.getElementById("todayPlan").textContent =
            `Day starts (Days left: ${data.days_left})\n\n` + output;
    })
    .catch(err => {
        console.error(err);
        alert("Failed to load next day");
    });
}



