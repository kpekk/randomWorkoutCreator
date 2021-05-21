import smtplib, ssl
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from treeningplaan import treeningplaan

def treeningkava_main(outputType,options,sample_size,receiver_email):

    #skip this part if we're sending a test email
    if(outputType != "testEmail"):
        groups, exercises = treeningplaan(options,sample_size) 

    #output to text file
    if (outputType == "outputToTextFile"):
        with open("workout.txt", "w+") as f:
            for i, group in enumerate(groups):
                f.write(group+"------------\n")
                for exercise in exercises[i]:
                    f.write(exercise+"\n")

    #send email
    else:
        #output to html file only if we're not sending a test email    
        if(outputType != "testEmail"):
            
            #email design & content    
            with open("sample.html", "r+") as f:
                content = ""
                for i, group in enumerate(groups):
                    content += "<div><h2>{group}</h2>".format(group=group)
                    for exercise in exercises[i]:
                        content += "{exercise}<br>".format(exercise=exercise)
                    content +="</div>" #close the div

                html_text = f.read().format(test = content)
            
        #get sender info from email.txt
        sender_email_info = ""
        with open("config\email.txt") as f:
            sender_email_info = f.read().split("\n")

        sender_email = sender_email_info[0].strip()
        password = sender_email_info[1].strip()

        #email info
        message = MIMEMultipart("alternative")
        randId = random.randint(1,12345)
        #using a completely random id to send separate emails (emails in the same convo tend to get quoted and)
        #   that just messes the css styles up
        message["Subject"] = "Ding dong! Get pumping! Or running. Or walking. {id}".format(id=randId)
        message["From"] = sender_email
        message["To"] = receiver_email    

        #sending the real deal
        if(outputType != "testEmail"):
            message.attach(MIMEText(html_text, "html", "utf-8"))
        
        #sending a test email
        else:
            message.attach(MIMEText("Are You seeing me? Me as in the email. You most likely are. All is good.", "plain"))

        #using smtplib to send the email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())