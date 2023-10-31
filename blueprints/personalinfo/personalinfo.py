from flask import Blueprint, render_template, redirect

personalinfo_bp = Blueprint("personalinfo", __name__, template_folder="templates")

@personalinfo_bp.route("/personalinfo")
def personalinfo():
    return "This is the Personal Information page"