import re
import smtplib


def message():
    f2 = open('out.txt', 'w')
    ecount = 0
    ccount = 0
    with open('error_log.txt', 'r') as f:
        for line in f:
            list = re.findall("(?:CRITICAL|ERROR)", line)
            for line in list:
                if line == 'ERROR':
                    ecount += 1
                    f2.write(line + "\n")
                else:
                    ccount += 1
                    f2.write(line + "\n")

    print("Extracted all messages")
    print("The total Error count:", ecount)
    print("The total Critical count:", ccount)
    f2.close()


def sendemail(sender, path):
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = "Logging level Messages"
    body = '''The total Error count: 19\n
             The total Critical count: 10'''
    sender_email = "dandgulepandit@gmail.com"
    receiver_email = "dandgulepandit@gmail.com"
    password = input("Type your password and press enter:")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = path  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


if __name__ == '__main__':
    message()

    sender = input("Enter valid email id:")
    path = 'F:\\Projects\\codingnest\\out.txt'
    sendemail(sender, path)
