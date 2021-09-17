import os
from flask import Flask, flash, request, redirect, render_template, send_file
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from gpFinder import gpMain, assignGrade
from merge import mergeMain, preprocessing
import time

app = Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'capstonecpg53@gmail.com'
app.config['MAIL_PASSWORD'] = 'capstone53'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['csv', 'txt', 'xlsx'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['GET','POST'])
def upload_file():

    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        mergeMain()
        gpMain('preprocessed.csv')
        # time.sleep(5)
        # fileToBeSent = open('output/results.csv', 'rb')
        # return send_file(fileToBeSent, attachment_filename='results.csv', as_attachment=True)
        return render_template('/sendEmail.html')

@app.route('/sendEmail')
def sendEmailHTML():
    return render_template('sendEmail.html')

@app.route('/sendEmail', methods=['GET', 'POST'])
def sendEmail():
    if request.method == 'POST':
        emailsRaw = request.form.get('emails')
        emails = emailsRaw.split(',')
        
        final_receipients = []
        for email in emails:
            email = email.strip()  
            final_receipients.append(email)  
        
        msg = Message('Results for attatched file(s)', sender="capstonecpg53@gmail.com", recipients=final_receipients)
        msg.body = "Hi, \nplease find below the attatched file containing the combined results of the file(s) you entered."
        with app.open_resource("output/results.csv", "rb") as fp:   
            msg.attach(filename="results.csv", content_type="text/plain", data=fp.read())  
        mail.send(msg)
        return render_template('/success.html')
    return render_template('/')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)