from fastapi import FastAPI, status, Request, Response

from conf import settings
from helper import route

from datastructures import (PayloadCommentRequest, TokenPayload, UsernamePasswordForm)

app = FastAPI()

@route(
    request_method=app.post,
    path='/api/auth',
    status_code=status.HTTP_201_CREATED,
    payload_key='username_password',
    service_url=settings.AUTH_SERVICE_URL
)
async def auth(username_password: UsernamePasswordForm,
                request: Request, response: Response):
    pass

@route(
    request_method=app.post,
    path='/api/login',
    status_code=status.HTTP_201_CREATED,
    payload_key='username_password',
    service_url=settings.AUTH_SERVICE_URL
)
async def login(username_password: UsernamePasswordForm,
                request: Request, response: Response):
    pass

@route(
    request_method=app.post,
    path='/api/tweets',
    status_code=status.HTTP_201_CREATED,
    payload_key='payload_token',
    service_url=settings.TWEETS_SERVICE_URL
)
async def tweets(payload_token: TokenPayload,
                request: Request, response: Response):
    pass

@route(
    request_method=app.post,
    path='/api/comments',
    status_code=status.HTTP_201_CREATED,
    payload_key='payload_comment_request',
    service_url=settings.COMMENTS_SERVICE_URL,
)
async def comments(payload_comment_request: PayloadCommentRequest,
                request: Request, response: Response):
    pass