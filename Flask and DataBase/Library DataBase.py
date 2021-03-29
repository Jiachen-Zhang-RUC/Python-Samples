from flask import request, redirect
from flask import Flask
from flask import Blueprint, render_template, send_file
import pyodbc
from datetime import datetime
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from flask import Flask
import pymysql

from flask import flash
from flask import g

app = Flask(__name__)

gl = {'name': 'Default'}
guo = {'updateop': 'Default'}
guc = {'updatecon': 'Default'}
guoo = {'updateopop': 'Default'}
gucc = {'updateconcon': 'Default'}
gqn = {'queryne': 'Default'}
gqo = {'queryop': 'Default'}
glb = {'nameb': 'Default'}
guob = {'updateopb': 'Default'}
gucb = {'updateconb': 'Default'}
guoob = {'updateopopb': 'Default'}
guccb = {'updateconconb': 'Default'}
gqnb = {'queryneb': 'Default'}
gqob = {'queryopb': 'Default'}

@app.route('/')
def index1():
    msg = "Hello!"
    return render_template("realfirstpage.html", data=msg)

@app.route('/addmin')
def index2():
    msg = "Hello!"
    return render_template("addminfirstpage.html", data=msg)

@app.route('/user')
def index3():
    msg = "Hello!"
    return render_template("userfirstpage.html", data=msg)

@app.route('/insert')
def insertinto():
    return send_file("insert1.html")


@app.route('/insert1', methods=['POST'])
def insert():
    student_idinsert = request.form['student_id']
    student_nameinsert = request.form['student_name']
    student_sexinsert = request.form['student_sex']
    student_ageinsert = request.form['student_age']
    student_majorinsert = request.form['student_major']
    student_gradeinsert = request.form['student_grade']
    student_borrownuminsert = request.form['student_borrower']
    student_credibilityinsert = request.form['student_credibility']

    print("student_idinsert: " + student_idinsert + "; student_nameinsert: " + student_nameinsert)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """insert into student values 
        ("""
    tsql = tsql + student_idinsert
    tsql = tsql + ",'"
    tsql = tsql + student_nameinsert
    tsql = tsql + "','"
    tsql = tsql + student_sexinsert
    tsql = tsql + "',"
    tsql = tsql + student_ageinsert
    tsql = tsql + ",'"
    tsql = tsql + student_majorinsert
    tsql = tsql + "','"
    tsql = tsql + student_gradeinsert
    tsql = tsql + "',"
    tsql = tsql + student_borrownuminsert
    tsql = tsql + ","
    tsql = tsql + student_credibilityinsert
    tsql = tsql + ");"
    print(tsql)
    '''tsql = "INSERT INTO student(user_name, user_email, user_password) VALUES(%s, %s, %s)"
    data = (_name, _email, _hashed_password,)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, data)'''

    cursor.execute(tsql)
    cnxn.commit()
    print('User added successfully!')
    msg = "insert finished"
    return render_template("realfirstpage.html", data=msg)


@app.route('/delete')
def deletefrom():
    return send_file("delete1.html")


@app.route('/delete1', methods=['POST'])
def deletionoption():
    deleteoption = request.form['delete_option']
    gl['name'] = deleteoption
    print("deleteoption: " + deleteoption)
    if (deleteoption == 'stu_id' or deleteoption == 'borrow_num' or deleteoption == 'stu_credibility'):
        return send_file("delete2.html")
    else:
        return send_file("delete3.html")

@app.route('/delete2', methods=['POST'])
def deletionoptionnumber():

    option = gl['name']
    deletecondinumber = request.form['delete_conditionnumber']

    print("delete: " + option + " " + deletecondinumber)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """delete from student 
            where """
    tsql = tsql + option
    tsql = tsql + " = "
    tsql = tsql + deletecondinumber
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('Usernum deleted successfully!')
    msg1 = "deletenum finished"
    return render_template("realfirstpage.html", data=msg1)


