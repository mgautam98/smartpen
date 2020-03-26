import os
import json
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import edge_detect

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('display', filename=filename))
    return render_template('home.html')

@app.route('/upload/<filename>')
def uploaded_file(filename):
    print(filename)
    return send_from_directory("uploads", filename)

@app.route('/coordinates/<filename>')
def closest_edge(filename):
    return (255,255)

@app.route('/display/<filename>')
def display(filename):
    [processed_imgname, data] = edge_detect.canny_edge_detect(filename)
    return render_template("display.html", org_img=filename, prc_img=processed_imgname, data = json.dumps(data))

                               
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')
