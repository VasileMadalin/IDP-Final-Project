import aiohttp
import functools
import async_timeout

from conf import settings

from fastapi import Request, Response, HTTPException, status
from typing import List

async def make_request(url: str, method: str, data: dict = None, headers: dict = None):
    
    if not data:
        data = {}

    with async_timeout.timeout(settings.GATEWAY_TIMEOUT):
        async with aiohttp.ClientSession() as session:
            request = getattr(session, method)
            async with request(url, json=data, headers=headers) as response:
                data = await response.json()
                return (data, response.status)

def route(request_method, path: str, status_code: int, payload_key: str, service_url: str):
    
    app_any = request_method(
        path, status_code=status_code
    )

    def wrapper(f):
        @app_any
        @functools.wraps(f)
        async def inner(request: Request, response: Response, **kwargs):
            service_headers = {}

            scope = request.scope

            method = scope['method'].lower()
            path = scope['path']

            payload_obj = kwargs.get(payload_key)
            payload = payload_obj.dict() if payload_obj else {}

            url = f'{service_url}{path}'

            try:
                resp_data, status_code_from_service = await make_request(
                    url=url,
                    method=method,
                    data=payload,
                    headers=service_headers,
                )
            except aiohttp.client_exceptions.ClientConnectorError:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail='Service is unavailable.',
                )
            except aiohttp.client_exceptions.ContentTypeError:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail='Service error.',
                )

            response.status_code = status_code_from_service

            return resp_data

    return wrapper