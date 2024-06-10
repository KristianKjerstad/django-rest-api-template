from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja.security import django_auth, HttpBearer

from tracks.api import router as tracks_router
from apitemplate.api import router as api_router

class InvalidToken(Exception):
    pass


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token
        raise InvalidToken

api = NinjaAPI(csrf=True, auth=GlobalAuth())
api.add_router("/tracks", tracks_router)
api.add_router("/api", api_router)

@api.exception_handler(InvalidToken)
def on_invalid_token(request, exc):
    return api.create_response(request, {"detail": "Invalid token supplied"}, status=401)


urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("api/", api.urls),
    path("", api.urls)
]
