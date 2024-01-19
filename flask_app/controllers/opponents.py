from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.opponent import Opponent

@app.route('/opponents')
def opponents():
  opponents = Opponent.get_all() 
  return render_template("dashboard.html", all_opponents = opponents )

@app.route('/create/opponent', methods=['POST'])
def create_opponent():
  Opponent.save(request.form)
  return redirect('/opponents')