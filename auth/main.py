from typing import List
import json
from fastapi import FastAPI, status, HTTPException
import sys
from os import getenv

import MySQLdb
import jwt
import bcrypt
import binascii

app = FastAPI()

from datastructures import UsernamePasswordForm

RESPONSE_CONTENT_TYPE = 'application/json'

@app.post('/api/auth', status_code=status.HTTP_201_CREATED)
async def auth(form_data: UsernamePasswordForm):

	DB_NAME = 'Usersdb'


	db = MySQLdb.connect(
		host='mysql',
		port=int(getenv('MYSQL_PORT')),
		user='root',
		passwd='root',
		db=DB_NAME
	)
	cr = db.cursor()

	password =  bytes(form_data.password, encoding='utf-8')
	
	hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
	hashed_password_hex = binascii.hexlify(hashed_password).decode('utf-8')

	tabel = "Users"

	string = 'INSERT INTO ' + tabel + ' (username, passorwd) VALUES ' + '(' + '"' + form_data.username + '"' + ',' + '"' + hashed_password_hex + '"' + ')'
	
	cr.execute(string)
	db.commit()
	
	cr.execute('SELECT * FROM Users')
	return "user inregistrat cu succes"

@app.post('/api/login', status_code=status.HTTP_201_CREATED)
async def login(form_data: UsernamePasswordForm):

	DB_NAME = 'Usersdb'


	db = MySQLdb.connect(
		host='mysql',
		port=int(getenv('MYSQL_PORT')),
		user='root',
		passwd='root',
		db=DB_NAME
	)
	cr = db.cursor()

	secret_key = "secret_key"

	# Definește informațiile de payload
	payload = {
	    "username": form_data.username,
	}

	user = 'SELECT * FROM Users WHERE username = ' + '"' + form_data.username + '"'
	cr.execute(user)	

	response = cr.fetchone()

    # If no user is found, raise an HTTPException
	if response is None:
		raise HTTPException(status_code=404, detail="User not found")

	hashed_password_hex = response[2]
	hashed_password = binascii.unhexlify(hashed_password_hex)

	if bcrypt.checkpw(form_data.password.encode('utf-8'), hashed_password):
		jwt_token = jwt.encode(payload, secret_key, algorithm="HS256")
		return jwt_token
	else:
		raise HTTPException(status_code=403, detail="Credentiale incorecte")
