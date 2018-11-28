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

def calc_ac():
    sql="truncate account"
    print(sql)
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    print("inserted")
    tempconts=0
    temploans=0
    table="total_contributions"
    sql="select amount from "+ table +" where memno='"+session["memno"]+"'"
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    list_of_cols=[]
    with con:
        rows = cur.fetchall()
        try:
            list_of_cols=list(rows[0].keys())
        except Exception as e:
            list_of_cols=["empty","empty"]
        for row in rows:
            toto=list(row.values())
            tempconts=toto[0]
    table="total_loans"
    sql="select amount from "+ table +" where memno='"+str(session["memno"])+"'"
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    list_of_cols=[]
    with con:
        rows = cur.fetchall()
        try:
            list_of_cols=list(rows[0].keys())
        except Exception as e:
            list_of_cols=["empty","empty"]
        for row in rows:
            toto=list(row.values())
            temploans=toto[0]
    table="total_dividends"
    cred=""
    sql="select amount from "+ table +" where memno='"+str(session["memno"])+"'"
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    list_of_cols=[]
    with con:
        rows = cur.fetchall()
        try:
            list_of_cols=list(rows[0].keys())
        except Exception as e:
            list_of_cols=["empty","empty"]
        for row in rows:
            toto=list(row.values())
            cred=toto[0]
    grand=temploans+tempconts
    session["grand"]=grand
    session["loans"]=temploans
    session["conts"]=tempconts
    session["cred"]=cred
    sql="insert into account values('"+ session["memno"] +"','"+ str(session["grand"])+"');"
    print(sql)
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    print("inserted")

def calc_loans():
    sql="truncate total_loans"
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    print("truncated")
    table='users'
    sql="select memno from "+ table
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    list_of_cols=[]
    list_of_values=[]
    list_of_amounts=[]
    with con:
        rows = cur.fetchall()
        try:
            list_of_cols=list(rows[0].keys())
        except Exception as e:
            list_of_cols=["empty","empty"]
        for row in rows:
            kop=list(row.values())
            list_of_values.append(kop)
    table="loan"
    print(list_of_values)
    for x  in list_of_values:
        x=x[0]
        print(x)
        sql="select sum(amount) from "+ table +" where memno='"+x+"'"
        con = connect()
        cur = con.cursor()
        cur.execute(sql)
        list_of_cols=[]
        with con:
            rows = cur.fetchall()
            try:
                list_of_cols=list(rows[0].keys())
            except Exception as e:
                list_of_cols=["empty","empty"]
            for row in rows:
                toto=list(row.values())
                tt=toto[0]
                print(tt)
                if tt==None:
                    tt=0
                list_of_amounts.append(tt)
    y=0
    print(list_of_amounts)
    print(list_of_values)
    for x  in list_of_values:
        x=x[0]
        sql="insert into total_loans values('"+ x +"','"+ str(list_of_amounts[y])+"');"
        print(sql)
        y+=1
        con = connect()
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print("inserted")

def calc_contribution():
    sql="truncate total_contributions"
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    print("truncated")
    table='users'
    sql="select memno from "+ table
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    list_of_cols=[]
    list_of_values=[]
    list_of_amounts=[]
    with con:
        rows = cur.fetchall()
        try:
            list_of_cols=list(rows[0].keys())
        except Exception as e:
            list_of_cols=["empty","empty"]
        for row in rows:
            kop=list(row.values())
            list_of_values.append(kop)
    table="contribution"
    print(list_of_values)
    for x  in list_of_values:
        x=x[0]
        print(x)
        sql="select sum(amount) from "+ table +" where memno='"+x+"'"
        con = connect()
        cur = con.cursor()
        cur.execute(sql)
        list_of_cols=[]
        with con:
            rows = cur.fetchall()
            try:
                list_of_cols=list(rows[0].keys())
            except Exception as e:
                list_of_cols=["empty","empty"]
            for row in rows:
                toto=list(row.values())
                tt=toto[0]
                print(tt)
                if tt==None:
                    tt=0
                list_of_amounts.append(tt)
    y=0
    print(list_of_amounts)
    print(list_of_values)
    for x  in list_of_values:
        x=x[0]
        sql="insert into total_contributions values('"+ x +"','"+ str(list_of_amounts[y])+"');"
        print(sql)
        y+=1
        con = connect()
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print("inserted")

