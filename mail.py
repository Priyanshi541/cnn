import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "kailapriyanshi541@gmail.com"
host_pass = "preeti2010"
guest_address = "kailapriyanshi541@gmail.com"
subject = "80% Accuracy Acheived "
content = "We would like to inform you that your model has successfully achieved more than 80% accuracy";
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
