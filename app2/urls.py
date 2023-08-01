from django.urls import path
from . import views


urlpatterns = [
	path("", views.table, name="table"),
	path("<int:pk>/cs", views.update_student, name="cs"),
    path("sst/<str:pk>", views.student_detail, name="sst"),
    path("sfun", views.search_student, name="sfun"),
    path("create", views.create, name="create"),
    path("<int:pk>/rst", views.rst, name="rst")
]