@app.route('/delete3', methods=['POST'])
def deletionoptiontext():

    option3 = gl['name']
    deleteconditext = request.form['delete_conditiontext']

    print("delete: " + option3 + " " + deleteconditext)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """delete from student 
            where """
    tsql = tsql + option3
    tsql = tsql + " = '"
    tsql = tsql + deleteconditext
    tsql = tsql + "';"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('Usertext deleted successfully!')
    msg2 = "deletetext finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/update')
def updateitem():
    print("/update")
    return send_file("update1.html")

@app.route('/update1', methods=['POST'])
def updateresultoption():
    print("/update1.1")
    updateoption = request.form['update_option']
    print("/update1.2")
    updatecondition = request.form['update_condition']
    print("/update1.3")
    guo['updateop'] = updateoption
    guc['updatecon'] = updatecondition

    print("updateoption: " + updateoption + "  updatecondition: " + updatecondition)
    if ((updateoption == 'stu_id' or updateoption == 'borrow_num' or updateoption == 'stu_credibility')and (updatecondition == 'stu_id' or updatecondition == 'borrow_num' or updatecondition == 'stu_credibility')):
        return send_file("update2.html")
    elif (updateoption == 'stu_id' or updateoption == 'borrow_num' or updateoption == 'stu_credibility'):
        return send_file("update3.html")
    elif (updatecondition == 'stu_id' or updatecondition == 'borrow_num' or updatecondition == 'stu_credibility'):
        return send_file("update4.html")
    else:
        return send_file("update5.html")


@app.route('/update2', methods=['POST'])
def updatenumnum():

    option2 = guo['updateop']
    condition2 = guc['updatecon']
    updateoptionnum = request.form['update_optionnumber']
    updateconditionnum = request.form['update_conditionnumber']
    print("uppate option: " + option2 + " " + updateoptionnum + "update condition: " + condition2 + " " + updateconditionnum)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """update student 
                set """
    tsql = tsql + option2
    tsql = tsql + " = "
    tsql = tsql + updateoptionnum
    tsql = tsql + " where "
    tsql = tsql + condition2
    tsql = tsql + " = "
    tsql = tsql + updateconditionnum
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('Updated successfully!')
    msg2 = "updatenumnum finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/update3', methods=['POST'])
def updatenumtext():
    option3 = guo['updateop']
    condition3 = guc['updatecon']
    updateoptionnum = request.form['update_optionnumber']
    updateconditiontext = request.form['update_conditiontext']
    print("uppate option: " + option3 + " " + updateoptionnum + "update condition: " + condition3 + " " + updateconditiontext)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """update student 
                set """
    tsql = tsql + option3
    tsql = tsql + " = "
    tsql = tsql + updateoptionnum
    tsql = tsql + " where "
    tsql = tsql + condition3
    tsql = tsql + " = '"
    tsql = tsql + updateconditiontext
    tsql = tsql + "';"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('Updated successfully!')
    msg2 = "updatenumtext finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/update4', methods=['POST'])
def updatetextnum():
    option4 = guo['updateop']
    condition4 = guc['updatecon']
    updateoptiontext = request.form['update_optiontext']
    updateconditionnum = request.form['update_conditionnumber']
    print("uppate option: " + option4 + " " + updateoptiontext + "update condition: " + condition4 + " " + updateconditionnum)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """update student 
                set """
    tsql = tsql + option4
    tsql = tsql + " = '"
    tsql = tsql + updateoptiontext
    tsql = tsql + "' where "
    tsql = tsql + condition4
    tsql = tsql + " = "
    tsql = tsql + updateconditionnum
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('Updated successfully!')
    msg2 = "updatenumnum finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/update5', methods=['POST'])
def updatetexttext():
    option5 = guo['updateop']
    condition5 = guc['updatecon']
    updateoptiontext = request.form['update_optiontext']
    updateconditiontext = request.form['update_conditiontext']
    print("uppate option: " + option5 + " " + updateoptiontext + "update condition: " + condition5 + " " + updateconditiontext)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """update student 
                set """
    tsql = tsql + option5
    tsql = tsql + " = '"
    tsql = tsql + updateoptiontext
    tsql = tsql + "' where "
    tsql = tsql + condition5
    tsql = tsql + " = '"
    tsql = tsql + updateconditiontext
    tsql = tsql + "';"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('Updated successfully!')
    msg2 = "updatenumnum finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/query')
