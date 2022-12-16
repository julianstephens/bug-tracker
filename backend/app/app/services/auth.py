from fastapi import Depends, HTTPException, security, status
import jwt

from .config import settings

AUTH0_DOMAIN = settings["AUTH0_DOMAIN"]
AUTH0_AUDIENCE = settings["AUTH0_AUDIENCE"]
AUTH0_ALGORITHMS = settings["AUTH0_ALGORITHMS"]
AUTH0_ISSUER = settings["AUTH0_ISSUER"]
VERIFY_EX = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

client = jwt.PyJWKClient(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
signing_key = None

token_auth_scheme = security.HTTPBearer()


def check_auth(
    token: security.HTTPAuthorizationCredentials = Depends(token_auth_scheme),
):
    try:
        signing_key = client.get_signing_key_from_jwt(token.credentials).key
    except jwt.exceptions.PyJWKClientError:
        raise VERIFY_EX
    except jwt.exceptions.DecodeError:
        raise VERIFY_EX

    try:
        payload = jwt.decode(
            token.credentials,
            signing_key,
            algorithms=AUTH0_ALGORITHMS,
            audience=AUTH0_AUDIENCE,
            issuer=AUTH0_ISSUER,
        )
    except:
        raise VERIFY_EX

    return payload
