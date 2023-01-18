from models import Candidate,CourtSearch,Recruiter,db,app



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
    lst=[]
    for candidate in candidates:
        temp={}
        temp["report"]=[]
        for document in candidate.document:
            temp["social_security"] = document.social_security
            temp["drivers_licsense"] = document.drivers_licsense
        for location in candidate.location:
            temp["zipcode"] = location.zipcode
            temp["location"] = location.locationname
        for report in candidate.reportinformation:
            temp["report"].append({"status":report.status,"adjunction":report.adjunction,"package": report.package,"completed_date":report.completed_date,
            "turn_around_time": report.turn_around_time})
        
        temp["id"]= candidate.id
        temp["name"]= candidate.name
        temp["adjunction"]= candidate.adjunction
        temp["status"]=candidate.status
        temp["date"]= candidate.date
        temp["emailid"]=candidate.email_id
           
        
        lst.append(temp)

    return lst


@app.route('/candidates/<id>')
def get_candidate(id):
    candidates = Candidate.query.filter_by(id=id)
    lst=[]
    for candidate in candidates:
        temp={}
        temp["report"]=[]
        for document in candidate.document:
            temp["social_security"] = document.social_security
            temp["drivers_licsense"] = document.drivers_licsense
        for location in candidate.location:
            temp["zipcode"] = location.zipcode
            temp["location"] = location.locationname
        for report in candidate.reportinformation:
            temp["report"].append({"status":report.status,"adjunction":report.adjunction,"package": report.package,"completed_date":report.completed_date,
            "turn_around_time": report.turn_around_time})
         
        temp["id"]= candidate.id
        temp["name"]= candidate.name
        temp["adjunction"]= candidate.adjunction
        temp["status"]=candidate.status
        temp["date"]= candidate.date
        temp["emailid"]=candidate.email_id
           
        
        lst.append(temp)

        return lst

    
   
       



@app.route('/courtsearches/<id>')
def get_courtsearch(id):
    court_search = CourtSearch.query.filter_by(search_id=id)
    results = [
            {
                "id": c.id,
                "name": c.name,
                "status": c.status,
                "date": c.date
            } for c in court_search]
    return results

@app.route('/courtsearches')
def get_courtsearches():
    court_search = CourtSearch.query.all()
    results = [
            {
                "name": c.name,
                "status": c.status,
                "date": c.date
            } for c in court_search]
    return results





if __name__ == '__main__':
    app.run()



# conn.close()
