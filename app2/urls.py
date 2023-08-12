from django.urls import path
from . import views


urlpatterns = [
	path("", views.table, name="table"),
    path("create", views.create, name="create"),
	path("<int:pk>/cs", views.update_student, name="cs"),
    path("<int:pk>/rst", views.rst, name="rst"),
    path("teacher", views.TForm, name="teacher"),
    path("<int:pk>/ut", views.update_teacher, name="ut"),
    path("<int:pk>/rt", views.rt, name="rt"),
    path("subj", views.SubjForm, name="subj"),
    path("<int:pk>/us", views.update_subject, name="us"),
    path("<int:pk>/rsubj", views.rsubj, name="rsubj"),
    path("enroll", views.EnrollForm, name="enroll"),
    path("<int:pk>/uenroll", views.update_enroll, name="uenroll"),
    path("<int:pk>/renroll", views.renroll, name="renroll"),
    path("sfun1", views.search_student, name="sfunst"),
    path("sst/<str:pk>", views.search_detail, name="sst"),
    path("sfun2", views.search_teacher, name="sfunt"),
    path("sst/<str:pk>", views.search_detail, name="ste"),
    path("sfun3", views.search_subject, name="sfunsubj"),
    path("sst/<str:pk>", views.search_detail, name="ssubj")
]
