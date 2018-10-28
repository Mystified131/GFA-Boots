#This code imports the necessary modules.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mystified131:Jackson131!@mystified131.mysql.pythonanywhere-services.com/mystified131$GFASearches'
db = SQLAlchemy(app)
app.secret_key = 'noirhag3423irg'

#This code sets up the model for the database

class GFASearches(db.Model):
    sessiondata = db.Column(db.String(120), primary_key=True)

    def __init__(self, sessiondata):
        self.sessiondata = sessiondata

alldata = []
totaldata = GFASearches.query.all()
outstr = ""
for elem in totaldata:
    alldata.append(elem)

filnm = "GFA_Use_Report_Log.txt"

outfile = open(filnm, "w")

outfile.write('GFA Use Report Log (As of 10/28/2018, 10:00 am Central US time):'  + '\n')
outfile.write('\n')

for elem2 in alldata:
    elem3 = str(elem2)
    outfile.write(elem3 + '\n')

outfile.close()

## THE GHOST OF THE SHADOW ##