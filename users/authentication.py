import jwt
import datetime
from django.conf import settings


def access_tokens(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
