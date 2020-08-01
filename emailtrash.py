import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = "dhuhydsasadasd@gmail.com"
gmail_password = "1234567890.abcd"

def send_email (message):
    to = ["maivannhatminh2005@gmail.com"]
    sent_from = gmail_user

    msg = MIMEMultipart()
    msg ['From'] = gmail_user
    msg ['To'] = ','.join(to)
    msg ['Subject'] = 'Test'
    text = message

    body = MIMEText(text, 'plain')
    msg.attach(body)

    while True:
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, msg.as_string())
            server.close()

            print ("sent")

        except Exception as e:
            print("something wrong")
            print(e)

send_email("Địt mẹ mày !")