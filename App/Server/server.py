import uvicorn
from fastapi import FastAPI
from fastapi import Body, Depends

# [TODO]
from App.Server.Models.model import Tone, Source, Model_extract_dataset
from App.Server.APIs.auth import jwt_handler
from App.Server.APIs.auth.jwt_handler import signJWT
from App.Server.APIs.auth.jwt_bearer import jwtBearer


app = FastAPI()

# [TODO] -> create a get users from db
users

# [TODO]user sign up 
@app.post('/', tags=["Model_pickle_files"])
def user_signup(model: Model_extract_dataset = Body(default=None)):

    return signJWT(model)

# [TODO]
@app.get('/', tags="ENDPOINTS")
def home(): # pass schema as arg
    return {
        "home" :"Route"
    }