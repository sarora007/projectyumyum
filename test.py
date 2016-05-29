from twilio.rest import TwilioRestClient
account_sid = "AC4bac6baa1f943ac100f2000526a55c7f"
auth_token = "f9608374e4898fcfffd9c611d3ed62f3"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(to="+16142888469", from_="+16148456738",
                                     body="test")