from django.urls import path
from . import views
from .views import Stapi


urlpatterns = [
	path("", Stapi.as_view(), name="stapi"),
    path("getapi", views.get_api, name="getapi"),
    path("postapi", views.post_api, name="postapi")
]
