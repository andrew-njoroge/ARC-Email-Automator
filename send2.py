# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
ccaddr1 = ''
ccaddr2 = ''
ccaddr3 = ''
ccaddr4 = ''

ccaddr = [ccaddr1,ccaddr2,ccaddr3,ccaddr4]

def get_pops():
    dir_path = r'path to files'
    
    pop_list = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path,path)): 
            pop_list.append(path)

    #print(pop_list)
    return(pop_list)


    
def send_mail(pops):
    
    real_recs = [all recipient emails]
              
    #no_rec = [#jentech;#FDR;#Few Olas # Few Totals,Church_Army]
    fromaddr = EMAIL
    for i in range(len(real_recs)):
        toaddr = real_recs[i]
        print(toaddr)


        # instance of MIMEMultipart 
        msg = MIMEMultipart() 

        # storing the senders email address 
        msg['From'] = fromaddr 

        # storing the receivers email address 
        msg['To'] = toaddr 
        # attempt to cc sammy
        msg['Cc']=','.join(ccaddr)
        #msg['cc'] = ccaddr1
        

        # storing the subject 
     
        msg['Subject'] = "ARC RIDE 2024 POPs"

        # string to store the body of the mail 
        body = "All the mambo jambo you want to place here."

        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 

        # open the file to be sent 
        filename = 'C:/Users/PC/Desktop/ARC RIDE stuff/POP-April/BaaS_One/'+ pops[i]
        print(filename)
        attachment = open(filename, "rb") 

        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 

        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 

        # encode into base64 
        encoders.encode_base64(p) 

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 

        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 

        # start TLS for security 
        s.starttls() 

        # Authentication 
        s.login(fromaddr, PASSWORD) 

        # Converts the Multipart msg into a string 
        text = msg.as_string() 

        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 

    # terminating the session 
    s.quit() 


pops = get_pops()
print(pops)
send_mail(pops)


input( "Are you done ?" )
