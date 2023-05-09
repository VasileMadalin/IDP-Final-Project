from fastapi import FastAPI, status
import json
import jwt
import MySQLdb
import sys
from os import getenv

app = FastAPI()


from datastructures import PayloadCommentRequest

@app.post('/api/comments', status_code=status.HTTP_201_CREATED)
async def comments(form_data: PayloadCommentRequest):
	
    DB_NAME = 'Tweetsdb'

    db = MySQLdb.connect(
        host='mysql',
        port=int(getenv('MYSQL_PORT')),
        user='root',
        passwd='root',
        db=DB_NAME
    )
    
    cr = db.cursor()

    tabel = "Comments"

    token = form_data.token
    secret_key = "secret_key"
    algorithm = "HS256" # the algorithm used to sign the token

    # Decode the token
    decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
    username = decoded_token['username']

    string = 'INSERT INTO ' + tabel + ' (idtweet, author, comment) VALUES ' + '(' + str(form_data.idtweet) + ',' + '"' + username + '"' + ',' + '"' + form_data.comment + '"' + ')'

    cr.execute(string)
    db.commit()

    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return decoded_token
