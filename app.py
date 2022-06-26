# coding: utf-8
from flask import Flask, render_template, request
import json
from copy import copy

app = Flask(__name__)

j = open('param.json','r')
param = json.load(j)
@app.route("/", methods=["GET"]) 
def index():
    pr = copy(param)
    req = request.args
    pr['IMAGE_SERVER']['HOST'] = pr['IMAGE_SERVER']['HOST'] if req.get("image_server_host") == None else req.get("image_server_host")
    pr['IMAGE_SERVER']['PORT'] = pr['IMAGE_SERVER']['PORT'] if req.get("image_server_port") == None else req.get("image_server_port")
    pr['ROSBRIDGE_SEVER']['HOST'] = pr['ROSBRIDGE_SEVER']['HOST'] if req.get("rosbidge_server_host") == None else req.get("rosbidge_server_host")
    pr['ROSBRIDGE_SEVER']['PORT'] = pr['ROSBRIDGE_SEVER']['PORT'] if req.get("rosbidge_server_port") == None else req.get("rosbidge_server_port")
    return render_template('index.html',IMAGE_SERVER = pr['IMAGE_SERVER'],ROSBRIDGE_SEVER = pr['ROSBRIDGE_SEVER'])

if __name__ == "__main__":
    app.run(host='0.0.0.0')