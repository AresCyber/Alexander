from august.api import Api 
from august.authenticator import Authenticator, AuthenticationState

#this file is mainly for acquiring access_token_cache_file.txt

api = Api(timeout=20)
authenticator = Authenticator(api, "email", "email@email.com", "Password",
                              access_token_cache_file="access_token_cache_file.txt")

authentication = authenticator.authenticate()

# State can be either REQUIRES_VALIDATION, BAD_PASSWORD or AUTHENTICATED
# You'll need to call different methods to finish authentication process, see below
##state = authentication.state

#authenticator.send_verification_code()
# Wait for your code and pass it in to validate_verification_code()
#validation_result = authenticator.validate_verification_code(105726)
# If ValidationResult is INVALID_VERIFICATION_CODE, then you'll need to either enter correct one or resend by calling send_verification_code() again
# If ValidationResult is VALIDATED, then you'll need to call authenticate() again to finish authentication process
#authentication = authenticator.authenticate()

# Once you have authenticated and validated you can use the access token to make API calls
locks = api.get_locks(authentication.access_token)


print(locks)

self.api.get_lock_status(self.access_token, self.id)