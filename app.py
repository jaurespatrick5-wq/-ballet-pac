from flask import Flask, render_template, request
import random

app = Flask(__name__)

def ia_prediction():
    teams = ["PSG", "Real Madrid", "Barça", "Man City"]
    score1 = random.randint(0, 4)
    score2 = random.randint(0, 4)
    return f"{random.choice(teams)} {score1} - {score2} {random.choice(teams)}"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        prediction = ia_prediction()
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
