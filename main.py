import os
import jinja2
from google.appengine.ext import vendor, ndb

vendor.add('lib')

from flask import Flask, render_template, request, redirect
app = Flask(__name__,static_url_path='')
app.config['DEBUG'] = True

from twilio.rest import TwilioRestClient
account_sid = "AC4bac6baa1f943ac100f2000526a55c7f"
auth_token = "f9608374e4898fcfffd9c611d3ed62f3"
client = TwilioRestClient(account_sid, auth_token)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+'/templates/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/fridgeopened')
def send_message():
	#message = client.messages.create(to="+16142888469", from_="+16148456738", body="http://project-yumyum.appspot.com/static/scanner.html")
	return 'Message sent, son'

@app.route('/add')
def display_add_form():
	template = JINJA_ENVIRONMENT.get_template('add.html')
	return render_template(template)

@app.route('/add', methods = ['POST'])
def add():
	itemname = request.form.get('name')
	itemquant = float(request.form.get('quant'))
	unit = request.form.get('unit')
	NewItem=Item(name=itemname, quantity=itemquant, unit=unit)
	NewItem.put()
	return "added, Sandy"

@app.route('/list')
def GetItems():
	items = Item.query().fetch()
	template = JINJA_ENVIRONMENT.get_template('show.html')
	return template.render({'items':items})

@app.route('/delete', methods = ['GET'])
def deleteItems():
	id = request.args.get('id')
	key = ndb.Key(urlsafe=id)
	key.delete()
	return "deleted " + id +",Sandy"

@app.route('/update', methods=['GET'])
def updateItems():
	id=request.args.get('id')
	quant=request.args.get('quant')
	key = ndb.Key(urlsafe=id)
	item = key.get()
	item.quantity = float(quant)
	item.put()
	return 'updated ' + id + " with value " + quant

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

class Item(ndb.Model):
	name = ndb.StringProperty(required=True)
	quantity = ndb.FloatProperty(required=True)
	unit = ndb.StringProperty(required=True)


