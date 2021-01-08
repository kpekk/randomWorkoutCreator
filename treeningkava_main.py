import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from treeningplaan import treeningplaan

def treeningkava_main(essa,tessa,kossa, meiliaadress):
    #essa = input("1.lihasgrupp: ").lower()
    #tessa = input("2.lihasgrupp: ").lower()
    #kossa = input("3.lihasgrupp: ").lower()

    treeningplaan(essa,tessa,kossa)
    #treeningplaan(essa,tessa)
    sender_email = ""
    receiver_email = meiliaadress
    password = ""

    message = MIMEMultipart("alternative")
    message["Subject"] = "Be there or be a hyperbolic holy ramen"
    message["From"] = sender_email
    message["To"] = receiver_email

    def listToString(s):  
        str1 = ""     
        for ele in s:  
            str1 += ele     
        return str1        
    
    fail = open("treening.txt","r+")
    s = fail.readlines()  

    fail = open("treening.txt","r+")
    text, text2 = listToString(s), listToString(s)

    part1 = MIMEText(text, "plain")
    message.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )