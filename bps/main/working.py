from flask import Blueprint,render_template,redirect,flash,url_for

Dashboard = Blueprint('Dashboard', __name__)

@Dashboard.route('/dashboard')
def dashboard():
    return render_template("dashboard.html",title = 'Dashboard')