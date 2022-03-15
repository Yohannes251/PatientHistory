from models import patient, records
from flask import Flask, render_template, request, flash
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=patient.engine)
session = Session()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/reception', methods=['GET', 'POST'])
def reception():
    if request.method == 'GET':
        if ('getinfo' in request.args.keys()):
            phonenumber = request.args['getinfo']
            data = session.query(patient.Patient).filter(patient.Patient.phonenumber == phonenumber)
            return render_template('information.html', data=data)
        else:
            return render_template('reception.html')
    elif request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        phonenumber = request.form['phonenumber']
        city = request.form['city']
        new_patient = patient.Patient(name, gender, age, phonenumber, city)
        session.add(new_patient)
        session.commit()

        return render_template('reception.html')

@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    if request.method == 'GET':
        if ('getinfo' in request.args.keys()):
            cardno = request.args['getinfo']
            info = session.query(patient.Patient).filter(patient.Patient.id == cardno)
            data = session.query(records.Records).filter(records.Records.cardno == cardno)
            return render_template('records.html', data=data, info=info)
        else:
            return render_template('doctor.html')
    elif request.method =='POST':
        cardno = request.form['cardno']
        doctorname = request.form['doctorname']
        labtests = request.form['labtests']
        labresults = request.form['labresults']
        diagnosis = request.form['diagnosis']
        treatment = request.form['treatment']
        prescription = request.form['prescription']
        critical = request.form['critical']
        new_record = records.Records(cardno, doctorname, labtests, labresults, diagnosis, treatment, prescription, critical)
        session.add(new_record)
        session.commit()

        return render_template('doctor.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
