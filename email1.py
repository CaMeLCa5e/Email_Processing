#sending an email using PY

import smtplib

sender =  "jm273606@gmail.com"
recievers = "JM273606@gmail.com"

message = """From: From Person <jm273606@gmail.com>
To: To Person <JM273606@gmail.com>
Subject: SMTP e-mail test

Insert message here
"""

try 
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender, receivers, message)
	print "successfully sent email"
except SMTPException:
	print "Error: unable to send email"
	
	
	