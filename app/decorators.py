from functools import wraps
from flask import abort

user_list = ["arevalo","dani","chob","chueca","edu","richi","julio","borja","javi"]

def valid_user(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if kwargs['nickname'] in user_list:
            return f(*args, **kwargs)
        else:
            return abort(404)
    return decorated_function
    
