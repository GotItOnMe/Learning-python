#sends email
import smtplib
import getpass #get pass hides it when entering
print("import successful")
s=smtplib.SMTP("smtp.gmail.com",587) #otherwise use 465
s.ehlo()
s.starttls() #delete this if other
email='justinhaoq@gmail.com'
password='wtmp lzoh umxj ckww'
s.login(email,password)
#if disconnected, generate another APP password
from_address=email
to_address=input("who to send the email to?") #email of recipient
subject=input("enter the subject line")
message=input("enter the body message")
msg=subject+"\n"+message
s.sendmail(from_address,to_address,msg)
s.quit()

