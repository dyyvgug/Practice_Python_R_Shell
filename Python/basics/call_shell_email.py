import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Define the shell command you want to execute
command = "ls"

# Execute the shell command and capture the output
output = subprocess.check_output(command, shell=True)

# Specify the file path to save the output
output_file = "output.txt"

# Write the output to a file
with open(output_file, "w") as file:
    file.write(output.decode())  # Convert bytes to string and write to file

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body text to the message
    message.attach(MIMEText(body, "plain"))

    # Open the file in bytestream mode
    with open(attachment_path, "rb") as attachment:
        # Create a base64 encoded attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode the attachment and add a header
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )

    # Attach the attachment to the message
    message.attach(part)

    # Connect to the email server (e.g., Gmail SMTP server)
    with smtplib.SMTP("smtp.office365.com",587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)

# Example usage
sender_email = "hello@outlook.com"
sender_password = "12345"
receiver_email = "hello@mail.com"
subject = "Email with Attachment"
body = "Please find the attached file."
attachment_path = "./output.txt"

send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)


