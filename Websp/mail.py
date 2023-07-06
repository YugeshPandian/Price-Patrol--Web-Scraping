import smtplib


def mailsend(to_add,subject,message):
    
    smtp_obj=smtplib.SMTP('smtp.gmail.com',587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    email='yukpandian@gmail.com'
    password='tqmuxihwbzzbbmib'
    smtp_obj.login(email,password)
    from_add=email
    msg=f"Subject: {subject}\n\n{message}"
    msg = msg.encode('utf-8')
    smtp_obj.sendmail(from_addr=from_add,to_addrs=to_add,msg=msg)
    smtp_obj.quit()