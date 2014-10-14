#sending attachment 

import smtplib
import base64

filename = '/tmp/test.txt'

#read file and encode in base64
fo = open(filename, "rb")
filecontent = fo.read.()
encodedcontent = base64.b64encode(filecontent) #base64 (even Kanye can love that base.)

sender = "jm273606@gmail.com"
receiver = "jm273606@gmail.com"

marker = "Marker!"

body = """
This is a test email to send an attachment.
"""

# define headers
part1 = """From: From Person <jm273606@gmail.com>
To: To Person <jm273606@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0 
Content-Type: multipart/mixed: boundary =%s
--%s
""" % (marker, marker)

#Define message in action 

part2 = """ Content-Type: text/plain
Content-Transfer-encoding:8bit

%s
--%s
""" %(body, marker)

#define the attachment section 
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename = %s

%s
--%s-- 
""" % (filename, filename, encodedcontent,marker)
message = part1 + part2 + part3

try:
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender, reciever, message)
	print "Successfully sent email"
except Exception:
	print "Error: unable to sent email"
	
	

























