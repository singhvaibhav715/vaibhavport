from flask import Flask, render_template, redirect, url_for,request,Response
from flask_bootstrap import Bootstrap

app=Flask(__name__,static_url_path='/static')
UPLOAD_FOLDER='/media/vaibhav/8A00102700101D2F/Projects/Portfolio/static/'
app.config['SECRET_KEY'] = 'singhvaibhav715'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
