#!/usr/env/bin python
#encoding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.environ.get('DATABASE_URL'), 'app.db') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')