from django.urls import path
from ninja import NinjaAPI
from ninja.security import HttpBearer

from apitemplate.api import router as api_router
from apitemplate.exceptions import ServiceUnavailableError
from tracks.api import router as tracks_router


class InvalidToken(Exception):
    pass


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":  # nosec
            return token
        raise InvalidToken


openapi_extra = {
    "info": {"termsOfService": "https://example.com/terms/"},
}


api = NinjaAPI(
    csrf=True,
    auth=GlobalAuth(),
    version="1.0.0",
    openapi_extra=openapi_extra,
    title="Demo API",
    description="This is a demo API with dynamic OpenAPI info section",
)
api.add_router("/tracks", tracks_router)
api.add_router("/api", api_router)


@api.exception_handler(InvalidToken)
def on_invalid_token(request, exc):
    return api.create_response(request, {"detail": "Invalid token supplied"}, status=401)


@api.exception_handler(ServiceUnavailableError)
def service_unavailable(request, exc):
    return api.create_response(
        request,
        {"message": "Please retry later"},
        status=503,
    )


urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("api/", api.urls),
    path("", api.urls)
]
