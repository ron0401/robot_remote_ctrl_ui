# coding: utf-8
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/index") 
def index():
   return render_template('index.html',myip = '192.168.0.196')

if __name__ == "__main__":
    app.run(host='0.0.0.0')