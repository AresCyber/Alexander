from twilio.rest import Client 
 
def sendalert(msgbdy):
    account_sid = 'AC3390bfac3ff99b978d12be2881f7b0c0' 
    auth_token = 'fefad7079ba0f7faeb4b0faf9502748b' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                  from_='+14344046180',  
                                  body=msgbdy,      
                                  to='+16055209594' 
                              ) 
    
    print(message.sid)