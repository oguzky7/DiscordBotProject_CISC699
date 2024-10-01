# email_utils.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from utils.Config import Config

def send_email_with_attachments():
    try:
        # Setup the MIME
        msg = MIMEMultipart()
        msg['From'] = Config.EMAIL_USER
        msg['To'] = Config.EMAIL_RECEIVER
        msg['Subject'] = "Exported Files from Discord Bot"

        # Body of the email
        body = "Attached are the exported files you requested."
        msg.attach(MIMEText(body, 'plain'))

        # Attach XLSX and HTML files
        folder_path = './ExportedFiles'
        for folder, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(folder, file)
                attachment = open(file_path, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {file}")
                msg.attach(part)
                attachment.close()

        # Send the email
        server = smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT)
        server.starttls()
        server.login(Config.EMAIL_USER, Config.EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(Config.EMAIL_USER, Config.EMAIL_RECEIVER, text)
        server.quit()

        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