def calc_account():
    table="total_contributions"
    sql="select sum(amount) from "+ table +""
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    list_of_cols=[]
    with con:
        rows = cur.fetchall()
        try:
            list_of_cols=list(rows[0].keys())
        except Exception as e:
            list_of_cols=["empty","empty"]
        for row in rows:
            toto=list(row.values())
            tt=toto[0]
            print(tt)
            totalcontrib=tt
    sql="truncate total_dividends"
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    print("truncated")
    table='users'
    sql="select memno from "+ table
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    list_of_cols=[]
    list_of_values=[]
    list_of_amounts=[]
    with con:
        rows = cur.fetchall()
        try:
            list_of_cols=list(rows[0].keys())
        except Exception as e:
            list_of_cols=["empty","empty"]
        for row in rows:
            kop=list(row.values())
            list_of_values.append(kop)
    table="contribution"
    print(list_of_values)
    for x  in list_of_values:
        x=x[0]
        print(x)
        sql="select sum(amount) from "+ table +" where memno='"+x+"'"
        con = connect()
        cur = con.cursor()
        cur.execute(sql)
        list_of_cols=[]
        with con:
            rows = cur.fetchall()
            try:
                list_of_cols=list(rows[0].keys())
            except Exception as e:
                list_of_cols=["empty","empty"]
            try:
                for row in rows:
                    toto=list(row.values())
                    tt=toto[0]
                    print(tt)
                    if tt==None:
                        tt=0
                    list_of_amounts.append(tt)
            except Exception as e:
                list_of_amounts.append(1)
    y=0
    print(list_of_amounts)
    print(list_of_values)
    for x  in list_of_values:
        x=x[0]
        kkk=list_of_amounts[y]/totalcontrib
        kkk=kkk*100
        sql="insert into total_dividends values('"+ x +"','"+ str(kkk)+"');"
        print(sql)
        y+=1
        con = connect()
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print("inserted")
    
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


@app.route('/dashboard/dividends')
def div():
    session["table"]="total_dividends"
    read_data()
    return (render_template('dividends.html'))

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
            rd="/dashboard/"+session["table"]+"s/updates/"+kop[0]
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
        calc_loans()
        print("loans")
        calc_contribution()
        print("contribution")
        calc_account()
        print("account")
        con = connect()
        cur = con.cursor()
        table="total_dividends"
        cur.execute("SELECT * FROM "+str(table).lower())
        complist=[['Member id','Contribution']]
        with con:
            rows = cur.fetchall()
            try:
                list_of_cols=list(rows[0].keys())
            except Exception as e:
                list_of_cols=["empty","empty"]
            for row in rows:
                kop=list(row.values())
                st=str(kop[0])
                rd=kop[1]
                #st="'"+st+"'"
                #rd="'"+rd+"'"
                mnm=[st,rd]
                complist.append(mnm)
                con = connect()
        cur = con.cursor()
        table="total_loans"
        cur.execute("SELECT * FROM "+str(table).lower())
        complistx=[['Member id','Loans']]
        with con:
            rows = cur.fetchall()
            try:
                list_of_cols=list(rows[0].keys())
            except Exception as e:
                list_of_cols=["empty","empty"]
            for row in rows:
                kop=list(row.values())
                st=str(kop[0])
                rd=kop[1]
                #st="'"+st+"'"
                #rd="'"+rd+"'"
                mnm=[st,rd]
                complistx.append(mnm)
        session["complist"]=str(complist)
        session["complistx"]=str(complistx)
        return (render_template('dashboard.html'))


@app.route('/dashboard/members', methods=['GET', 'POST'])
@is_logged_in
def members():
    if request.method == 'POST':
        k=str(time.time())
        k=k.split(".")
        mo="".join(k)
        mo=str(int(int(mo)/3))
        print(mo)
        mo=mo+str(randint(0, 19))
        mo=mo[-8:]
        mo=mo[::-1]
        arr=[mo,request.form["name"],request.form["email"],request.form["phone"],request.form["desc"],request.form["cred"]]
        print(arr)
        create_data(arr)
        return (redirect(url_for('members')))
    else:
        h="localhost"
        u="root"
        p="Black11060"
        d="sacco_plus"
        set_db(h,u,p,d)
        connect()
        session["table"]="members"
        read_data()
        session["cond"]="Memno = '"
        return (render_template('members.html'))

@app.route('/dashboard/contributions', methods=['GET', 'POST'])
@is_logged_in
def contributions():
    if request.method == 'POST':
        k=str(time.time())
        k=k.split(".")
        mo="".join(k)
        mo=str(int(int(mo)/3))
        print(mo)
        mo=mo+str(randint(0, 19))
        mo=mo[-5:]
        mo=mo[::-1]
        mo="CONT"+mo
        arr=[mo,request.form["id"],request.form["date"],request.form["amount"]]
        print(arr)
        create_data(arr)
        return (redirect(url_for('contributions')))
    else:
        h="localhost"
        u="root"
        p="Black11060"
        d="sacco_plus"
        set_db(h,u,p,d)
        connect()
        session["table"]="contribution"
        read_data()
        print("io")
        session["cond"]="contno = '"
        return (render_template('contributions.html'))

@app.route('/d/<string:name>')
@is_logged_in
def delete(name):
    cond=session["cond"]+name+"'"
    del_data(cond)
    return(redirect(url_for("members")))


@app.route('/dashboard/memberss/updates/<string:name>', methods=['GET', 'POST'])
@is_logged_in
def update(name):
    cond="Memno = '"+name+"'"
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
@app.route('/dashboard/contributions/updates/<string:name>', methods=['GET', 'POST'])
@is_logged_in
def contr(name):
    cond="contno = '"+name+"'"
    session["table"]="contribution"
    if request.method == 'POST':
        arr=[name,request.form["memno"],request.form["date"],request.form["amount"]]
        update_data(arr,cond)
        return (redirect(url_for('contributions')))
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
        session["memno"]= list_of_value[1]
        session["date"]= list_of_value[2]
        session["amount"]= list_of_value[3]
        return(render_template("contribupdate.html"))


