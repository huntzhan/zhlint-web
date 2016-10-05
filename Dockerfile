FROM ubuntu:latest
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get -y update && apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils git

RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

RUN echo 'export PATH="/root/.pyenv/bin:$PATH"' > ~/.bash_profile
RUN echo 'eval "$(pyenv init -)"' > ~/.bash_profile
RUN echo 'eval "$(pyenv virtualenv-init -)"' > ~/.bash_profile

ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 2.7.12
RUN pyenv global 2.7.12
RUN pyenv rehash

RUN git clone https://github.com/huntzhan/zhlint-web.git ~/zhlint-web

RUN cd ~/zhlint-web; pip install -r requirements.txt
RUN cd ~/zhlint-web; python setup.py install

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

CMD cd ~/zhlint-web; ZHLINT_PYENV_VERSION=2.7.12 $PYENV_ROOT/versions/2.7.12/bin/zhlint-web
