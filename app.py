import sqlite3
import hashlib
from flask import Flask, render_template, redirect, url_for, request, session
from functools import wraps
import time
from random import randint
app = Flask(__name__)
app.secret_key = "nico"
app.debug = True

import pymysql as mysql
import pymysql

def set_db(h,u,p,d):
    session["host"]=h
    session["username"]=u
    session["password"]=p
    session["database"]=d


def connect():
    h=session["host"]
    u=session["username"]
    p=session["password"]
    d=session["database"]
    con= mysql.connect(h,u,p,d,port=3307,cursorclass=pymysql.cursors.DictCursor)
    return con

def del_data(condition=""):
    table=session["table"]
    sql="DELETE FROM "+ table +" where "+condition+" ;"
    #print(sql)
    #return 0
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()

def create_data(info=[]):
    table=session["table"]
    datax="'"
    for x in info:
        datax+=str(x)+"','"
    datax=datax[:-2]
    sql="insert into " + table +" values("+datax+");"
    print(sql)
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()


def update_data(updates=[],condition=""):
    table=session["table"]
    nico="update "+table+" set "
    y=0
    for x in session["cols"]:
        q=str(x)+"= '"+str(updates[y])+"',"
        nico+=q
        y+=1
    nico=nico[:-1]
    nico+=" where "+condition+" ;"
    print(nico)
    #return "hj"
    con = connect()
    cur = con.cursor()
    cur.execute(nico)
    con.commit()
    return("successfully inserted data")

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


@app.route('/')
def index():
    return (render_template('index.html'))

	
def read_data():
    table=session["table"]
    list_of_values=[]
    list_of_cols=[]
    lit_of_dels=[]
    list_of_updates=[]
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM "+str(table).lower())
    with con:
        rows = cur.fetchall()
        try:
            list_of_cols=list(rows[0].keys())
        except Exception as e:
            list_of_cols=["empty","empty"]
        for row in rows:
            kop=list(row.values())
            list_of_values.append(kop)
            st="/d/"+kop[0]
            rd="/dashboard/members/updates/"+kop[0]
            list_of_updates.append(rd)
            lit_of_dels.append(st)
    if list_of_values==[]:
        list_of_values=[['UH OH ;)'],['This table is empty']]
    session["cols"]= list_of_cols
    session["colsxy"]= len(list_of_cols)
    session["vals"]= list_of_values
    session["valsxy"]= len(list_of_values)
    session["dels"]= lit_of_dels
    session["updates"]= list_of_updates
    return([list_of_cols,list_of_values])

@app.route('/pricing')
def pricing():
    return (render_template('pricing.html'))


@app.route('/dashboard', methods=['GET', 'POST'])
@is_logged_in
def dashboard():
    if request.method == 'POST':
        pass
        return (render_template('dashboard.html'))
    else:
        return (render_template('dashboard.html'))


@app.route('/dashboard/members', methods=['GET', 'POST'])
@is_logged_in
def members():
    if request.method == 'POST':
        k=str(time.time())
        k=k.split(".")
        mo="x".join(k)
        print(mo)
        mo=mo+str(randint(0, 19))
        arr=[mo,request.form["name"],request.form["email"],request.form["phone"],request.form["desc"],request.form["cred"]]
        print(arr)
        create_data(arr)
        return (redirect(url_for('members')))
    else:
        h="localhost"
        u="root"
        p="Black11060"
        d="saccos"
        set_db(h,u,p,d)
        connect()
        session["table"]="members"
        read_data()
        return (render_template('members.html'))
		
@app.route('/d/<string:name>')
@is_logged_in
def delete(name):
    cond="id = '"+name+"'"
    del_data(cond)
    return(redirect(url_for("members")))


@app.route('/dashboard/members/updates/<string:name>', methods=['GET', 'POST'])
@is_logged_in
def update(name):
    cond="id = '"+name+"'"
    if request.method == 'POST':
        arr=[name,request.form["name"],request.form["email"],request.form["phone"],request.form["desc"],request.form["cred"]]
        update_data(arr,cond)
        return (redirect(url_for('members')))
    else:
        table=session["table"]
        list_of_value=[]
        con = connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM "+str(table).lower()+" where "+cond)
        with con:
            rows = cur.fetchall()
            for row in rows:
                kop=list(row.values())
                list_of_value.append(kop)
        list_of_value=list_of_value[0]
        print(list_of_value)
        session["nme"]= list_of_value[1]
        session["mail"]= list_of_value[2]
        session["phon"]= list_of_value[3]
        session["de"]= list_of_value[4]
        session["cred"]= list_of_value[5]
        
        return(render_template("memberupdate.html"))


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        conn = sqlite3.connect('static/login.db')
        c = conn.cursor()
        username = request.form['username']
        print(username)
        password = request.form['password']
        email = request.form['email']
        subscription = request.form['subscription']

        fullstring = "'" + str(username) + "'" + "," + "'" + str(password) + "'" + "," + "'" + str(
            email) + "'" + "," + "'" + str(subscription) + "'"
        print(fullstring)
        c.execute("INSERT INTO users VALUES(" + str(fullstring) + ")")
        conn.commit()
        conn.close
        return redirect(url_for('login'))

    return render_template('register.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion == False:
            app.logger.info("PASSWORD NOT MATCHED")
            error = 'Invalid Credentials. Please try again...'
        else:
            app.logger.info("PASSWORD MATCHED")
            session['logged_in'] = True
            session['username'] = username

            con = sqlite3.connect('static/login.db')
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbsub = row[3]
                    if dbUser == username:
                        subscription = dbsub
            session['subscription'] = subscription
            return redirect(url_for('members'))
    return render_template('login.html', error=error)


def validate(username, password):
    con = sqlite3.connect('static/login.db')
    completion = False
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            dbUser = row[0]
            dbPass = row[1]
            if dbUser == username:
                completion = check_password(dbPass, password)
    return completion


def check_password(hashed_password, user_password):
    return hashed_password == user_password


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port= 1000)
