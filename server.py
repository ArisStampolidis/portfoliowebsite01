from flask import Flask, render_template, url_for, request, redirect
import csv
import requests
import hashlib
import sys
from passwordchecker import request_api_data, get_password_leaks_count, pwned_api_check, main

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#def write_to_password(data):
#  with open('./portfolio01/database_password.txt', mode='w') as database:
#    password = data["password"]
#    file = database.write(f'{password}')

def write_to_csv(data):
  with open('./portfolio01/database.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
      except:
        return 'did not save to database'
    else:
      return 'something went wrong. Try again!'


@app.route('/predict', methods=['POST'])
def predict():
    password = request.form['password']
    result = str(main(password))
    return render_template('work1.html', prediction_text=(result))