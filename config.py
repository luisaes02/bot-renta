BOT_TOKEN = '5253208958:AAGOSN1d41xvq490dc1a1QAcMbyb3MgtJuQ'
PV_USERS = ['LAES2002']
#Database
USERS = {}
def saveDB():
    import os
    name = 'database.udb'
    dbfile = open(name,'w')
    i = 0
    for user in USERS:
        separator = ''
        if i < len(USERS)-1:
            separator = '\n'
        dbfile.write(user+'='+str(USERS[user]) + separator)
        i+=1
    dbfile.close()

def createUser(name):
    import time
    USERS[name] = {'moodle_host':'https://eduvirtual.uho.edu.cu/','moodle_repo_id':3,'moodle_user':'karina-marrera','moodle_password':'kari0829','isadmin':0,'zips':180}

def getUser(name):
    try:
        return USERS[name]
    except:
        return None

def saveDataUser(user,data):
    USERS[user] = data

def isAdmin(user):
    User = getUser(user)
    if User:
        return User['isadmin']==1
    return False

def loadDB():
    import os
    import json
    name = 'database.udb'
    dbfile = open(name,'r')
    lines = dbfile.read().split('\n')
    dbfile.close()
    for lin in lines:
        if lin == '':continue
        tokens = lin.split('=')
        user = tokens[0]
        PV_USERS.append(user)
        data = json.loads(str(tokens[1]).replace("'",'"'))
        USERS[user] = data

#load db to init
loadDB()
