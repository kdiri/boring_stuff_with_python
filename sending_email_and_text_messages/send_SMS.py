"""
.. module:: sending_email_and_text_messages.send_SMS
   :synopsis: send SMS throughout telecoms operators gateways's
"""

from twilio.rest import Client
from ansicolortags import printc

account_sid = "***"
auth_token = "***"
twilio_number = "***"
my_number = "***"


def create_sms_instance():
    return Client(account_sid, auth_token)


def send_message():
    try:
        twilio_cli = create_sms_instance()
        twilio_cli.messages.create(
            body="This is a test message from Kemal.", from_=twilio_number, to=my_number
        )
        printc(f"<green>Success: SMS send successfully to {my_number}.<white>")
    except Exception as exc:
        printc(f"<red>Error: Error occurred when to send an SMS. {exc}")


if __name__ == "__main__":
    send_message()
