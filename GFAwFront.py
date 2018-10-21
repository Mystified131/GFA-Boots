#This code imports the necessary modules.

from flask import Flask, request, render_template, send_file, session

from GFAw import data_process

import cgi, datetime, random

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'nomdutysn'

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
                session['playlist'] = "GFA_" + sear + sear2 + "_" + timestamp + ".m3u"
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