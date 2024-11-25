from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/Demo1'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  namn = db.Column(db.String(80), unique=False, nullable=False)
  city = db.Column(db.String(80), unique=False, nullable=False)
  postalcode = db.Column(db.String(10), unique=False, nullable=False)
  address = db.Column(db.String(50), unique=False, nullable=True)
  admin = db.relationship('Admin', backref='person', lazy=True)

class Admin(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  power = db.Column(db.String(80), unique=False, nullable=False)
  person = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

if __name__ == "__main__":
    with app.app_context():
      # db.create_all()
      upgrade()
