
import pathlib

from dotenv import dotenv_values
from twilio.rest import Client

env_path = pathlib.Path(__file__).parent.parent / ".env"
config = dotenv_values(env_path) 

def send_whatsapp_message(text, telephone_number_sender, telephone_number_receiver):

    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = config["TWILIO_ACCOUNT_SID"] # 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = config["TWILIO_AUTH_TOKEN"] # 'your_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                body=text,
                                from_=telephone_number_sender,
                                to=telephone_number_receiver,
                            )

    return message

