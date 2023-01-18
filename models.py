from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()
host_name=os.getenv('host_name')
portid=os.getenv('portid')
database= os.getenv('database')
username=os.getenv('username')
pwd=os.getenv('pwd')

app = Flask(__name__)
CORS(app)

app.config['WTF_CSRF_ENABLED'] = False

app.config["SQLALCHEMY_DATABASE_URI"]= f"postgresql://{username}:{pwd}@{host_name}:{portid}/{database}"

db = SQLAlchemy(app)

class Recruiter(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        name = db.Column(db.VARCHAR)
        email_id= db.Column(db.VARCHAR)

class Document(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    drivers_licsense= db.Column(db.VARCHAR)
    social_security= db.Column(db.VARCHAR)
    candidate_id = db.Column(db.Integer,db.ForeignKey('candidate.id'))
    
    
    
    
class Location(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    locationname=db.Column(db.VARCHAR)
    zipcode= db.Column(db.VARCHAR)
    location_id = db.Column(db.Integer,db.ForeignKey('candidate.id'))


class ReportInformation(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    status= db.Column(db.VARCHAR)
    adjunction= db.Column(db.VARCHAR)
    package=db.Column(db.VARCHAR)
    completed_date=db.Column(db.VARCHAR)
    turn_around_time=db.Column(db.VARCHAR)
    report_id = db.Column(db.Integer,db.ForeignKey('candidate.id'))    


class CourtSearch(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.VARCHAR)
    status= db.Column(db.VARCHAR)
    date=db.Column(db.VARCHAR)
    search_id = db.Column(db.Integer,db.ForeignKey('candidate.id'))

class Candidate(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column(db.VARCHAR)
    dob= db.Column(db.VARCHAR)
    phone= db.Column(db.VARCHAR)
    adjunction = db.Column(db.VARCHAR)
    status = db.Column(db.VARCHAR)
    date = db.Column(db.VARCHAR)
    email_id = db.Column(db.VARCHAR)
    document = db.relationship('Document',backref='candidate',lazy=True)
    location = db.relationship('Location',backref='candidate',lazy=True)
    reportinformation = db.relationship('ReportInformation',backref='candidate',lazy=True)
    CourtSearch = db.relationship('CourtSearch',backref='candidate',lazy=True)
   














if __name__ == '__main__':
  app.run()