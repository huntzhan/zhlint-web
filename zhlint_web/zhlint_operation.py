# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

import os
from tempfile import NamedTemporaryFile
import subprocess

from flask import render_template


def dump2tmpfile(func):

    def wrapper(file_content):
        with NamedTemporaryFile() as fin:
            with NamedTemporaryFile() as fout:
                # input.
                with open(fin.name, encoding='utf-8', mode='w') as _f:
                    _f.write(file_content)

                # process.
                func(fin, fout)

                # output.
                with open(fout.name) as _f:
                    ret = _f.read()
        return ret

    return wrapper


@dump2tmpfile
def run_bash_script(fin, fout):
    subprocess.call(
        'chmod +x "{0}"'.format(fin.name),
        shell=True,
    )
    subprocess.call(
        fin.name,
        shell=True,
    )


@dump2tmpfile
def zhlint_check(fin, fout):
    bash_script = render_template(
        'run_zhlint.sh',
        pyenv_python_version=os.environ['ZHLINT_PYENV_VERSION'],
        zhlint_command='check',
        input_file=fin.name,
        output_file=fout.name,
    )
    run_bash_script(bash_script)


@dump2tmpfile
def zhlint_fix(fin, fout):
    bash_script = render_template(
        'run_zhlint.sh',
        pyenv_python_version=os.environ['ZHLINT_PYENV_VERSION'],
        zhlint_command='fix',
        input_file=fin.name,
        output_file=fout.name,
    )
    run_bash_script(bash_script)
