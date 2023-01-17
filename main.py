from flask import Flask,request
from flask_cors import CORS
import psycopg2

# flask app initilization
app = Flask(__name__)
host_name='127.0.0.1'
portid=5432
database= 'Candidatetracker'
username='postgres'
pwd=1234

# setting up a connection cursor
conn  = psycopg2.connect(host=host_name,dbname=database,user=username,password=pwd)
try:
    cur = conn.cursor()

except Exception as error:
    print(error)


@app.route('/recruiters',methods=['GET'])
def get_recruiters():
    cur.execute("SELECT * FROM RECRUITERS")
    records = cur.fetchall()
    return records


@app.route('/recruiters/<id>',methods=['GET'])
def get_recruiter():
    cur.execute("SELECT * FROM RECRUITERS RECRUITER WHERE RECRUITER.ID='%s"%(id))
    records = cur.fetchall()
    return records


@app.route('/candidates',methods=['GET'])    
def get_candidates():
    cur.execute("select c.id,c.name,c.adjunction,c.date,c.email_id,l.zipcode,d.drivers_licsense,d.social_security,r.* from candidates c inner join locations l on c.id= l.id inner join documents d on c.documentid= d.id inner join report_information r on c.id = r.id")
    records = cur.fetchall()
    return records

@app.route('/candidates/<id>',methods=['GET'])    
def get_candidate(id):
    cur.execute("select c.id,c.name,c.adjunction,c.date,c.email_id,l.zipcode,d.drivers_licsense,d.social_security,r.* from candidates c inner join locations l on c.id= l.id inner join documents d on c.documentid= d.id inner join report_information r on c.id = r.id where c.id='%s'"%(id))
    records = cur.fetchall()
    return records

@app.route('/candidates/<id>',methods=['PUT','GET'])
def update_adverse_action(id):
    adverse_action = request.form.get('adverse_action')
    print(adverse_action)
    cur.execute("update candidates set adjunction =CASE adjunction  when 'pre-adverse' then 'adverse' when 'engage' then 'engage' else '-' end  where candidates.id='%s'"%(id))
    records = cur.fetchall()
    return records

if __name__ == '__main__':
    app.run()



conn.close()
