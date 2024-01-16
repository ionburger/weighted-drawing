from flask import Flask, render_template, request
from fileinput import filename
from werkzeug.utils import secure_filename
from os import getcwd
from draw import choice


app = Flask("app")

@app.route('/')   
def main():   
    return render_template("index.html")   
  
@app.route('/result', methods = ['POST'])   
def result():   
    if request.method == 'POST':   
        f = request.files['file']
        if not f:
            return render_template("index.html", error = "No file selected")
        fname = secure_filename(f.filename)
        f.save(f"uploads/{fname}")

        return render_template("success.html", result = choice(f"uploads/{fname}"))
  
app.run()
