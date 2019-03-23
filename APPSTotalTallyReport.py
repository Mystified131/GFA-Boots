#This code imports the necessary modules.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mystified131:Jackson131!@mystified131.mysql.pythonanywhere-services.com/mystified131$APPSTotal'
db = SQLAlchemy(app)
app.secret_key = 'noirhag3423irg'

#This code sets up the model for the database

class APPSTotal(db.Model):
    sessiondata = db.Column(db.String(120), primary_key=True)

def __init__(self, sessiondata):
    self.sessiondata = sessiondata

right_now = datetime.datetime.now().isoformat()

alldata = []
totaldata = APPSTotal.query.all()
totalhits = str(len(totaldata))
outstr = ""
for elem in totaldata:
    alldata.append(elem)

filnm = "Apps_Use_Tally_Report_Log_Current.txt"

outfile = open(filnm, "w")

outfile.write('Web Applications Use Report Log (Beginning 10/29/2018, 5:00 am Central US time):'  + '\n')
outfile.write('\n')
outfile.write('Report created at: ' + right_now  + '\n')
outfile.write('\n')

outfile.write('Total App Hits: ' + totalhits  + '\n')
outfile.write('\n')

Mixplant = 0
IAPG = 0
IAVA = 0
GFA = 0
TPAE = 0
GSR = 0
EDR = 0
PI = 0
TA = 0
RIC = 0
BB = 0

for elem2 in alldata:
    elem3 = str(elem2)
    if "Mixplant" in elem3:
        Mixplant += 1
    if "IAPG" in elem3:
        IAPG += 1
    if "IAVA" in elem3:
        IAVA += 1
    if "GFA" in elem3:
        GFA += 1
    if "TPAE" in elem3:
        TPAE += 1
    if "GSR" in elem3:
        GSR += 1
    if "EDR" in elem3:
        EDR += 1
    if "PI" in elem3:
        PI += 1
    if "TextAnalysis" in elem3:
        TA += 1
    if "RIC" in elem3:
        RIC += 1
    if "BB" in elem3:
        BB += 1


Mixplantstr = "Mixplant: " + str(Mixplant)
IAPGstr = "IAPG: " + str(IAPG)
IAVAstr = "IAVA: " + str (IAVA)
GFAstr = "GFA: " + str(GFA)
TPAEstr = "TPAE: " + str(TPAE)
GSRstr = "GSR: " + str(GSR)
EDRstr = "EDR: " + str(EDR)
PIstr = "PI: " + str(PI)
TAstr = "TA: " + str(TA)
RICstr = "RIC: " + str(RIC)
BBstr = "BB: " + str(BB)

outfile.write(Mixplantstr + '\n')
outfile.write(IAPGstr + '\n')
outfile.write(IAVAstr + '\n')
outfile.write(GFAstr + '\n')
outfile.write(TPAEstr + '\n')
outfile.write(GSRstr + '\n')
outfile.write(EDRstr + '\n')
outfile.write(PIstr + '\n')
outfile.write(TAstr + '\n')
outfile.write(RICstr + '\n')
outfile.write(BBstr + '\n')

outfile.close()

## THE GHOST OF THE SHADOW ##