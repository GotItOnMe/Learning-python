#google keyword for sending emails on smptlib
import imaplib
import email
M=imaplib.IMAP4_SSL("imap.gmail.com")
import getpass
user_email='justinhaoq@gmail.com'
password='wtmp lzoh umxj ckww'
M.login(user_email,password)
#print(M.list()) #Everything you can check in email
M.select("INBOX")
#FROM some_string for sending from someone
typ, data=M.search(None,'SINCE 1-Dec-2023') #Format Criteria (e.g. BEFORE date)
print(data[0])#references the email   #^string inside stringn
email_id=data[0]
for email_id in email_id.split():
    result, email_data=M.fetch(email_id,"(RFC822)")
    raw_email=email_data[0][1] #otherwise it would be a mess
    raw_email_string=raw_email.decode("utf-8")
    #print(raw_email_string)
    email_message=email.message_from_string(raw_email_string) #email data
    email_messagelist=email_message.as_string().split()
    #print(email_messagelist)
    for x in email_messagelist:
        if x=='Subject:':
            print('Subject:',email_messagelist[email_messagelist.index(x)+1])
    for part in email_message.walk():
        if part.get_content_type()=="text/plain": #if it is plaintext, do text/html for html
            body=part.get_payload(decode=True) #decodes it
            body=str(body).lstrip("b'").replace("\\r","").replace("\\n","\n")
            print('Body:',body)
        if part.get_content_type()=="text/HTML": #if it is plaintext, do text/html for html
            body=part.get_payload(decode=True) #decodes it
            print('HTML:',body)

