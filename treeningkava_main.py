import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from treeningplaan import treeningplaan

def treeningkava_main(option1,option2,option3,receiver_email):

    workoutPlan = treeningplaan(option1,option2,option3)
    
    sender_email = ""
    password = ""

    message = MIMEMultipart("alternative")
    message["Subject"] = "Put some beef in yo ramen!"
    message["From"] = sender_email
    message["To"] = receiver_email      

    message.attach(MIMEText(workoutPlan, "plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )