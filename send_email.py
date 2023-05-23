import smtplib
# from email.message import EmailMessage
from email.mime.text import MIMEText
import os


def email_alert(email_from, password, subject, body, to):
    msg = MIMEText(body)  # use msg.set_content(body) if under EmailMessage
    msg['subject'] = subject 
    msg['to'] = to 
    msg['from'] = email_from 

    password = password

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465) # port 587 if EmailMessage()
    # server.starttls()
    server.login(email_from, password)

    print("login successfully!")

    text = msg.as_string()
    server.sendmail(email_from, to, text)

    server.quit()

    print("send email successfully!")

email_from = os.getenv("email")
app_password = os.getenv("app_password")   
sender = os.getenv("sender_email")
print(app_password)
phone_number = os.getenv("phone_number")
print(phone_number)

email_alert(email_from = email_from, password= app_password, subject = 'Hey!', body = 'haha test from miao :D', to = f'{phone_number}@pcs.rogers.com')

# reference: https://sendgrid.com/blog/what-is-starttls/

# i'm using fido account - then try phone_number+mms.fido.ca - unfortunately, it's not working for python
# you can find your carrier info here if you live in Canada https://www.techwyse.com/blog/online-innovation/send-sms-through-email-to-usa-and-canada/
