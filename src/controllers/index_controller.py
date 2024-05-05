from flask import render_template
from app_init import app


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('room.html')