def query():
    return send_file("query1.html")

@app.route('/query1', methods=['POST'])
def queryoption():
    queryoption = request.form['query_option']
    gqo['queryop'] = queryoption
    print("query: " + queryoption)
    if (queryoption == 'stu_id' or queryoption == 'borrow_num' or queryoption == 'stu_credibility'):
        return send_file("query2.html")
    else:
        return send_file("query3.html")

@app.route('/query2', methods=['POST'])
def querynum():
    queryoption2 = gqo['queryop']
    query_num = request.form['querynum']
    print("query condition: " + queryoption2 + " = " + query_num)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()
    print("hereplease")
    tsql = "select * from student where "
    tsql = tsql + queryoption2
    tsql = tsql + " = "
    tsql = tsql + query_num
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    content = cursor.fetchall()
    return render_template('querytables.html', u = content)


@app.route('/query3', methods=['POST'])
def querytext():

    queryoption3 = gqo['queryop']
    query_text = request.form['querytext']
    print("query condition: " + queryoption3 + " = " + query_text)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = "select * from student where "
    tsql = tsql + queryoption3
    tsql = tsql + " = '"
    tsql = tsql + query_text
    tsql = tsql + "';"

    print(tsql)

    cursor.execute(tsql)
    content = cursor.fetchall()
    return render_template('querytables.html', u=content)

#书籍


@app.route('/insertbook')
def insertintobook():
    return send_file("insertbook1.html")

@app.route('/insertbook1', methods=['POST'])
def insertbook():
    book_idinsert = request.form['book_id']
    book_nameinsert = request.form['book_name']
    book_authorinsert = request.form['book_author']
    book_companyinsert = request.form['book_company']
    book_sortinsert = request.form['book_sort']
    book_numinsert = request.form['book_numer']
    borrow_timesinsert = request.form['borrow_times']

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """insert into book values 
        ("""
    tsql = tsql + book_idinsert
    tsql = tsql + ",'"
    tsql = tsql + book_nameinsert
    tsql = tsql + "','"
    tsql = tsql + book_authorinsert
    tsql = tsql + "','"
    tsql = tsql + book_companyinsert
    tsql = tsql + "','"
    tsql = tsql + book_sortinsert
    tsql = tsql + "',"
    tsql = tsql + book_numinsert
    tsql = tsql + ", "
    tsql = tsql + borrow_timesinsert
    tsql = tsql + ");"
    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()
    print('Book added successfully!')
    msg = "insert finished"
    return render_template("realfirstpage.html", data=msg)

@app.route('/deletebook')
def deletefrombook():
    return send_file("deletebook1.html")

@app.route('/deletebook1', methods=['POST'])
def deletionoptionbook():
    deleteoption = request.form['delete_option']
    glb['nameb'] = deleteoption
    print("deleteoption: " + deleteoption)
    if (deleteoption == 'book_id' or deleteoption == 'book_num' or deleteoption == 'borrow_times'):
        return send_file("deletebook2.html")
    else:
        return send_file("deletebook3.html")

@app.route('/deletebook2', methods=['POST'])
def deletionoptionnumberbook():

    option = glb['nameb']
    deletecondinumber = request.form['delete_conditionnumber']

    print("delete: " + option + " " + deletecondinumber)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """delete from book where """
    tsql = tsql + option
    tsql = tsql + " = "
    tsql = tsql + deletecondinumber
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('booknum deleted successfully!')
    msg1 = "delete finished"
    return render_template("realfirstpage.html", data=msg1)


