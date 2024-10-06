# email_utils.py
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from utils.Config import Config

def send_email_with_attachments(file_name=None):
    try:
        # Setup the MIME
        msg = MIMEMultipart()
        msg['From'] = Config.EMAIL_USER
        msg['To'] = Config.EMAIL_RECEIVER
        msg['Subject'] = "Exported Files from Discord Bot"
        
        # Body of the email
        body = "Attached is the exported file you requested."
        msg.attach(MIMEText(body, 'plain'))

        # Check if a specific file was requested
        if file_name:
            file_path = None
            # Search in both directories
            for folder in ['excelFiles', 'htmlFiles']:
                possible_path = os.path.join('./ExportedFiles', folder, file_name)
                if os.path.exists(possible_path):
                    file_path = possible_path
                    break

            if not file_path:
                return f"File '{file_name}' not found in either excelFiles or htmlFiles."

            # Attach the requested file
            attachment = open(file_path, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {file_name}")
            msg.attach(part)
            attachment.close()
        else:
            return "Please specify a file to send."

        # Send the email
        server = smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT)
        server.starttls()
        server.login(Config.EMAIL_USER, Config.EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(Config.EMAIL_USER, Config.EMAIL_RECEIVER, text)
        server.quit()

        return f"Email with file '{file_name}' sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
