from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['pdf',"png","jpg","jpeg"]) # We only allow upload of pdf and image files.

app = Flask(__name__)

def remove_non_ascii(s): return "".join(i for i in s if ord(i)<128)

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
        
        # if we got a valid file:
        
        if file and allowed_file(file.filename):
            
            filename = remove_non_ascii(secure_filename(file.filename))        
            
            file.save(filename)
            
            return("Thank you for submitting a valid file!")
        
    return '''
    <!doctype html>
    <html>
    <head>
    <title>Template app</title>
    </head>
    <body>
    <h1>Template app</h2>
    Submit PDF/PNG/JPG-file:<br>
    
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload><br><br>
    </form>
    <br>
    <i>(You are doing great.)</i>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run()