@app.route('/deletebook3', methods=['POST'])
def deletionoptiontextbook():

    option3 = glb['nameb']
    deleteconditext = request.form['delete_conditiontext']

    print("delete: " + option3 + " " + deleteconditext)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """delete from book where """
    tsql = tsql + option3
    tsql = tsql + " = '"
    tsql = tsql + deleteconditext
    tsql = tsql + "';"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('booktext deleted successfully!')
    msg2 = "delete finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/updatebook')
def updateitembook():

    return send_file("updatebook1.html")

@app.route('/updatebook1', methods=['POST'])
def updateresultoptionbook():

    updateoption = request.form['update_option']
    updatecondition = request.form['update_condition']
    guob['updateopb'] = updateoption
    gucb['updateconb'] = updatecondition

    print("updateoption: " + updateoption + "  updatecondition: " + updatecondition)
    if ((updateoption == 'book_id' or updateoption == 'book_num' or updateoption == 'borrow_times')and (updatecondition == 'book_id' or updatecondition == 'book_num' or updatecondition == 'borrow_times')):
        return send_file("updatebook2.html")
    elif (updateoption == 'book_id' or updateoption == 'book_num' or updateoption == 'borrow_times'):
        return send_file("updatebook3.html")
    elif (updatecondition == 'book_id' or updatecondition == 'book_num' or updatecondition == 'borrow_times'):
        return send_file("updatebook4.html")
    else:
        return send_file("updatebook5.html")

@app.route('/updatebook2', methods=['POST'])
def updatenumnumbook():

    option2 = guob['updateopb']
    condition2 = gucb['updateconb']
    updateoptionnum = request.form['update_optionnumber']
    updateconditionnum = request.form['update_conditionnumber']
    print("update option: " + option2 + " " + updateoptionnum + "update condition: " + condition2 + " " + updateconditionnum)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """update book 
                set """
    tsql = tsql + option2
    tsql = tsql + " = "
    tsql = tsql + updateoptionnum
    tsql = tsql + " where "
    tsql = tsql + condition2
    tsql = tsql + " = "
    tsql = tsql + updateconditionnum
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('Updated successfully!')
    msg2 = "update finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/updatebook3', methods=['POST'])
def updatenumtextbook():
    option3 = guob['updateopb']
    condition3 = gucb['updateconb']
    updateoptionnum = request.form['update_optionnumber']
    updateconditiontext = request.form['update_conditiontext']
    print("uppate option: " + option3 + " " + updateoptionnum + "update condition: " + condition3 + " " + updateconditiontext)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """update book 
                set """
    tsql = tsql + option3
    tsql = tsql + " = "
    tsql = tsql + updateoptionnum
    tsql = tsql + " where "
    tsql = tsql + condition3
    tsql = tsql + " = '"
    tsql = tsql + updateconditiontext
    tsql = tsql + "';"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('Updated successfully!')
    msg2 = "update finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/updatebook4', methods=['POST'])
def updatetextnumbook():
    option4 = guob['updateopb']
    condition4 = gucb['updateconb']
    updateoptiontext = request.form['update_optiontext']
    updateconditionnum = request.form['update_conditionnumber']
    print("uppate option: " + option4 + " " + updateoptiontext + "update condition: " + condition4 + " " + updateconditionnum)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """update book 
                set """
    tsql = tsql + option4
    tsql = tsql + " = '"
    tsql = tsql + updateoptiontext
    tsql = tsql + "' where "
    tsql = tsql + condition4
    tsql = tsql + " = "
    tsql = tsql + updateconditionnum
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('Updated successfully!')
    msg2 = "update finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/updatebook5', methods=['POST'])
def updatetexttextbook():
    option5 = guob['updateopb']
    condition5 = gucb['updateconb']
    updateoptiontext = request.form['update_optiontext']
    updateconditiontext = request.form['update_conditiontext']
    print("uppate option: " + option5 + " " + updateoptiontext + "update condition: " + condition5 + " " + updateconditiontext)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """update book 
                set """
    tsql = tsql + option5
    tsql = tsql + " = '"
    tsql = tsql + updateoptiontext
    tsql = tsql + "' where "
    tsql = tsql + condition5
    tsql = tsql + " = '"
    tsql = tsql + updateconditiontext
    tsql = tsql + "';"

    print(tsql)


    cursor.execute(tsql)
    cnxn.commit()

    print('Updated successfully!')
    msg2 = "update finished"
    return render_template("realfirstpage.html", data=msg2)

