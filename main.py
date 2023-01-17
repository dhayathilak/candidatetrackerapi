from flask import Flask,request
from flask_cors import CORS
from models import Candidate,CourtSearch,Recruiter,db,app

lst=[]

@app.route('/recruiters')
def get_recruiters():
    recruiters_info = Recruiter.query.all()
    results = [
            {
                "id": recruiter.id,
                "name": recruiter.name,
                "email_id": recruiter.email_id
            } for recruiter in recruiters_info]
    return results

@app.route('/recruiters/<id>')
def get_recruiter(id):
    recruiters_info = Recruiter.query.filter_by(id=id)
    results = [
            {
                "id": recruiter.id,
                "name": recruiter.name,
                "email_id": recruiter.email_id
            } for recruiter in recruiters_info]
    return results

@app.route('/candidates')
def get_candidates():
    candidates = Candidate.query.all()
    
    for candidate in candidates:
        for document in candidate.document:
            lst.append({"social_security":document.social_security})
            lst.append({"drivers_licsense":document.drivers_licsense})
        for location in candidate.location:
            lst.append({'zipcode':location.zipcode})
        for report in candidate.reportinformation:
            lst.append({'status':report.status})
            lst.append({'adjunction':report.adjunction})
            lst.append({'package':report.package})
            lst.append({'completed_date':report.completed_date})
            lst.append({'turn_around_time':report.turn_around_time})
        
        lst.append({'candidate_name':candidate.name})

    return lst


@app.route('/candidates/<id>')
def get_candidate(id):
    candidates = Candidate.query.filter_by(id=id)
    
    for candidate in candidates:
        for document in candidate.document:
            lst.append({"social_security":document.social_security})
            lst.append({"drivers_licsense":document.drivers_licsense})
        for location in candidate.location:
            lst.append({'zipcode':location.zipcode})
        for report in candidate.reportinformation:
            lst.append({'status':report.status})
            lst.append({'adjunction':report.adjunction})
            lst.append({'package':report.package})
            lst.append({'completed_date':report.completed_date})
            lst.append({'turn_around_time':report.turn_around_time})
        
        lst.append({'candidate_name':candidate.name})

    return lst

@app.route('/courtsearch/<id>')
def get_courtsearch(id):
    court_search = CourtSearch.query.filter_by(id=id)
    results = [
            {
                "id": c.id,
                "name": c.name,
                "status": c.status,
                "date": c.date
            } for c in court_search]
    return results





if __name__ == '__main__':
    app.run()



# conn.close()
