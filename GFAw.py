#this code returns a string of the page location's code

def page_to_string(url):
    import requests
    page = requests.get(url).text
    return page

#this function retrieves item file names from a chunk of text

def isolate_itemname(codechnk):
    newlst = []

    for ctr in range(len(codechnk)):
        if codechnk[ctr] == "h" and codechnk[ctr+1] == "r" and codechnk[ctr+2] == "e" and codechnk[ctr+3] == "f":
            newchk = codechnk[ctr:]
            for ct in range(len(newchk)):
                if newchk[ct] == "t" and newchk[ct+1] == "i" and newchk[ct+2] == "t" and newchk[ct+3] == "l":
                    newnum = ct - 2
                    newstchk = newchk[:newnum]
                    numa = newstchk.count("href")
                    if numa == 1 and (len(newstchk)<75):
                        newmon = newstchk[6:]
                        newerm = "https://archive.org" + newmon
                        numb = newerm.count("archive")
                        if numb == 1 and "&sor" not in newerm and "?sor" not in newerm and "title" not in newerm:
                            newlst.append(newerm)
    return newlst

#this function sends each of the netlabel's pages to have item files retrieved and turned into a list

def retrieve_pages(labelname, pgs, schtm, schtm2):
    medfnl = []
    for num1 in range(pgs):
        catr = num1+1
        ctr = str(catr)
        if schtm == "":
            schstr = ""
        if schtm != "":
            schstr = "and%5B%5D=" + schtm
        if schtm2 != "":
            tmptm = "+" + schtm2
            schstr += tmptm
        url =  "https://archive.org/details/" + labelname + "?" + schstr + "&sort=-publicdate&page=" + ctr
        print("Reading: " + url)
        bigstr = (page_to_string(url))
        medstr = isolate_itemname(bigstr)
        for itm in medstr:
            medfnl.append(itm)
    return medfnl

#this function cleans long, omipresent or inappropriate items from the list

def clean_list(lstin):
    lstout = []
    for itm in lstin:
        if "treetrunk 370" not in itm and "abides" not in itm and "disperse" not in itm and "POPSAKAL" not in itm and "TFR1121" not in itm and "Vvltvs" not in itm:
            lstout.append(itm)
    return lstout

#this function creates urls for the item download pages

def convert_itemname_list(lst, nm):
    trnlst = []
    for item in lst:
        ast = item[:20]
        bst = "download"
        cst = item[27:]
        dst = ast + bst + cst
        trnlst.append(dst)
    return trnlst

#this function makes a list of item titles

def make_itemtitle_list(last):
    nmlst = []
    for elem in last:
        atr = elem[28:]
        nmlst.append(atr)
    return nmlst

#this function retrieves mp3 file names from a chunk of text

def isolate_filename(codechnk, itmnm, typ):
    newlst = []

    for ctr in range(len(codechnk)):
        if codechnk[ctr] == "h" and codechnk[ctr+1] == "r" and codechnk[ctr+2] == "e" and codechnk[ctr+3] == "f":
            newchk = codechnk[ctr:]
            for ct in range(len(newchk)):
                if typ != "j" and newchk[ct] == "." and newchk[ct+1] == "m" and newchk[ct+2] == "p" and newchk[ct+3] == typ:
                    newnum = ct + 4
                    newstchk = newchk[:newnum]
                    searchstr = ".mp" + typ
                    numa = newstchk.count(searchstr)
                    numb = newstchk.count("href=")
                    ctr = 0
                    if (numa == 1) and (numb == 1) and ("_64kb" not in newstchk) and ("_vbr" not in newstchk) and (len(newstchk)<100):
                        newmon = newstchk[6:]
                        newrl = "https://archive.org/download" + itmnm + "/" + newmon
                        newlst.append(newrl)
                if typ == "j" and newchk[ct] == "." and newchk[ct+1] == "j" and newchk[ct+2] == "p" and newchk[ct+3] == "g":
                    newnum = ct + 4
                    newstchk = newchk[:newnum]
                    searchstr = ".jpg"
                    numa = newstchk.count(searchstr)
                    numb = newstchk.count("href=")
                    ctr = 0
                    if (numa == 1) and (numb == 1) and ("glogo" not in newstchk) and ("_thumb" not in newstchk) and (len(newstchk)<100):
                        newmon = newstchk[6:]
                        newrl = "https://archive.org/download" + itmnm + "/" + newmon
                        newlst.append(newrl)
    return newlst

