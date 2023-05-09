from typing import List
import json
import jwt
import MySQLdb
from fastapi import FastAPI, status, Header
import sys
from os import getenv

app = FastAPI()


from datastructures import TokenPayload

RESPONSE_CONTENT_TYPE = 'application/json'

@app.post('/api/tweets', status_code=status.HTTP_201_CREATED)
async def tweets(form_data: TokenPayload):

    DB_NAME = 'Tweetsdb'

    db = MySQLdb.connect(
        host='mysql',
        port=int(getenv('MYSQL_PORT')),
        user='root',
        passwd='root',
        db=DB_NAME
    )
    cr = db.cursor()

    tabel = "Tweets"

    token = form_data.token
    secret_key = "secret_key"
    algorithm = "HS256" # the algorithm used to sign the token

    # Decode the token
    decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
    username = decoded_token['username']

    string = 'INSERT INTO ' + tabel + ' (author, messagetweets) VALUES ' + '(' + '"' + username + '"' + ',' + '"' + form_data.message + '"' + ')'

    cr.execute(string)
    db.commit()

    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return decoded_token
