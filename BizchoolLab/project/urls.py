from django.urls import path, re_path
from . import views
urlpatterns = [
    re_path(r'^new/$', views.project_new, name="project_new"),
    re_path(r'^$', views.project_list, name="project_list"),
    re_path(r'^(?P<pk>\d+)/$', views.project_detail, name="project_detail"),
    re_path(r'^(?P<pk>\d+)/Edit/$', views.project_edit, name="project_edit"),

]