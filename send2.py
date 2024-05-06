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
ccaddr1 = 'sammy.waweru@arcrideglobal.com'
ccaddr2 = 'jeremy.kimbo@arcrideglobal.com'
ccaddr3 = 'vivien.wambui@arcrideglobal.com'
ccaddr4 = 'jennifer.mbithe@arcrideglobal.com'

ccaddr = [ccaddr1,ccaddr2,ccaddr3,ccaddr4]

def get_pops():
    dir_path = r'C:/Users/PC/Desktop/ARC RIDE stuff/POP-April/BaaS_One'
    # C:/Users/PC/Desktop/ARC RIDE stuff/POP-February/Baas-Pop
    # C:/Users/PC/Desktop/ARC RIDE stuff/POP-April/BaaS
    pop_list = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path,path)): 
            pop_list.append(path)

    #print(pop_list)
    return(pop_list)


    
def send_mail(pops):

    #mail_recs = ['njorogekariuki022@gmail.com','rewand.njoroge@gmail.com']#,"andrew.njoroge@arcrideglobal.com"]#,"kariukicharitywanja@gmail.com","sammy.waweru@arcrideglobal.com","mary.wanjeri@arcrideglobal.com","stacy.kibarak@arcrideglobal.com"]
    
    real_recs = ['rewand.njoroge@gmail.com','Ellykabugi@gmail.com','bodabossie@gmail.com','rewand.njoroge@gmail.com',
                 'georgemlami@yahoo.com','wanyamajackson898@gmail.com','cnautosolution@gmail.com','cycleplanetspareparts@gmail.com',
                 'cycleplanetspareparts@gmail.com','thomas.obaga@yahoo.com','jaspergitosh2000@gmail.com','emasterworks@gmail.com',
                 'bonnynjenga93@gmail.com','jecywain@gmail.com','rewand.njoroge@gmail.com','gecocafe@gecotribe.com','paulwachira28@gmail.com',
                 'rosemarykabui@gmail.com','zephanngure@gmail.com','bikeworldke@outlook.com','Martin.Waititu@hfgroup.co.ke',
                 'rewand.njoroge@gmail.com','gibsonmburu9@gmail.com','johnkuria0722@gmail.com','ramno89@gmail.com','gitarigerald2018@gmail.com',
                 'kamauwandiritu@gmail.com','kanotiowino@gmail.com','lincolnwamae17@gmail.com','benisonim@yahoo.com','davidsmercy@yahoo.com',
                 'muigaikaranu@gmail.com','meshkimz30@gmail.com','rewand.njoroge@gmail.com','nanwanja2000@gmail.com','petermugaiiii@gmail.com',
                 'william.wachiuri@yahoo.com','fuelchoicelimited@gmail.com','davidhingah@gmail.com','rewand.njoroge@gmail.com','tricentke@gmail.com',
                 'jkabugi09@gmail.com','james.thuku@powergovernors.co.ke','purplebasket.pb@gmail.com','kimkadah@gmail.com','cad.subarksfinance@gmail.com',
                 'rapidshineke@gmail.com','robbybikes@gmail.com','jckmwania@gmail.com','samm6137@gmail.com',]
              
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
        #msg['Subject'] = "ARC RIDE 2024 POPs "
        msg['Subject'] = "ARC RIDE 2024 POPs"

        # string to store the body of the mail 
        body = "Good morning esteemed ARCRIDE SITE PARTNER. PFA the Proof of Payment Document issued in APRIL 2024. We appreciate your continued support and wish you a productive month ahead.\n Kind regards,"

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