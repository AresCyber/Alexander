from august.api import Api 
from august.authenticator import Authenticator, AuthenticationState
import time

class SmartLock:

    def __init__(self):
        self.api = Api(timeout=20)
        self.authenticator = Authenticator(self.api, "email", "email@email.com", "Password",
                                access_token_cache_file="access_token_cache_file.txt")
        self.id='id number'
        self.authentication = self.authenticator.authenticate()
        self.access_token = self.authentication.access_token

    def get_smartlock_status(self):
        self.api.get_lock_status(self.access_token, self.id)

    def unlock(self):
        unlock_response = self.api.unlock(self.access_token, self.id)
        print(unlock_response)
    
    def lock(self): 
        self.api.lock(self.access_token, self.id)

def main():
    smart_lock_instance = SmartLock()
    time.sleep(6)
    #smart_lock_instance.lock()



if __name__ == "__main__":
    main()