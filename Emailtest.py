__author__ = 'Steve'

import smtplib

to = 'stephen_b12@yahoo.com'
gmail_user = 'ozzshoppinglist@gmail.com'

gmailpassword= '************'

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user,gmailpassword)

header= 'To:'+ to + '\n' + 'From:' + gmail_user + '\n' + 'Subject:Home Shopping List\n'
#construct the body of the mesage and assign it to msg
msg = header + '\n this is a msg from Steves python program \n \n'
#send email to the given email address using, sendmail protocol
smtpserver.sendmail(gmail_user,to,msg)
print("done")#once email has been sent print done to the user
smtpserver.close() #close call to the smtp object