@app.route('/querybook')
def querybook():
    return send_file("querybook1.html")

@app.route('/querybook1', methods=['POST'])
def queryoptionbook():
    queryoption = request.form['query_option']
    gqob['queryopb'] = queryoption
    print("query: " + queryoption)
    if (queryoption == 'book_id' or queryoption == 'book_num' or queryoption == 'borrow_times'):
        return send_file("querybook2.html")
    else:
        return send_file("querybook3.html")

@app.route('/querybook2', methods=['POST'])
def querynumbook():
    queryoption2 = gqob['queryopb']
    query_num = request.form['querynum']
    print("query condition: " + queryoption2 + " = " + query_num)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = "select * from book where "
    tsql = tsql + queryoption2
    tsql = tsql + " = "
    tsql = tsql + query_num
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    content = cursor.fetchall()
    return render_template('querytablesbook.html', u = content)

@app.route('/querybook3', methods=['POST'])
def querytextbook():

    queryoption3 = gqob['queryopb']
    query_text = request.form['querytext']
    print("query condition: " + queryoption3 + " = " + query_text)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = "select * from book where "
    tsql = tsql + queryoption3
    tsql = tsql + " = '"
    tsql = tsql + query_text
    tsql = tsql + "';"

    print(tsql)


    cursor.execute(tsql)
    content = cursor.fetchall()
    return render_template('querytablesbook.html', u = content)

@app.route('/querybookorder1')
def queryorderbook1():
    return send_file("queryorderbook4.html")

@app.route('/querybookorder2', methods=['POST'])
def queryorderbook():

    query_x = request.form['query_orderx']
    query_y = request.form['query_ordery']
    print("query condition: " + query_x + " = " + query_y)

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = "select "
    tsql = tsql + query_x
    tsql = tsql + ", "
    tsql = tsql + query_y
    tsql = tsql + " from book order by "
    tsql = tsql + query_y
    tsql = tsql + " DESC;"

    print(tsql)

    cursor.execute(tsql)
    content = cursor.fetchall()

    x_list = []
    y_list = []

    with cursor.execute(tsql):
        row = cursor.fetchone()
        while row:
            temp = row[0]
            #temp = temp.strip()
            x_list.append(temp)
            print(row[0])
            temp = row[1]
            temp = int(temp)  # temp.to_integral_value()
            y_list.append(temp)
            print(row[1])
            row = cursor.fetchone()

    print(x_list)
    print(y_list)

    context = {
        'name': x_list,
        'shu': y_list
    }
    return render_template('queryordertables.html', u = content, data_x = query_x, data_y = query_y, **context)


#借书信息
@app.route('/insertborr')
def insertintoborr():
    return send_file("insertborr1.html")


@app.route('/insertborr1', methods=['POST'])
def insertborr():
    student_idinsert = request.form['student_id']
    book_idinsert = request.form['book_id']
    borrow_dateinsert = request.form['borrow_date']
    expreturn_dateinsert = request.form['expectreturn_date']

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """insert into borrow_table values 
        ("""
    tsql = tsql + student_idinsert
    tsql = tsql + ", "
    tsql = tsql + book_idinsert
    tsql = tsql + ", "
    tsql = tsql + borrow_dateinsert
    tsql = tsql + ", "
    tsql = tsql + expreturn_dateinsert
    tsql = tsql + ");"
    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()
    print('成功添加借书信息')
    msg = "成功添加借书信息"
    return render_template("realfirstpage.html", data=msg)


@app.route('/deleteborr')
def deletefromborr():
    return send_file("deleteborr2.html")

