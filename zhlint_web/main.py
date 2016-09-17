# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

from flask import Flask, render_template

app = Flask('zhlint-web')


@app.route('/default_console.html')
def default_console_html():
    return render_template('default_console.html')


@app.route('/')
def index():
    return render_template('index.html')


def entry_point():
    app.run(debug=True)
