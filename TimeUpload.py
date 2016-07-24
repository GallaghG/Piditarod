from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import time
import csv

timeID='0B9ffTjUEqeFEZ28zdTRhMlJlY0k'
for i in range(10):
#get the curret time
    date_time=time.asctime()
    date_time_split=date_time.split(' ')  #gives a list with the date and time components
    time_only=date_time_split[3] # gives just the current time
    date_only = str(date_time_split[1] + ' ' + date_time_split[2]+' ' +date_time_split[4])

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
    #Download the prior file that we will append the new data to
    current=drive.CreateFile({'id': timeID})
    current.GetContentFile('current.csv')
    
    #delete the prior data file to keep these files from accumulating on the GDrive
    #current.DeleteFile(timeID)
    

    with open('current.csv', 'a') as csvfile:
        fieldnames = ['Time', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Time': time_only, 'Date': date_only})
    csvfile.close()
       
    file1 = drive.CreateFile({'title':'time.csv', 'id': timeID}) #open a new file on the GDrive
    file1.SetContentFile('current.csv') #sets the file content to the CSV file created above from the working directory
    file1.Upload() #upload the file
    timeID=file1['id']

    time.sleep(30) #pause for 30seconds
