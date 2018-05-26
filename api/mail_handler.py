# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
def send_read_receipt(sender):
    fromaddr = "info@pandozasolutions.com"
    toaddr = "info@pandozasolutions.com"

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    sender=(sender.split("@")[0]).replace("<","",).replace(">","")


    msgRoot['Subject'] = 'READ Receipt From '+sender+':MHWTC - First Stakeholder Meet'

    msgRoot['From'] = fromaddr
    msgRoot['To'] = toaddr
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    msgRoot['X-MSMail-Priority']="High"
    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText("Mail read by- "+sender)


    msgAlternative.attach(msgText)


    # Define the image's ID as referenced above

    # Send the email (this example assumes SMTP authentication is required)
    import smtplib
    smtp = smtplib.SMTP()
    smtp.connect('mail.pandozasolutions.com', 8025)
    smtp.login(fromaddr, "Info@123456")
    smtp.sendmail(fromaddr, toaddr, msgRoot.as_string())
    smtp.quit()