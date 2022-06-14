from app import app
import os
import time
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import algo.process_image as ap


UPLOAD_FOLDER = 'app/temp/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model_path  = 'res/model_v3.sav'
mdl = ap.init(model_path)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():

    if request.method == 'GET':
        time.sleep(1000)

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            #filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "test.png"))
            img_path = 'app/temp/test.png'
            result = ap.recognise_text(img_path, mdl)
            print('Result is {} and {}'.format(result[0], result[1]))
            flash('Result is {} and {}'.format(result[0], result[1]))
        
        
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()