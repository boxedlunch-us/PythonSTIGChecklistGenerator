#!/usr/bin/env python
#comment because reasons

from __future__ import print_function
from getvmhosts import listvmhosts
from getvmhosts import checks
from flask import Flask
from flask import render_template
from getvmhosts import v63173
from getvmhosts import getsinglehost
#from getvmhosts import v63173


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', hosts=listvmhosts(), targethosts=checks())


@app.route('/compliance/<hostname>')
def compliance(hostname):
    check = v63173(getsinglehost(hostname))
    return render_template('compliance.html', host=hostname, check=check)



################################################
