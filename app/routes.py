# app/routes.py: default route page
from app import app
from flask import request, jsonify
import operator

@app.route('/')
@app.route('/index')
@app.route('/methodsGet')
def index():
  return "Hello Demo Flask World!"


@app.route('/predict', methods=["POST"])
def predict():
  input_value = request.form["input_value"]

  message = "Hello " + input_value + " Demo Flask World!"
  return jsonify(
		message = message
	), 200


def get_operator_fn(op):
  return {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
    }[op]


@app.route('/findValue', methods=["POST"])
def findValue():
  x = request.form["x"]
  y = request.form["y"]
  op = request.form["operator"]

  result = get_operator_fn(op)(int(x), int(y))

  return jsonify(
		x = x,
    y = y,
    operator = op,
    result = result
	), 200