from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


from .jwt_handler import decodeJWT

# [TODO]
class jwtBearer(HTTPBearer):

    def __init__(self, auto_Error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)
    
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer,self).__call__(request)

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, details="Invalid or Expiredtoken")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, details="Invalid or Expired token")
    
    # authenticate a token
    def verify_jwt(self, jwtoken:str):

        # false flag
        isTokenValid: bool = False
        payload = decodeJWT(jwtoken)

        if payload:
            isTokenValid = True
        
        return isTokenValid