from flask import Flask, request, render_template, flash
import requests
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from dist_calc import Geocode

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class AddrInput(Form):
	api_key = TextField('API Key:', validators=[validators.required()])
	addr1 = TextField('Address 1:', validators=[validators.required()])
	addr2 = TextField('Address 2:', validators=[validators.required()])

@app.route('/', methods=['GET', 'POST'])

def calc():

	form = AddrInput(request.form)

	print form.errors
	if request.method == 'POST':
		api_key=request.form['api_key']
		addr1=request.form['addr1']
		addr2=request.form['addr2']
		
		print (addr1, addr2)

		if form.validate():
			Gdata1 = Geocode(addr1,api_key)
			Gdata2 = Geocode(addr2,api_key)

			address1, address2, dist=Gdata1.calc_dist(Gdata2)
			if (address1 == 'REQUEST_DENIED'):
				flash('Request Denied: Please Enter a Valid API Key. ')
			else:
				flash('The distance between {} and {} is '.format(address1, address2) + '{0:.2f}'.format(dist) + ' km')
		else:
			flash('All the form fields are required. ')

	return render_template("calc.html", form=form)

if __name__ == "__main__":
	app.run(host='localhost', debug=True, port=5001, use_reloader=True)