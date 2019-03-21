#!/usr/bin/env python


from __future__ import print_function
from getvmhosts import listvmhosts
from getvmhosts import checks
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', hosts=listvmhosts(), targethosts=checks())
@app.route('/compliance/<string:hostname>')
def compliance(hostname):
    return render_template('compliance.html',host=hostname)

#hello_world(h.names)


################################################
