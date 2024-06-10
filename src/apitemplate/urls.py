from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI


from tracks.api import router as tracks_router
from apitemplate.api import router as api_router

api = NinjaAPI()
api.add_router("/tracks", tracks_router)
api.add_router("/api", api_router)

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("api/", api.urls),
    path("", api.urls)
]
