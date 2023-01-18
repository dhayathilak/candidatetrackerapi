from models import db, Document, Candidate, ReportInformation

candidate1 = Candidate(name='john smith',adjunction='-',status='cleared',date='24/12/2022',email_id='johns@gmail.com')
candidate2 = Candidate(name='jason',adjunction='-',status='cleared',date='24/12/2022',email_id='jass@gmail.com')
candidate3 = Candidate(name='dhaya',adjunction='-',status='cleared',date='24/12/2022',email_id='d@gmail.com')


document1 = Document(drivers_licsense='12wff67y',social_security='xxxx-xx-xx-69',candidate_id=candidate1)
document2 = Document(drivers_licsense='12wff675y',social_security='xxxx-xx-xx-60',candidate_id=candidate1)
document3 = Document(drivers_licsense='12wfdg',social_security='xxxx-xx-xx-645',candidate_id=candidate2)
document4 = Document(drivers_licsense='12wfdg',social_security='xxxx-xx-xx-685',candidate_id=candidate3)

report1 = ReportInformation(status='engaged',adjunction='-',package='delivered',completed_date='23/12/33',turn_around_time='1 day 6 hours',id=4)




db.session.add_all([candidate1,candidate2,candidate3])
db.session.add_all([document1,document2,document3,document4])
db.session.commit()