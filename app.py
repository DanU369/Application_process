from flask import Flask, render_template, request, url_for, redirect
from random import randint

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    city_name=request.args.get('city-name')
    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city_name:
        mentor_details = data_manager.get_mentors_by_city(city_name)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details)

@app.route('/applicants', methods=['GET','POST'])
def applicants_list():
    if request.method=='POST':
        ending_email=request.form['email-ending']
        data_manager.delete_applicant_by_ending_email(ending_email)
    applicant_details=data_manager.get_applicants()
    return render_template('applicants.html', applicants=applicant_details)

@app.route('/add-applicant', methods=['GET','POST'])
def add_new_applicant():
    if request.method=='POST':
        first_name=request.form['first-name']
        last_name = request.form['last-name']
        phone_number = request.form['phone-number']
        email = request.form['email']
        id=randint(10000,99999)
        application_id=str(id)
        data_manager.add_applicant(first_name,last_name,phone_number,email,id)
        return redirect('/applicants/'+application_id)
    else:
        return render_template('add_applicant.html')


@app.route('/applicants/<application_code>', methods=['GET','POST'])
def update_applicant_details(application_code):
    if request.method=='POST':
        new_phone_number = request.form['new-phone']
        data_manager.update_phone_number(new_phone_number,application_code)
        return redirect('/applicants/'+application_code)
    else:
        applicant_details=data_manager.get_applicants_by_application_code(application_code)
    return render_template('applicants_update.html',applicants=applicant_details,application_code=application_code)

@app.route('/applicants/<application_code>/delete')
def delete_applicant(application_code):
    data_manager.delete_applicant_by_application_code(application_code)
    return redirect('/applicants')


@app.route('/applicants-phone')
def applicants_phone():
    applicant_name=request.args.get('applicant-name')
    applicant_email=request.args.get('email-ending')
    if applicant_name:
        applicant_details=data_manager.get_applicants_by_name(applicant_name)
    elif applicant_email:
        applicant_details = data_manager.get_applicants_by_email(applicant_email)
    else:
        return "YOU SHOULD NOT BE HERE"
    return render_template('search_applicants.html', applicants=applicant_details)



if __name__ == '__main__':
    app.run(debug=True)
