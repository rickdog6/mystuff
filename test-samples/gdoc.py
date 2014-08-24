#!/usr/bin/env python

#This is a script to post information about a headless system to a google spreadsheet for access and logging
#You will need to create a google spreadsheet in google drive the name is not important as it is referenced by the 
#unique key below but the first row (headers) must match the headers in the dictionary lower down.
#my headers are    ///   time   date   locip   pubip   uptime      ///      google inserts into the first match of each
#This script depends on the google python data API (sudo apt-get install python-gdata)

#I have this set up in cron to run hourly which also means it runs just after boot also.
#A cool feature of google docs is that you can subscirbe to document changes which means you will get an email everytime its updated
#(if you subscribe that is)
#For the next step I will probably store all the config in an ini file and the IP's in a text file then I can compare the IP's and only
#update the spreadsheet if they have changed.

import time
import gdata.spreadsheet.service
import os
import subprocess
import re

email = 'rickdog6@gmail.com'    #this is your full gmail address
password = 'crotalus'            #this is your gmail password
IP_WEBSITE = "http://myip.xname.org"   #this is the url i am using to get the public IP

spreadsheet_key = '0AmoSLvVqU5mvdGtlLVUyS0ZlcGtCY0V6T2t0OHJ6d3c' # Find this value in the spreadsheet url with 'key=XXX' and copy XXX below
worksheet_id = '1' #This is the worksheet ID not sure how this works I "borrowed" this from one of the examples

def getip(): #Gets the local IP using the hostname -I method
   command = "hostname -I"
   proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
   output = proc.stdout.read()
   output = output.replace("\n","")
   return output
   
def getpubip(): #Gets the public IP by doing a get of the webpage below
   url = "myip.xname.org:80"
   import httplib, urllib
   headers = {"Content-type": "HTML"}
   params = ''
   conn = httplib.HTTPConnection(url)
   conn.request("GET", "/")
   response = conn.getresponse()
   message = response.status, response.reason
   message = str(message) 
   #print message #print http responce for debugging
   ip = response.read()
   ip = ip.replace("\n","") #get rid of new line character (may not be necessary)
   return ip
   
def uptime(): #gets uptime load average etc could split it out easily if needed it is comma seperated
   command = "uptime"
   proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
   output = proc.stdout.read()
   output = output.replace("\n","") #get rid of new line character (may not be necessary)
   return output
   
def temp():
   command = "sensors"
   proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
   output = proc.stdout.read()
   output = output.replace("\n","") #remove returns
   return output

def main():
   spr_client = gdata.spreadsheet.service.SpreadsheetsService()
   spr_client.email = email
   spr_client.password = password
   #spr_client.source = 'rick-laptop'
   spr_client.ProgrammaticLogin()

   #publip=getpubip() # it doesnt seem to like it if I try to return the output directly into the dictionary so I stick in a variable first
   #loclip=getip()
   #uptim=uptime()
   #tempur=temp()
   #print uptim #print for debugging

   dict = {} # match headers in spreadsheet exactly
   dict['date'] = time.strftime('%m/%d/%Y')
   dict['time'] = time.strftime('%H:%M:%S')
   dict['pubip'] = getpubip()
   dict['locip'] = getip()
   dict['uptime'] = uptime()
   dict['temp'] = temp()

   entry = spr_client.InsertRow(dict, spreadsheet_key, worksheet_id)
#   if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
#     print "Insert row succeeded."
#   else:
#      return 0

if __name__ == '__main__':
#   while True:
      try:
         main()
#         time.sleep(30)
      except:
         print "Insert Row Failed!"
#         time.sleep(30)