#this code takes a list as an argument and removes redundant elements from that list

def remove_duplicates(x):
    y = list(set(x))
    return y

#this code writes a list into a file

def write_list_to_file(outname, lstname, typ, srch, timestamp):
    if typ == "3":
        wrtstr = ".m3u"
    if typ == "4":
        wrtstr = ".txt"
    if typ == "j":
        wrtstr = ".txt"
    outnm = "GFA_" + srch + "_" + timestamp + wrtstr

    outfile = open(outnm, "w")

    for elem in range(len(lstname)):
        outln = lstname[elem]
        try:
            outfile.write(outln + '\n')
        except:
            print("")

    outfile.close()


#this function writes a text file as a wpl

def write_wpl_code(wrtnm, conlst):
    outfile = open(wrtnm, "w")
    outfile.write("<?wpl version='1.0'?>" + '\n')
    outfile.write("<smil>" + '\n')
    outfile.write("    <head>"+ '\n')
    outfile.write("        <meta name='Generator' content='Microsoft Windows Media Player -- 12.0.17134.48'/>"+ '\n')
    outfile.write("        <meta name='ItemCount' content='0'/>"+ '\n')
    outfile.write("        <title>" + wrtnm + "</title>"+ '\n')
    outfile.write("    </head>"+ '\n')
    outfile.write("    <body>"+ '\n')
    outfile.write("        <seq>"+ '\n')
    for elem in conlst:
        outfile.write("            <media src=" + "'" + elem + "'" + "/>" + '\n')
    outfile.write("        </seq>"+ '\n')
    outfile.write("    </body>"+ '\n')
    outfile.write("</smil>"+ '\n')
    outfile.close()

#this code retrieves the date and time from the computer, to create the timestamp

def retrieve_date():
    import datetime
    right_now = datetime.datetime.now().isoformat()
    list = []

    for i in right_now:
        if i.isnumeric():
           list.append(i)

    tim = ("".join(list))
    return tim

#this code writes a list into a file

def write_list_to_htmlfile(outname, lstname, srch):

    outnm = outname + "_" + srch + ".html"

    outfile = open(outnm, "w")

    leng = str(len(lstname))

    outfile.write("Here are links to items from the search " + outname + " " + srch + "<br><br>" + '\n')

    outfile.write("Total Items: " + leng + "<br><br>" + '\n')

    for elem in range(len(lstname)):
        outln = lstname[elem]
        outln2 = "<a href = '" + outln + "'>" + outln + "</a><br>"
        try:
            outfile.write(outln2 + '\n')
        except:
            print("This item did not save due to an error:" + outln)

    outfile.close()

    return outnm

#this function returns a random variant of a list

def retrieve_random_elements(inlist, numoutlines):
    import random
    outlines = []

    for num1 in range(numoutlines):
        num2 = random.randrange(len(inlist))
        outlines.append(inlist[num2])

    return outlines

#this code writes the mp3 to a local file

def write_list_to_mp3(ur, titl):
    import requests
    print("")
    print("Downloading mp3 from: " + ur)
    ur2 = ""
    urb = ur[29:]
    for elem in urb:
        if elem.isalpha() or elem.isnumeric() or elem == ".":
            ur2 += elem
    ur3 = '/Users/mysti/Downloads/' + titl + "_" + ur2
    r = requests.get(ur)
    with open(ur3, 'wb') as f:
        f.write(r.content)

#this code is the main process to export to the web app

def data_process(ans1, timestamp, typ, sear, sear2):
    ans2 = 1
    error = ""
    lstend = retrieve_pages(ans1, ans2, sear, sear2)
    lstmor = clean_list(lstend)
    totm3u = []
    lster = convert_itemname_list(lstmor, ans1)
    namlst = make_itemtitle_list(lster)
    ctr = 0
    for elem in lster:
        pgchk = page_to_string(elem)
        itmnm = namlst[ctr]
        allmp3 = isolate_filename(pgchk, itmnm, typ)
        fnlmp3 = remove_duplicates(allmp3)
        for item in fnlmp3:
            totm3u.append(item)
        ctr += 1
    serch = sear + sear2
    if len(totm3u) == 0:
        error = "Your search turned up no items. Please try again."
    else:
        write_list_to_file(ans1, totm3u, typ, serch, timestamp)
        error = ""
    return error

## THE GHOST OF THE SHADOW ##










