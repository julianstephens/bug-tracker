# from fastapi import Depends, HTTPException, status
# import jwt
# from app.services import settings
# from app.routes import auth_router


# @auth_router.post("/token")
# def verify(token: str = Depends(token_auth_scheme)):
#     signing_key = None

#     verify_ex = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     try:
#         signing_key = client.get_signing_key_from_jwt(token).key
#     except jwt.exceptions.PyJWKClientError as error:
#         raise verify_ex
#     except jwt.exceptions.DecodeError as error:
#         raise verify_ex

#     try:
#         payload = jwt.decode(
#             token,
#             signing_key,
#             algorithms=AUTH0_ALGORITHMS,
#             audience=AUTH0_AUDIENCE,
#             issuer=AUTH0_ISSUER,
#         )
#     except Exception as e:
#         raise verify_ex

#     return payload
