"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template, request
import requests
import os

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/index')
def index():
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/')
def homepage():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html")

@app.route('/about')
def about():
	return render_template("About Us.html")

@app.route('/contact',methods=("GET", "POST")) 
def submitted():
	username = request.form.get("username")
	subject = request.form.get("subject")
	message = request.form.get("message")
	if (username != "" and subject != "" and message != ""):
		requests.post(
        	os.environ["INFO253_MAILGUN_DOMAIN"],
        	auth=("api", os.environ["INFO253_MAILGUN_USER"]),
        	data={"from": os.environ["INFO253_MAILGUN_FROM_EMAIL"],
              "to": os.environ["INFO253_MAILGUN_TO_EMAIL"],
              "subject": subject,
              "text": message})
	return render_template("Contact Us.html")


@app.route('/blog/8-experiments-in-motivation')
def motivation_post():
	return render_template("8 Experiments in Motivation.html")

@app.route('/blog/a-mindful-shift-of-focus')
def focus_post():
	return render_template("A Mindful Shift of Focus.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def direction_post():
	return render_template("How to Develop an Awesome Sense of Direction.html")

@app.route('/blog/training-to-be-a-good-writer')
def writer_post():
	return render_template("Training to Be a Good Writer.html")

@app.route('/blog/what-productivity-systems-wont-solve')
def productivity_post():
	return render_template("What Productivity Systems Won't Solve.html")

