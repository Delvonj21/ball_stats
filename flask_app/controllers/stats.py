from flask_app import app
from flask import render_template, flash, redirect, request, session
from flask_app.models.stat import Stat
from flask_app.models.user import User

#! READ
@app.route('/stats')
def get_all_stats():

    if 'user_id' not in session:
        flash("You're not logged in!!")
        return redirect('/')
    
    user_id = session.get('user_id')
    
    return render_template("dashboard.html", stats = Stat.get_stats_for_user(user_id))

#! READ
@app.route("/stat/<int:id>")
def get_one(id):

    if 'user_id' not in session:
        flash("You're not logged in!!")
        return redirect('/')
    
    user_id = session.get('user_id')

    if not user_id:
        return redirect('/')
    
    stat = Stat.get_by_id(id)

    if stat and stat.user_id == user_id:
        return render_template("view_stats.html", stat=stat)
    else:
        return redirect('/stats')


#! CREATE
@app.route("/stat") 
def get_add_stat_form():

    if 'user_id' not in session:
        return redirect('/')
  
    return render_template("add_stats.html")


@app.route("/stat", methods=["POST"])  
def add_stat():

    if 'user_id' not in session:
        flash("You're not logged in!!")
        return redirect('/')
    
    user_id = session['user_id']
    
    data = {
        "points": request.form["points"],
        "assists": request.form["assists"],
        "rebounds": request.form["rebounds"],
        "opponent": request.form["opponent"],
        "date": request.form["date"],
        "user_id": user_id,
    }
    
    
    Stat.add_stat(data)
    return redirect("/stats")  # redirect when data is updated


#! UPDATE
@app.route("/stat/update/<int:id>") 
def update_stat_form(id):
    if 'user_id' not in session:
        flash("You're not logged in!!")
        return redirect('/')

    
    return render_template("edit_stats.html", stat=Stat.get_by_id(id))


@app.route("/stat/update", methods=["POST"])  
def update_stats():

    if 'user_id' not in session:
        flash("You're not logged in!!")
        return redirect('/')
    #Debug messages
    print("Updating stats with form data:", request.form)

    
    result = Stat.update(request.form)

    if result:
        flash("Stats updated successfully", "info")
    else:
        flash("Failed to update stats. Check for errors.", "error")
    
    return redirect("/stats")  # redirect when data is updated


#! DELETE
@app.route("/stat/delete/<int:id>")
def delete(id):

    if 'user_id' not in session:
        flash("You're not logged in!!")
        return redirect('/')
    
    Stat.delete(id)
    flash("Stats deleted", "info")
    return redirect("/stats")



