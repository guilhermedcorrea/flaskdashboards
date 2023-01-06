from flask import Blueprint, render_template, redirect

admin_bp = Blueprint("Admin", __name__)


@admin_bp.route("/")
def index():
    return render_template("dashboard.html")