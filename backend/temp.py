from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from auth import AuthHandler
from schemas import AuthDetails

app = FastAPI()

auth_handler = AuthHandler()
users = []

@app.post('/register')
def register(auth_details: AuthDetails):
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(status_code=400, detail="Username is taken")
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password
    })
    return

@app.post('/login')
def login(auth_details: AuthDetails):
    user = None
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break
    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid usrname and or password!')
    token = auth_handler.encode_token(user['username'])
    return {'token':token}

@app.post('/unprotected')
def unprotected():
    return {'hello' : 'world!'}

@app.post('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'name': username}


