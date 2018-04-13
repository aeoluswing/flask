# coding: utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# class Config(object):
# 	DEBUG = False
	# SQLALCHEMY_DATABASE_URI = 'dialect+driver://username:password@host:port/database'
	# For Example As Below
	# SQLite
	# SQLALCHEMY_DATABASE_URI = "sqlite///path/to/sqlite.db"

app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)


@app.route('/')
def hello_world():
	return 'Flask Image For Python:3.6.5-alpine'


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)