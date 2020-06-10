# app/routes.py: default route page
from app import app
from flask import request, jsonify

@app.route('/')
@app.route('/index')
def index():
  return "Hello Demo Flask World!"


@app.route('/predict', methods=["POST"])
def predict():
  input_value = request.form["input_value"]

  message = "Hello " + input_value + " Demo Flask World!"
  return jsonify(
		message = message
	), 200