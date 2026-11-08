from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import random

from services.hunt_generator import generate_hunt

app = Flask(__name__)

app.secret_key = "ecoexplora secret"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/selection")
def selection():
    return render_template("selection.html")

@app.route("/hunt")
def hunt():

    if "hunt" not in session:
        session["hunt"] = generate_hunt(
            session["area"],
            session["habitat"]
        )

    return render_template(
        "hunt.html",
        area=session["area"],
        habitat=session["habitat"],
        hunt=session["hunt"]
    )

@app.route("/new_hunt")
def new_hunt():
    session.pop("hunt", None)

    return redirect(url_for("hunt"))


@app.route("/save_area", methods=["POST"])
def save_area():
    area = request.form.get("area")

    habitat = request.form.get("habitat")

    if not area or not habitat:
        return render_template(
            "selection.html",
            error=True
        )

    session["area"] = area
    session["habitat"] = habitat
    session.pop("hunt", None)

    return redirect(url_for("hunt"))

if __name__ == "__main__":
    app.run(debug=True)