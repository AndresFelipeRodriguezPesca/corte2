from django.urls import path
from . import views


app_name="formlabs"

urlpatterns =[
    path('',views.save, name="save_client"),

]