@app.route('/deleteborr2', methods=['POST'])
def deletionoptionnumberborr():

    deletecondistuid = request.form['delete_conditionnumber1']
    deletecondibookid = request.form['delete_conditionnumber2']
    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """delete from borrow_table 
            where stu_id = """
    tsql = tsql + deletecondistuid
    tsql = tsql + " and book_id = "
    tsql = tsql + deletecondibookid
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('成功删除了满足条件的借书信息')
    msg1 = "成功删除了满足条件的借书信息"
    return render_template("realfirstpage.html", data=msg1)

@app.route('/updateborr')
def updateitemborr():

    return send_file("updateborr2.html")

@app.route('/updateborr2', methods=['POST'])
def updatenumnumborr():

    updatestuid = request.form['update_optionnumber1']
    updatebookid = request.form['update_optionnumber2']
    updatereturndate = request.form['update_conditionnumber']

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """update borrow_table 
                set expect_return_date = """
    tsql = tsql + updatereturndate
    tsql = tsql + " where stu_id = "
    tsql = tsql + updatestuid
    tsql = tsql + " and book_id = "
    tsql = tsql + updatebookid
    tsql = tsql + " ;"

    print(tsql)
    cursor.execute(tsql)
    cnxn.commit()

    print('成功修改预计还书日期')
    msg2 = "成功修改预计还书日期，续借成功"
    return render_template("realfirstpage.html", data=msg2)


@app.route('/queryborr')
def queryborr():
    return send_file("queryborr2.html")

@app.route('/queryborr2', methods=['POST'])
def querynumborr():

    query_stuid = request.form['querynum']

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()
    print("hereplease")
    tsql = "select * from borrow_table where stu_id = "
    tsql = tsql + query_stuid
    tsql = tsql + ";"

    print(tsql)
    cursor.execute(tsql)
    content = cursor.fetchall()
    return render_template('querytables.html', u = content)

#还书信息
@app.route('/insertretu')
def insertintoretu():
    return send_file("insertretu1.html")

@app.route('/insertborr1', methods=['POST'])
def insertretu():
    student_idinsert = request.form['student_id']
    book_idinsert = request.form['book_id']
    borrow_dateinsert = request.form['borrow_date']
    return_dateinsert = request.form['expectreturn_date']

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """insert into return_table values 
        ("""
    tsql = tsql + student_idinsert
    tsql = tsql + ", "
    tsql = tsql + book_idinsert
    tsql = tsql + ", "
    tsql = tsql + borrow_dateinsert
    tsql = tsql + ", "
    tsql = tsql + return_dateinsert
    tsql = tsql + ");"
    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()
    print('成功添加还书信息')
    msg = "成功添加还书信息"
    return render_template("realfirstpage.html", data=msg)


@app.route('/deleteretu')
def deletefromretu():
    return send_file("deleteretu2.html")

@app.route('/deleteretu2', methods=['POST'])
def deletionoptionnumberretu():

    deletecondistuid = request.form['delete_conditionnumber1']
    deletecondibookid = request.form['delete_conditionnumber2']
    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()

    tsql = """delete from return_table 
            where stu_id = """
    tsql = tsql + deletecondistuid
    tsql = tsql + " and book_id = "
    tsql = tsql + deletecondibookid
    tsql = tsql + ";"

    print(tsql)

    cursor.execute(tsql)
    cnxn.commit()

    print('成功删除了满足条件的还书信息')
    msg1 = "成功删除了满足条件的还书信息"
    return render_template("realfirstpage.html", data=msg1)

@app.route('/queryretu')
def queryretu():
    return send_file("queryretu2.html")

@app.route('/queryretu2', methods=['POST'])
def querynumretu():

    query_stuid = request.form['querynum']

    server = 'localhost'
    database = 'books'
    username = 'sa'
    password = 'rootroot'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';CHARSET=GBK')
    cursor = cnxn.cursor()
    tsql = "select * from borrow_table where stu_id = "
    tsql = tsql + query_stuid
    tsql = tsql + ";"

    print(tsql)
    cursor.execute(tsql)
    content = cursor.fetchall()
    return render_template('querytables.html', u = content)

if __name__ == "__main__":
    app.run()

