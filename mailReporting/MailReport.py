import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mailReporting import GenerateMail
from configuration import Configuration

class Report_Mailer():
    def send_mail(self, statusReport):
        body = GenerateMail.MailGenerate.generateMailBody(self, statusReport)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(Configuration.StatusConfig.mail_userName, Configuration.StatusConfig.mailpassword)
        msg = "\n!!!-----Daily Status Report----!!!"
        server.sendmail(Configuration.StatusConfig.send_mail1, Configuration.StatusConfig.send_mail2, msg)

        fromaddr = Configuration.StatusConfig.mail_userName
        toaddr = Configuration.StatusConfig.send_mail1
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Python email"

        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)

