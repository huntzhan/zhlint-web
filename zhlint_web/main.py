# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

from flask import Flask, render_template, request

from zhlint_web.zhlint_operation import zhlint_check, zhlint_fix

app = Flask('zhlint-web')


@app.route('/default_console.html')
def default_console_html():
    return render_template('default_console.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check/', methods=['POST'])
def check():
    file_content = request.get_data(as_text=True)
    return zhlint_check(file_content)


@app.route('/fix/', methods=['POST'])
def fix():
    file_content = request.get_data(as_text=True)
    return zhlint_fix(file_content)


def entry_point():
    app.run(
        host='0.0.0.0',
        port=80,
        debug=True,
    )
