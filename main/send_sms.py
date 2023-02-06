
from twilio.rest import Client

def sendsms():
    account_sid = "AC8d50a1df4e9697ddc6e8124c5eec7b5f"
    auth_token = "dba101247e7079fc97d39f6331b38316"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body="Time for medication ",
    from_="+13134509713",
    to="+256775949201"
    ) 

    print('Message sent successfuly')