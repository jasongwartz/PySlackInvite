#webapp

import bottle as bt
from bottle import route, run, template, request, get, post, static_file
from bottle import url
import os

import invite

app = bt.Bottle()


@app.route('/static/css/<filename>')
def server_static(filename):
    return static_file(filename, root='static/css')

@app.route('/static/fonts/<filename>')
def server_font(filename):
    return static_file(filename, root='static/fonts')

@app.route('/static/css/images/<filename>')
def server_cssimg(filename):
    return static_file(filename, root='static/css/images')

@app.route('/images/<filename>')
def server_img(filename):
    return static_file(filename, root='static/images')


@app.route("/")
def undeclared_index():
	return template("templates/index", text="Add Yourself", get_url=url)

@app.post("/send")
def submit():
	email = request.forms.get("email")
	firstname = request.forms.get("firstname")
	lastname = request.forms.get("lastname")
	access = request.forms.get("access")
	text = invite.invite(email, firstname, lastname, access)
	return template("templates/confirm", text=text)



run(app, reloader=True, host="0.0.0.0", port=9009)

