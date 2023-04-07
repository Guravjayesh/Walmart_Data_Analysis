from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
import datetime

dashboard_blueprint = Blueprint('dashboard_blueprint',__name__)

#todays visitors
@dashboard_blueprint.route('/today-visitors')
def todayVisitors():

    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")

    sqlTodayVisitors = text('SELECT COUNT(*) AS today_visitors from visitor_vlog where date = "'+currentDate+'"')
    resultData = db.engine.execute(sqlTodayVisitors)
    rawData = resultData.fetchall()

    jsonData = jsonify([dict(row) for row in rawData])

    return jsonData

#overall visitors
@dashboard_blueprint.route('/overall-visitors')
def overallVisitors():

    sqlTodayVisitors = text('SELECT COUNT(*) AS overall_visitors from visitor_vlog')
    resultData = db.engine.execute(sqlTodayVisitors)
    rawData = resultData.fetchall()

    jsonData = jsonify([dict(row) for row in rawData])

    return jsonData


#male visitors today
@dashboard_blueprint.route('/male-visitors')
def maleVisitors():
    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")

    sqlTodayVisitors = text('SELECT COUNT(*) AS male_visitors from visitor_vlog where date="'+currentDate+'" and gender =1')
    resultData = db.engine.execute(sqlTodayVisitors)
    rawData = resultData.fetchall()

    jsonData = jsonify([dict(row) for row in rawData])

    return jsonData

#female visitors today
@dashboard_blueprint.route('/female-visitors')
def femaleVisitors():
    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")

    sqlTodayVisitors = text('SELECT COUNT(*) AS female_visitors from visitor_vlog where date="'+currentDate+'" and gender =2')
    resultData = db.engine.execute(sqlTodayVisitors)
    rawData = resultData.fetchall()

    jsonData = jsonify([dict(row) for row in rawData])

    return jsonData

# TABLE DATA

@dashboard_blueprint.route('/table-data')
def tableData():

    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
    x= ''

    for a in range(1,6):
        txtlabel = ''
        if a==1:
            txtlabel='Kids'
        elif a==2:
            txtlabel='Teenagers'
        elif a==3:
            txtlabel='Youngsters'
        elif a==4:
            txtlabel='Adults'
        elif a==5:
            txtlabel='Senior citizens'

        for g in range(1,3):

            # get todays visitors
            
            
            sqlTodayVisitors = text('SELECT COUNT(*) AS today_visitors from visitor_vlog where date = "'+currentDate+'" and gender='+str(g)+' and age_group = '+str(a)+'')
            resultData = db.engine.execute(sqlTodayVisitors)

            rawData = resultData.fetchall()
            ageGroupGenderToday = rawData[0].today_visitors

            # get overall visitors
            
            sqlOverallVisitors = text('SELECT COUNT(*) AS overall_visitors from visitor_vlog where  gender='+str(g)+' and age_group = '+str(a)+'')
            resultOData = db.engine.execute(sqlOverallVisitors)

            rawOData = resultOData.fetchall()
            ageGroupGenderOverall = rawOData[0].overall_visitors

            gText = ''

            if g == 1:
                gText = "Male"

            elif g == 2:
                gText = 'Female'

            x += '{"gender":"'+gText+'","age_group":"'+txtlabel+'","today_visitors":"'+str(ageGroupGenderToday)+'","overall_visitors":"'+str(ageGroupGenderOverall)+'"},'

            # END OF THE INNER FOR LOOP
    # END OF OUTER FOR LOOP

    x= x[:-1]

    jsondata = '['+x+']'
    return jsondata
    # this process is callled as json serialization

# graph
@dashboard_blueprint.route('/graph-data')
def graphData():
    x=''
    for m in range(1,13):
        sqlMonthData = text('SELECT COUNT(*) AS monthly_visitors FROM visitor_vlog where MONTH(date) = "'+str(m)+'"')
        resultData = db.engine.execute(sqlMonthData)
        rawData = resultData.fetchall()
        totalMonthlyVisitors = rawData[0].monthly_visitors

        x+='{"month":"'+str(totalMonthlyVisitors)+'"},'

    x=x[:-1]
    jsonData = '['+x+']'
    return jsonData




