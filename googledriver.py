#!/usr/bin/env python3

from pydrive.auth import GoogleAuth    #version 1.0.1 of later...needs to be manually pulled from github...via h$
from pydrive.drive import GoogleDrive
import time
import csv

picebergID = '0B9ffTjUEqeFEY0RHRWtMSGJGNUU'  #piceberg1.csv fileID


#get the current csv from the GDrive and append the date and time and upload the new file to Gdrive
gauth = GoogleAuth()

# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()

# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

##Download the prior file that we will append the new data to
##Added the convert parameter to download the google sheet as a CSV file
#current=drive.CreateFile({'id': picebergID,'convert': False, mimetype:'text/csv'})
##add the desired mimetype of CSV for the downloaded file
#current.GetContentFile('piceberg1.csv', mimetype='text/csv')

file1 = drive.CreateFile({'title':'piceberg1.csv', 'id': picebergID}) #open a new file on the GDrive

file1.SetContentFile('record.csv') #sets the file content to the CSV file created above from the working directo$

file1.Upload({'convert': False}) #upload the file and convert to google sheet format

picebergID=file1['id']
