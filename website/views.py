from flask import Blueprint, render_template


"""
This file will store all the basic routes (beside authentication) that the user will navigate to

"""

views = Blueprint('views', __name__)

# HOME PAGE
@views.route('/')
def home():
    return render_template("base.html")


