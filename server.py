from flask import Flask, render_template, url_for, request

import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/<username>/<int:post_id>')
def hello_world2(username=None):
    return render_template('index.html', name=username)

@app.route('/index.html')
def about():
    return render_template('index.html')

#...@app.route('/favicon.ico')
# ..def favicon():
#.    return 'THESE ARE MY THOUGHTS ON BLOGS'


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        subject = data["Subject"]
        email = data["Email"]
        message = data["Message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([subject,email,message])
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'You have successfully submitted your form. Thank you for your cooperation! :)'
        
   