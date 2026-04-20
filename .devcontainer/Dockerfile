FROM jupyter/datascience-notebook:latest

USER root

ARG NB_USER=jovyan

RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    ruby-full \
    build-essential \
    libffi-dev \
    libzmq3-dev \
    libsqlite3-dev \
    libssl-dev \
    pkg-config \
    zlib1g-dev \
    libreadline-dev \
    libyaml-dev \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

RUN echo "${NB_USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${NB_USER} \
    && chmod 0440 /etc/sudoers.d/${NB_USER}

RUN echo "${NB_USER}:1454" | chpasswd

RUN gem install --no-document iruby rails activerecord sqlite3 nokogiri

USER ${NB_USER}

RUN iruby register --force --name iruby --display-name "Ruby (IRuby)"
