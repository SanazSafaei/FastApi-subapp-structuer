from datetime import datetime, timedelta
from typing import Any, Union

from passlib.context import CryptContext
from jose import jwt


from core import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
    user_pk: str, model: str, expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "user_pk": user_pk, "model": model}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
