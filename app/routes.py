from app import app
import os
import time
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import algo.process_image as ap
import test
import malayalam_letters as ml


UPLOAD_FOLDER = 'app/temp/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model_path  = 'res/model_v3_jlib'
#mdl = ap.init(model_path)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():

    result = None

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
            letter = test.recog(img_path)
            result = ml.to_malayalam(letter[0])
        
    return render_template('upload.html',var1 = result )

if __name__ == '__main__':
    app.run()