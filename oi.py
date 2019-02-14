#!/usr/bin/env python


from __future__ import print_function
from getvmhosts import listvmhosts
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html', hosts=listvmhosts())

# hello_world(h.names)


################################################
