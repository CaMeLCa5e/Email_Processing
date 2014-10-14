#email ex 2. sending HTML through email. 

import smtplib

message = ""From: From Person <from@fromdomain.com>
To: to Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

message here------- 

<b>This is HTML message. </b>
<h1>This is the headline. </h1>

try:
	smtpObj = smtplib.SMTP ('localhost')
	smtpObj.sendmail(sender, receivers, message)
	print "Successfully sent email"
except SMTPException:
	print "Error: unable to send email"
	