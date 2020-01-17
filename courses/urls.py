from django.urls import path
from . import views

urlpatterns = [
    path("",views.course_list),
    path("<int:course_pk>/<int:step_pk>",views.step_detail),
    path("<int:pk>",views.course_detail)
]
