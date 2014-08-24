import gdata.spreadsheet.service
import os
import subprocess
import re

email = 'ricktreinen@gmail.com'
password = 'querCus12'

spreadsheet_key = '0AgLeoKLB8vZFdDloN3ZuZUJRMFE3ZFJlejVzdlZiQWc'
worksheet_id = '1'

def temp():
   command = "sensors"
   proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
   output = proc.stdout.read()
   temp_regex = re.compile(r'Core 0:       +(\d+.\d+)\°C')
   matches = re.findall(temp_regex, output)
   temp = float(matches[0])
   return temp
   
def main():
   spr_client = gdata.spreadsheet.service.SpreadsheetsService()
   spr_client.email = email
   spr_client.password = password
   spr_client.ProgrammaticLogin()

   dict = {}
   dict['temp'] = temp()

   entry = spr_client.InsertRow(dict, spreadsheet_key, worksheet_id)

if __name__ == '__main__':
      try:
         main()
      except:
         print "Insert Row Failed!"
