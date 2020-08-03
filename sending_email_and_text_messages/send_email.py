"""
.. module:: sending_email_and_text_messages.seend_email
   :synopsis: send email using a gmail account

"""
import smtplib

gmail_user = "mymail@gmail.com"
gmail_password = "myP@ssword!"
to = [gmail_user, "you@gmail.com"]


def construct_email() -> str:
    return """
            From: mymail@gmail.com
            To: yourmail@gmail.com
            Subject: Test
            Body: Test mail
            """


def send_mail():
    email_text = construct_email()
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, email_text)
        server.close()
    except Exception as Ex:
        print(f"Something went wrong... {Ex}")


if __name__ == "__main__":
    send_mail()
