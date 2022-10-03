# for signing, encoding and deconding the tokens
import re
import time
from datetime import datetime

import jwt
from decouple import config

# [TODO] tokens generation
JWT_SECRET = config("secret")
JWT_ALGORITHIM = config("algorithim")


# [TODO] generated token resonse
def token_response(token: str):

    return {
        "access token" : token
    }

# [TODO] generate token on sign i
def signJWT(userID: str):
    
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 600

    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHIM)

    return token_response(token)

# [TODO]decoding the jwt token
def decodeJWT(token: str):

    try:
        
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHIM)
        return decode_token if decode_token["expiry"] >= time.time() else None
    
    except:
        return {}