import os
import smtplib

EMAIL_ADDRESS=os.environ.get('EMAIL_USER')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    subject='Nepal Book Depot'
    body='You logged into the system successfully'
    
    msg=f'subject: {subject}\n\n{body}'
    
    smtp.sendmail(EMAIL_ADDRESS, 'rushathapa1274@gmail.com', msg)