from flask import render_template, Flask
from app import app
from models import Crime, Celebrity, Charge


@app.route('/')
@app.route('/splash')
def splash():
    return render_template('splash.html')

@app.route('/celebrities')
@app.route('/celebrities/')
def celebrities():
    celebrity_list = Celebrity.query.all()
    return render_template('celebrities.html', celebrities=celebrity_list)
@app.route('/celebrities/<celebrity>')
def getCelebrity(celebrity):
	celebrity_info = Celebrity.query.filter(Celebrity.name == celebrity).first()
	return render_template('celebrity.html', celebrity=celebrity_info)

@app.route('/crimes')
@app.route('/crimes/')
def crimes():
	crime_list = Crime.query.all()
	return render_template('crimes.html', crimes=crime_list)

@app.route('/crimes/<crime>')
def getCrime(crime):
    crime_info = Crime.query.filter(Crime.name == crime).first()
    return render_template('crime.html', crime=crime_info)

@app.route('/charges')
@app.route('/charges/')
def charges():
	charge_list = Charge.query.all()
	return render_template('charges.html', charges=charge_list)

@app.route('/about_us')
@app.route('/about_us/')
def about_us():
    return render_template('about_us.html')

     





