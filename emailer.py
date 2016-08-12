#!/usr/bin/env python3

import csv, time, os, datetime, smtplib

def emailer():
    conn=smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('finbergtempmonitor@gmail.com', 'PASSWORD') #login with the piceberg account

    with open('incident.csv', 'r') as csv:
        lastrow= None
        for lastrow in csv: pass
        incident_date=datetime.datetime.fromtimestamp(int(lastrow.split(',')[0])).strftime('%d-%m-%y')
        incident_time=datetime.datetime.fromtimestamp(int(lastrow.split(',')[0])).strftime('%H:%M:%S')
        incident_temp=float(lastrow.split(',')[1])

    recipients=['name@', 'name@', '#####@messaging.sprintpcs.com']
    message='There may be a problem with freezer, 20E located in bay 260E. On ' + incident_date +' at '+incident_time+  ' the recorded temperature was '+ str(incident_temp) + '. Please check that the door is closed and that everything looks ok.'
    
    conn.sendmail('finbergtempmonitor@gmail.com', recipients, message)
    conn.quit()


emailer()
