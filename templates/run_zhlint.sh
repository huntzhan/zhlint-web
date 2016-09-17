#!/bin/bash
# Enable pyenv.
export PATH=~/.pyenv/shims:~/.pyenv/bin:"$PATH"
# Fix encoding problem.
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8

export PYENV_VERSION={{ pyenv_python_version }}

script -q -c '{{ zhlint_command }} "{{ input_file }}"' /dev/null zhlint | ansi2html > "{{ output_file }}"

# Reset version
unset PYENV_VERSION
