from twilio.rest import Client
import creds


client = Client(creds.account_sid, creds.auth_token)

message = client.messages.create(
    to=creds.to, 
    from_=creds.from_,
    body="Hello from Python!")

print(message.sid)

