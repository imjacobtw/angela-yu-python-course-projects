from flask import abort
from flask_login import current_user
from functools import wraps


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return f(*args, **kwargs)
        return abort(403)

    return decorated_function
