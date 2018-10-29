#This code imports the necessary modules.

from flask import Flask, request, render_template, send_file, session
from flask_sqlalchemy import SQLAlchemy
from GFAw import data_process

import cgi, datetime, random

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mystified131:Jackson131!@mystified131.mysql.pythonanywhere-services.com/mystified131$APPSTotal'
db = SQLAlchemy(app)
app.secret_key = 'nomdutysn'

#This code sets up the model for the database

class APPSTotal(db.Model):
    sessiondata = db.Column(db.String(120), primary_key=True)

    def __init__(self, sessiondata):
        self.sessiondata = sessiondata

#This code constructs the main page. It takes data from several forms, processed the data using some functions from the model, and, after processing, opens a player page.

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', error = "")
    else:
        right_now = datetime.datetime.now().isoformat()
        list = []
        for i in right_now:
            if i.isnumeric():
                list.append(i)
        tim = "".join(list)
        session['timestamp'] = tim
        ans1 = "audio"
        sear = request.form['searchin']
        sear = cgi.escape(sear)
        sear2 = request.form['secondsearch']
        sear2 = cgi.escape(sear2)
        opt = request.form['option']
        typ = "3"
        if opt != "y":
            error = data_process(ans1, tim, typ, sear, sear2)
            if error:
                return render_template('index.html', error = error)
            else:
                timestamp = session['timestamp']
                session['playlist'] = "GFA_audio_" + sear + sear2 + "_" + timestamp + ".m3u"
                sessiondata = timestamp + "_GFA_audio_" + sear + sear2
                if len(sessiondata) > 119:
                    sessiondata = sessiondata[:119]
                new_entry = APPSTotal(sessiondata)
                db.session.add(new_entry)
                db.session.commit()
                content = []
                playlist = session['playlist']
                infile = open(playlist, "r")
                plist = infile.readline()
                while plist:
                    content.append(plist)
                    plist = infile.readline()
                infile.close()
                length = str(len(content))
                atracknum = random.randrange(len(content))
                item = str(atracknum + 1)
                atrack = content[atracknum]
                return render_template('newsplayer.html', toplay = atrack, ur = playlist, length = length, item = item)

        else:
            right_now = datetime.datetime.now().isoformat()
            list = []
            for i in right_now:
                if i.isnumeric():
                    list.append(i)
        tim = "".join(list)
        linkslist = "GFA_links_" + sear + sear2 + "_" + tim
        sessiondata = tim + "_GFA_links_" + sear + sear2
        new_entry = APPSTotal(sessiondata)
        db.session.add(new_entry)
        db.session.commit()
        outfile = open(linkslist, "w")
        outfile.close()
        ans1 = "audio"
        return render_template('results.html', sear = sear, sear2 = sear2)

#This code sets up the player page. It takes a random item from a list and cues it up in the player, along with some additional information and functionality.

@app.route('/newsplayer', methods=['POST', 'GET'])
def newsplayer():
    content = []
    playlist = session['playlist']
    infile = open(playlist, "r")
    plist = infile.readline()
    while plist:
        content.append(plist)
        plist = infile.readline()
    infile.close()
    length = str(len(content))
    atracknum = random.randrange(len(content))
    item = str(atracknum + 1)
    atrack = content[atracknum]
    return render_template('newsplayer.html', toplay = atrack, ur = playlist, length = length, item = item)

#This code processes a request to download the program's output, and sends a file to the user's console.

@app.route('/download', methods=['POST', 'GET'])
def download():
    st5 = session['playlist']
    return send_file(st5, attachment_filename=st5, as_attachment=True)

## THE GHOST OF THE SHADOW ##