@app.route('/dashboard/loans/updates/<string:name>', methods=['GET', 'POST'])
@is_logged_in
def lns(name):
    cond="loanid = '"+name+"'"
    session["table"]="loan"
    if request.method == 'POST':
        arr=[name,session["memno"],request.form["date"],request.form["amount"],request.form["status"]]
        update_data(arr,cond)
        return (redirect(url_for('loans')))
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
        session["memno"]= list_of_value[1]
        session["date"]= list_of_value[2]
        session["amount"]= list_of_value[3]
        session["status"]= list_of_value[4]
        
        return(render_template("loanupdate.html"))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        #conn = sqlite3.connect('static/login.db')
        #c = conn.cursor()
        username = request.form['username']
        print(username)
        password = request.form['password']
        email = request.form['email']
        subscription = request.form['subscription']
        h="localhost"
        u="root"
        p="Black11060"
        d="sacco_plus"
        set_db(h,u,p,d)
        connect()
        md5_object = hashlib.md5()
        string = password.encode("utf-8")
        md5_object.update(string)
        password = md5_object.hexdigest()

        fullstring = "'" + str(username) + "'" + "," + "'" + str(password) + "'" + "," + "'" + str(
            subscription) + "'" + "," + "'" + str(email) + "'"
        print(fullstring)
        #c.execute("INSERT INTO users VALUES(" + str(fullstring) + ")")
        #conn.commit()
        #conn.close
        sql="INSERT INTO users VALUES(" + str(fullstring) + ")"
        con = connect()
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        return redirect(url_for('login'))

    return render_template('register.html', error=error)

@app.route('/dashboard/loans', methods=['GET', 'POST'])
def loans():
    table="loan"
    session["table"]="loan"
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
            rd="/dashboard/"+session["table"]+"s/updates/"+kop[0]
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
    session["cond"]="loanid = '"
    return render_template('loans.html')
@app.route('/users', methods=['GET', 'POST'])
def usrs():
    if request.method == 'POST':
        k=str(time.time())
        k=k.split(".")
        mo="".join(k)
        mo=str(int(int(mo)/3))
        print(mo)
        mo=mo+str(randint(0, 19))
        mo=mo[-8:]
        mo=mo[::-1]
        status="waiting"
        memno=session["memno"]
        arr=[mo,memno,request.form["date"],request.form["amount"],status]
        print(arr)
        session["table"]="loan"
        create_data(arr)
        return (redirect(url_for('usrs')))
    calc_ac()
    table="contribution"
    session["table"]="contribution"
    list_of_values=[]
    list_of_cols=[]
    lit_of_dels=[]
    list_of_updates=[]
    con = connect()
    cur = con.cursor()
    cvx="SELECT * FROM "+str(table).lower()+" where memno='"+str(session['memno'])+"'"
    print(cvx)
    cur.execute(cvx)
    print("executered")
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
            rd="/dashboard/"+session["table"]+"s/updates/"+kop[0]
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

    table="loan"
    session["table"]="loan"
    list_of_values=[]
    list_of_cols=[]
    lit_of_dels=[]
    list_of_updates=[]
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM "+str(table).lower()+" where memno='"+str(session['memno'])+"'")
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
            rd="/dashboard/"+session["table"]+"s/updates/"+kop[0]
            list_of_updates.append(rd)
            lit_of_dels.append(st)
    if list_of_values==[]:
        list_of_values=[['UH OH ;)'],['This table is empty']]
    session["colsx"]= list_of_cols
    session["colsxyx"]= len(list_of_cols)
    session["valsx"]= list_of_values
    session["valsxyx"]= len(list_of_values)
    session["delsx"]= lit_of_dels
    session["updatesx"]= list_of_updates
    return render_template('users.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    h="localhost"
    u="root"
    p="Black11060"
    d="sacco_plus"
    set_db(h,u,p,d)
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
            session['usrname'] = username
            con = connect()
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row["username"]
                    dbsub = row["role"]
                    if dbUser == username:
                        role = dbsub
                        cv=row["memno"]
                        session['memno']=cv
            session['role'] = role
            if role=="Admin":
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('usrs'))
            
    return render_template('login.html', error=error)


def validate(username, password):
    con = connect()
    completion = False
    md5_object = hashlib.md5()
    string = password.encode("utf-8")
    md5_object.update(string)
    password = md5_object.hexdigest()
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            dbUser = row["username"]
            dbPass = row["password"]
            if dbUser == username:
                completion = check_password(dbPass, password)
    return completion


def check_password(hashed_password, user_password):
    return hashed_password == user_password

@app.route("/testr")
def testr():
    calc_loans()
    calc_contribution()
    calc_account()
    return("kooo")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port= 1000)
