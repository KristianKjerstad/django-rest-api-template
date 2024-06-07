

from ninja import Schema


class HelloSchema(Schema):
    name: str = "world"

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # Unauthenticated users don't have the following fields, so provide defaults.
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class Error(Schema):
    message: str