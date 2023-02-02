import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "valenpendragon@gmail.com"
    # Get this password before testing.
    password = os.getenv("PASSWORD")
    receiver = "valenpendragon@hotmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    message = """
        Hi!
        How are you:
        Bye!
        """
    send_email(message)
